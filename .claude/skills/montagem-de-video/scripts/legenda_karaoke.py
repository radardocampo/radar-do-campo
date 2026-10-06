# -*- coding: utf-8 -*-
"""Legenda karaoke no padrao do canal (medido na montagem feita a mao pelo usuario):
  - a palavra que esta sendo falada fica amarela (#FAFE05); as outras, brancas
  - 1 linha, 2-3 palavras, fecha no fim de frase, nunca quebra em 2 linhas
  - Montserrat ExtraBold Italic (peso 800), ~3,1% da altura (80px em 2560)
  - contorno preto + sombra preta difusa e encorpada
  - centro do texto a ~54% da altura
  - minusculas; nome proprio com maiuscula; grafia e numeros como no ROTEIRO
Gera uma faixa de video com alpha (mov/qtrle) com so a banda da legenda.
Uma faixa unica e sobreposta uma vez: encadear dezenas de overlays no ffmpeg
descartou legendas em silencio numa montagem anterior.

uso:
  python legenda_karaoke.py --palavras palavras.json --roteiro roteiro.txt \
      --dur <segundos> --saida <pasta>  [--quadro amostra.png]
gera em <pasta>: faixa_legenda.mov, banda.json, blocos_legenda.json, legenda_capcut.srt
(o render_final.py copia o .srt para "<job>/legenda para o CapCut.srt")
"""
import argparse, difflib, json, os, re, shutil, subprocess, unicodedata
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--palavras", required=True)
ap.add_argument("--roteiro", help="texto do roteiro (grafia, numeros por extenso, nomes)")
ap.add_argument("--dur", type=float, required=True, help="duracao final do video")
ap.add_argument("--saida", required=True)
ap.add_argument("--fonte", default=os.path.join(AQUI, "..", "assets", "Montserrat-Italic-VF.ttf"))
ap.add_argument("--W", type=int, default=1440)
ap.add_argument("--H", type=int, default=2560)
ap.add_argument("--centro", type=float, default=0.54, help="centro vertical (fracao da altura)")
ap.add_argument("--tamanho", type=float, default=0.031, help="fonte em fracao da altura")
ap.add_argument("--max-palavras", type=int, default=3)
ap.add_argument("--nomes", default="", help="nomes proprios extras, separados por virgula (ex.: Varela,Carrascal)")
ap.add_argument("--quadro", help="imagem 1440x2560 para gerar uma previa com a legenda")
ap.add_argument("--previa", default="", help="trecho do texto do bloco a usar na previa")
a = ap.parse_args()
from pasta_job import dentro_do_job
dentro_do_job(a.saida)

W, H = a.W, a.H
AMARELO, BRANCO, PRETO = (250, 254, 5, 255), (255, 255, 255, 255), (0, 0, 0, 255)
FS = round(H * a.tamanho)
STROKE = max(3, round(W * 0.0028))     # ~4px em 1440
SOMBRA_BLUR = max(4, round(FS * 0.08))
MARGEM = round(W * 0.06)
BANDA_H = round(FS * 3.2)
BANDA_Y = round(H * a.centro - BANDA_H / 2)

fonte = ImageFont.truetype(a.fonte, FS)
try:
    fonte.set_variation_by_axes([800])
except Exception:
    pass

def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^\w]", "", "".join(c for c in s if unicodedata.category(c) != "Mn"))

def limpa(t):
    return re.sub(r"^[^\wÀ-ÿ]+|[^\wÀ-ÿ]+$", "", t)

# ---------- 1) texto: grafia do roteiro sobre o tempo do Whisper ----------
W_ = json.load(open(a.palavras, encoding="utf-8"))
FIM = r"[.!?,:;]$"   # o bloco fecha em fim de frase e em pausa marcada no texto
wh = [{"t": limpa(p["w"]), "ini": p["ini"], "fim": p["fim"], "fimfrase": bool(re.search(FIM, p["w"].strip()))}
      for p in W_ if limpa(p["w"])]

