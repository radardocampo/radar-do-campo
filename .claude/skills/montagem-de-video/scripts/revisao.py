# -*- coding: utf-8 -*-
"""Revisao obrigatoria antes de qualquer entrega: um quadro a cada 0,1s do video final, em
folhas numeradas com o tempo e o shot da EDL queimados em cada miniatura. Percorra TODAS as
folhas e confira cada area do quadro (assunto, legenda, marca de terceiros,
bordas, quadro preto, flash de outro lance). Qualquer defeito: corrija a EDL, rerenderize e
rode a revisao de novo.

uso:
  python revisao.py "<job>/_montagem/render/rascunho.mp4" "<job>/_montagem/revisao"
                    [--edl "<job>/_montagem/edl.json"] [--passo 0.1] [--cols 10] [--linhas 6]
gera revisao/folha_01.jpg, folha_02.jpg... (60 quadros por folha = 6s de video)
e, com --edl, revisao/bordas_01.jpg...: cada virada de shot a 30fps (0,2s antes e depois), uma linha
por corte. O passo de 0,1s pula quadros soltos: no Endrick (set/2026) 1 quadro de outro video com
marca "BTB", uma fusao da fonte e um quadro escurecido so apareceram olhando as bordas.
"""
import argparse, json, os, subprocess
from PIL import Image, ImageDraw, ImageFont
from pasta_job import dentro_do_job, ARIAL_BD

ap = argparse.ArgumentParser()
ap.add_argument("video"); ap.add_argument("saida")
ap.add_argument("--edl")
ap.add_argument("--passo", type=float, default=0.1)
ap.add_argument("--cols", type=int, default=10)
ap.add_argument("--linhas", type=int, default=6)
ap.add_argument("--largura", type=int, default=150)
ap.add_argument("--shots", default="", help="so estes shots (ex.: 18,20), com --margem antes/depois; "
                "use na revisao depois de uma correcao, em vez de refazer as folhas do video inteiro")
ap.add_argument("--margem", type=float, default=0.5)
ap.add_argument("--sem-bordas", action="store_true", help="nao gera as folhas de bordas (viradas de shot a 30fps)")
a = ap.parse_args()
dentro_do_job(a.saida)
os.makedirs(a.saida, exist_ok=True)

shots = json.load(open(a.edl, encoding="utf-8"))["shots"] if a.edl else []
janelas = []
if a.shots:
    if not shots: raise SystemExit("--shots precisa de --edl")
    ids = {int(x) for x in __import__("re").split(r"[,; ]+", a.shots) if x.strip()}
    janelas = [(s["tStart"] - a.margem, s["tEnd"] + a.margem) for s in shots if s["id"] in ids]
    if not janelas: raise SystemExit(f"nenhum shot {sorted(ids)} na EDL")
def dentro(t):
    return not janelas or any(i <= t < f for i, f in janelas)
def shot_em(t):
    for s in shots:
        if s["tStart"] <= t < s["tEnd"]:
            return s["id"]
    return None

dur = float(subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0",
                            a.video], capture_output=True, text=True).stdout)
w_in, h_in = map(int, subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                      "stream=width,height", "-of", "csv=p=0", a.video],
                                     capture_output=True, text=True).stdout.strip().split(",")[:2])
W = a.largura; H = int(round(h_in * W / w_in / 2) * 2)
# todos os quadros de uma vez: fps=1/passo, cru em RGB pelo pipe
p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", a.video, "-vf", f"fps={1 / a.passo:.4f},scale={W}:{H}",
                      "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
fonte = ImageFont.truetype(ARIAL_BD, 13)
por_folha = a.cols * a.linhas
quadros, n, folha, usados = [], 0, 0, 0