proprios = {norm(n) for n in a.nomes.split(",") if n.strip()}
# palavras comuns que abrem frase e NAO sao nome proprio
COMUNS = set(norm(x) for x in """a o as os um uma uns umas e ou mas se so ja nem nao sim
na no nas nos da do das dos de em por pra para pelo pela com sem sobre entre ate apos
aos as ao depois antes agora entao quando onde como porque porem ainda tambem muito pouco
ele ela eles elas eu voce voces isso isto aquilo esse essa este esta aquele aquela
foi era e esta estava tinha teve fez faz vai veio parecia ficou virou saiu voltou
hoje ontem amanha nunca sempre todo toda todos todas cada mais menos quase bem mal
aqui ali la vamos veja olha imagina resultado final primeiro segundo terceiro""".split())
if a.roteiro:
    txt = open(a.roteiro, encoding="utf-8").read()
    toks = re.findall(r"[\wÀ-ÿ]+(?:-[\wÀ-ÿ]+)*[.!?,:;]?", txt)
    rot = []
    inicio_frase = True
    for tk in toks:
        palavra = limpa(tk)
        if not palavra:
            continue
        if palavra[0].isupper() and not inicio_frase:
            proprios.add(norm(palavra))
        rot.append({"t": palavra, "fimfrase": bool(re.search(FIM, tk))})
        inicio_frase = bool(re.search(r"[.!?]$", tk))
    # Palavra em maiuscula SO no inicio de frase nao vira nome proprio (o chute antigo
    # deixou "Dezesseis", "Naquela", "Achou" em maiuscula). Nome que so aparece no
    # inicio de frase entra por --nomes.
    sm = difflib.SequenceMatcher(a=[norm(x["t"]) for x in wh], b=[norm(x["t"]) for x in rot], autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal" or (op == "replace" and (i2 - i1) == (j2 - j1)):
            for k in range(i2 - i1):
                wh[i1 + k]["t"] = rot[j1 + k]["t"]
                wh[i1 + k]["fimfrase"] = rot[j1 + k]["fimfrase"]
        elif op == "replace" and (i2 - i1) == 1:
            # 1 token do Whisper virou varios no roteiro (ex.: "0" -> "zero a zero"): junta
            wh[i1]["t"] = " ".join(r["t"] for r in rot[j1:j2])
            wh[i1]["fimfrase"] = rot[j2 - 1]["fimfrase"]

# Numero que sobrou em algarismo (o Whisper escreve "2", "20", "50" e o roteiro tambem pode ter
# digito) vai por extenso, como a voz fala (Endrick, set/2026: "dois a 2", "uns 20 minutos").
UNI = "zero um dois tres quatro cinco seis sete oito nove dez onze doze treze quatorze quinze dezesseis dezessete dezoito dezenove".split()
UNI = [u.replace("tres", "três") for u in UNI]
DEZ = {2: "vinte", 3: "trinta", 4: "quarenta", 5: "cinquenta", 6: "sessenta", 7: "setenta", 8: "oitenta", 9: "noventa"}
CEM = {1: "cento", 2: "duzentos", 3: "trezentos", 4: "quatrocentos", 5: "quinhentos", 6: "seiscentos",
       7: "setecentos", 8: "oitocentos", 9: "novecentos"}
def extenso(v):
    if v < 20: return UNI[v]
    if v < 100: return DEZ[v // 10] + ("" if v % 10 == 0 else " e " + UNI[v % 10])
    if v == 100: return "cem"
    if v < 1000: return CEM[v // 100] + ("" if v % 100 == 0 else " e " + extenso(v % 100))
    return None
for p in wh:
    if re.fullmatch(r"\d{1,3}", p["t"]):
        e = extenso(int(p["t"]))
        if e: p["t"] = e

def caixa(t):
    return " ".join(p if norm(p) in proprios else p.lower() for p in t.split(" "))
for p in wh:
    p["t"] = caixa(p["t"])

# ---------- 2) blocos de ate N palavras, 1 linha, fecham no fim de frase ----------
med = ImageDraw.Draw(Image.new("L", (8, 8)))
def larg(t):
    b = med.textbbox((0, 0), t, font=fonte, stroke_width=STROKE)
    return b[2] - b[0]
ESP = larg("a a") - 2 * larg("a")

blocos, i = [], 0
while i < len(wh):
    n = 1
    while (n < a.max_palavras and i + n < len(wh) and not wh[i + n - 1]["fimfrase"]
           and sum(larg(x["t"]) for x in wh[i:i + n + 1]) + ESP * n <= W - 2 * MARGEM):
        n += 1
    blocos.append(wh[i:i + n]); i += n

# ---------- 3) estados: um por palavra ativa ----------
estados = []   # (ini, fim, bloco_idx, palavra_ativa)
for bi, b in enumerate(blocos):
    prox = blocos[bi + 1][0]["ini"] if bi + 1 < len(blocos) else a.dur
    fim_bloco = prox if prox - b[-1]["fim"] <= 0.6 else b[-1]["fim"] + 0.15
    for k, p in enumerate(b):
        ini = p["ini"]
        fim = b[k + 1]["ini"] if k + 1 < len(b) else fim_bloco
        estados.append((ini, min(fim, a.dur), bi, k))

def desenha(bloco, ativa):
    img = Image.new("RGBA", (W, BANDA_H), (0, 0, 0, 0))
    textos = [p["t"] for p in bloco]
    total = sum(larg(t) for t in textos) + ESP * (len(textos) - 1)
    x0, y = (W - total) / 2, BANDA_H / 2
    # sombra difusa
    sombra = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ds = ImageDraw.Draw(sombra); x = x0
    for t in textos:
        ds.text((x, y + STROKE), t, font=fonte, fill=(0, 0, 0, 255), anchor="lm",
                stroke_width=STROKE * 3, stroke_fill=(0, 0, 0, 255))
        x += larg(t) + ESP
    borrada = sombra.filter(ImageFilter.GaussianBlur(SOMBRA_BLUR))
    img = Image.alpha_composite(Image.alpha_composite(img, borrada), borrada)  # 2x = sombra encorpada
    d = ImageDraw.Draw(img); x = x0
    for k, t in enumerate(textos):
        d.text((x, y), t, font=fonte, fill=AMARELO if k == ativa else BRANCO, anchor="lm",
               stroke_width=STROKE, stroke_fill=PRETO)
        x += larg(t) + ESP
    return img

# ---------- 4) faixa de video com alpha ----------
tmp = os.path.join(a.saida, "_leg_png")
shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
Image.new("RGBA", (W, BANDA_H), (0, 0, 0, 0)).save(os.path.join(tmp, "vazio.png"))
linhas, t = [], 0.0
def add(nome, d):
    if d > 0.0005:
        linhas.append(f"file '{nome}'"); linhas.append(f"duration {d:.4f}")
for n, (ini, fim, bi, k) in enumerate(estados):
    if ini > t:
        add("vazio.png", ini - t)
    nome = f"e{n:04d}.png"
    desenha(blocos[bi], k).save(os.path.join(tmp, nome))
    add(nome, fim - max(ini, t)); t = max(t, fim)
if t < a.dur:
    add("vazio.png", a.dur - t)
linhas.append("file 'vazio.png'")
open(os.path.join(tmp, "lista.txt"), "w", encoding="utf-8").write("\n".join(linhas) + "\n")
faixa = os.path.join(a.saida, "faixa_legenda.mov")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i",
                os.path.join(tmp, "lista.txt"), "-vf", "fps=60,format=rgba", "-c:v", "qtrle",
                "-t", f"{a.dur:.3f}", faixa], check=True)
json.dump({"y": BANDA_Y, "h": BANDA_H, "w": W}, open(os.path.join(a.saida, "banda.json"), "w"))
json.dump([{"ini": b[0]["ini"], "fim": b[-1]["fim"], "texto": " ".join(p["t"] for p in b)} for b in blocos],
          open(os.path.join(a.saida, "blocos_legenda.json"), "w", encoding="utf-8"), indent=0, ensure_ascii=False)
# SRT com a grafia certa para o usuario importar no CapCut em vez da legenda automatica dele
# (Raphinha, set/2026: a automatica escreveu "Rafinha" e trocou "a coxa dele ta pedindo socorro"
# por "Rafinha teve uma lesao"). Mesmos blocos e tempos da faixa karaoke.
def hms(s):
    ms = int(round(s * 1000)); return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"
srt = []
for bi, b in enumerate(blocos):
    prox = blocos[bi + 1][0]["ini"] if bi + 1 < len(blocos) else a.dur
    fim_b = min(prox if prox - b[-1]["fim"] <= 0.6 else b[-1]["fim"] + 0.15, a.dur)
    srt.append(f"{bi + 1}\n{hms(b[0]['ini'])} --> {hms(fim_b)}\n{' '.join(p['t'] for p in b)}\n")
open(os.path.join(a.saida, "legenda_capcut.srt"), "w", encoding="utf-8").write("\n".join(srt))
print(f"faixa_legenda.mov: {len(blocos)} blocos, {len(estados)} estados karaoke, banda y={BANDA_Y} h={BANDA_H}")
print(f"fonte {FS}px ({100*FS/H:.1f}% da altura), contorno {STROKE}px, centro {100*a.centro:.0f}%")
print("amostra:", " | ".join(" ".join(p["t"] for p in b) for b in blocos[:6]))

if a.quadro:
    base = Image.open(a.quadro).convert("RGBA").resize((W, H))
    alvo = next((i for i, b in enumerate(blocos) if a.previa and a.previa in " ".join(p["t"] for p in b)), 0)
    base.alpha_composite(desenha(blocos[alvo], len(blocos[alvo]) - 1), (0, BANDA_Y))
    base.convert("RGB").save(os.path.join(a.saida, "previa_legenda.png"))
    print("previa_legenda.png gerada")