def salvar(qs, k):
    img = Image.new("RGB", (W * a.cols, H * a.linhas), (20, 20, 20))
    for i, q in enumerate(qs):
        img.paste(q, ((i % a.cols) * W, (i // a.cols) * H))
    img.save(os.path.join(a.saida, f"folha_{k:02d}.jpg"), quality=85)

while True:
    raw = p.stdout.read(W * H * 3)
    if len(raw) < W * H * 3:
        break
    t = n * a.passo
    if not dentro(t):
        n += 1; continue
    im = Image.frombytes("RGB", (W, H), raw)
    d = ImageDraw.Draw(im)
    sid = shot_em(t)
    rot = f"{t:.1f}s" + (f" s{sid}" if sid else "")
    d.rectangle([0, 0, 8 + 7 * len(rot), 16], fill=(0, 0, 0)); d.text((3, 1), rot, fill=(255, 255, 0), font=fonte)
    # troca de shot: borda vermelha no primeiro quadro do shot novo
    if sid and n and shot_em(t - a.passo) != sid:
        d.rectangle([0, 0, W - 1, H - 1], outline=(255, 0, 0), width=3)
    quadros.append(im); n += 1; usados += 1
    if len(quadros) == por_folha:
        folha += 1; salvar(quadros, folha); quadros = []
if quadros:
    folha += 1; salvar(quadros, folha)
p.wait()
# folhas antigas de uma revisao maior nao podem ficar misturadas com as novas
k = folha + 1
while os.path.exists(os.path.join(a.saida, f"folha_{k:02d}.jpg")):
    os.remove(os.path.join(a.saida, f"folha_{k:02d}.jpg")); k += 1
alvo = f" (so shots {a.shots}, margem {a.margem}s)" if a.shots else ""
print(f"{usados} quadros de {dur:.1f}s{alvo}, passo {a.passo}s, em {folha} folhas em {a.saida}")
print("percorra TODAS as folhas antes de entregar; borda vermelha = primeiro quadro de cada shot")

# ---------- folhas de BORDAS: cada virada de shot quadro a quadro (30fps) ----------
if shots and not a.sem_bordas:
    ids = {int(x) for x in __import__("re").split(r"[,; ]+", a.shots) if x.strip()} if a.shots else None
    cortes = [(s["tEnd"], s["id"]) for s in shots[:-1]] + [(0.0, shots[0]["id"])]
    if ids: cortes = [c for c in cortes if c[1] in ids or c[1] + 1 in ids]
    cortes.sort()
    J, FPSB = 0.2, 30
    BW = 96; BH = int(round(h_in * BW / w_in / 2) * 2)
    p2 = subprocess.Popen(["ffmpeg", "-v", "error", "-i", a.video, "-vf", f"fps={FPSB},scale={BW}:{BH}",
                           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    linhas = {c: [] for c in cortes}; k = 0
    fnt = ImageFont.truetype(ARIAL_BD, 10)
    while True:
        raw = p2.stdout.read(BW * BH * 3)
        if len(raw) < BW * BH * 3: break
        t = k / FPSB; k += 1
        for c in cortes:
            if (c[0] == 0.0 and t < J) or (c[0] > 0 and c[0] - J <= t < c[0] + J) or (c[0] == 0.0 and t > dur - J):
                im = Image.frombytes("RGB", (BW, BH), raw); d = ImageDraw.Draw(im)
                rt = f"{t:.2f} s{shot_em(t) or ''}"
                d.rectangle([0, 0, 6 * len(rt) + 4, 12], fill=(0, 0, 0)); d.text((2, 0), rt, fill=(255, 255, 0), font=fnt)
                if c[0] > 0 and abs(t - c[0]) < 0.5 / FPSB or (c[0] > 0 and t >= c[0] and t - 1 / FPSB < c[0]):
                    d.rectangle([0, 0, BW - 1, BH - 1], outline=(255, 0, 0), width=2)
                linhas[c].append(im)
    p2.wait()
    POR = 8; cols = max(len(v) for v in linhas.values()) if linhas else 1; nb = 0
    ls = [linhas[c] for c in cortes if linhas[c]]
    for i in range(0, len(ls), POR):
        grp = ls[i:i + POR]
        img = Image.new("RGB", (BW * cols, BH * len(grp)), (20, 20, 20))
        for r_, row in enumerate(grp):
            for j, q in enumerate(row): img.paste(q, (j * BW, r_ * BH))
        nb += 1; img.save(os.path.join(a.saida, f"bordas_{nb:02d}.jpg"), quality=85)
    k = nb + 1
    while os.path.exists(os.path.join(a.saida, f"bordas_{k:02d}.jpg")):
        os.remove(os.path.join(a.saida, f"bordas_{k:02d}.jpg")); k += 1
    print(f"bordas: {len(ls)} viradas de shot a {FPSB}fps (+-{J}s) em {nb} folhas bordas_XX.jpg - "
          "procure 1 quadro de outra cena, fusao/fantasma, quadro escuro ou marca de terceiro; "
          "o clarao branco no 1o quadro de shot com fx 'flash' e esperado")
