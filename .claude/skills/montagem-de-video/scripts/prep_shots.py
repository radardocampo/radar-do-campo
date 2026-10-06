# -*- coding: utf-8 -*-
"""Audita a EDL e pre-processa cada shot (trim -> enquadramento -> upscale 1440x2560 60fps),
depois concatena tudo em um corte continuo. O render final so sobrepoe camadas nesse corte.

uso:
  python prep_shots.py edl.json --saida <pasta_render> [--pausas pausas.json] [--dur 60.43]
                       [--so-checar] [--shots 03,07]

edl.json:
{
  "clips": {"TORC1": "clipes/_extras/tt_xxx.mp4", "BLOQ": "clipes/parte05_...mp4"},
  "shots": [
    {"id": 1, "tStart": 0.0, "tEnd": 1.4, "clip": "CCOMP", "in": 52.5, "rate": 1.0,
     "tipo": "A", "fonte": "torcida|transmissao", "protagonista": true,
     "zoom": 1.0, "cx": 0.5, "cy": 0.5, "tracking": "fixo|mov", "nota": "por que este plano"}
  ]
}
  tStart/tEnd: tempo no video final (narracao ja acelerada)
  in: segundo do clipe-fonte onde o shot comeca; rate: 1.0 normal, 0.5 camera lenta
  zoom: 1.0 = maior janela 9:16 possivel; >1 fecha mais (use para tirar texto/logo queimado)
  cx, cy: centro da janela (fracao da largura/altura do fonte). tracking "mov" segue o movimento.
  keys: [[t, cx] | [t, cx, cy], ...] (t RELATIVO AO INICIO DO SHOT: 0 = primeiro quadro do shot)
        - a janela anda acompanhando a bola/o lance. Se vierem em tempo do video final (t >= tStart),
        o script converte sozinho e avisa (Endrick, set/2026: keys absolutas deixaram a janela parada).
  tracking "segue": acompanha o lance sozinho (fluxo optico, descontado o pan da camera). Confira.
  recorte: [x, y, larg, alt] (fracao do fonte) - tira a borda de repost (titulo, legenda do autor) antes do 9:16.
  borrar: [[t, x, y, larg, alt], ...] (fracao do quadro FINAL) - desfoca ferimento/sangue com borda suave.
  destaque: [{"tipo": "seta"|"circulo", "x", "y", "ang", "tam", "t0", "t1"}] - seta/circulo vermelho no protagonista.
            {"tipo": "icone", "arquivo": "<png>", "riscar": true, "x", "y", "tam", "t0", "t1"} - simbolo sobre a
            cabeca dele (escudo da CBF riscado = "cortado da Selecao").
  flashforward: true - o shot pode repetir quadros de outro shot: o gancho (previa do climax) e a 2a passada
                do lance-chave como replay (1a com seta, 2a limpa), Raphinha set/2026.
  ignorar_bordas: true - desliga a checagem de corte/fade SO neste shot, depois de conferir a 30fps que e alarme falso
                  (nunca use --sem-bordas no video inteiro por causa de um shot).
  "tampar" (opcional, na raiz): {"CLIPE": [[x, y, larg, alt], ...]} em fracao do fonte - apaga
  marca d'agua de outro perfil/emissora clonando textura vizinha (limpar_marcas.py), em todos
  os shots daquele clipe. Um shot pode ter seu proprio "tampar" (sobrepoe o do clipe; [] = nada).
  Onde der, prefira tirar a marca do quadro com zoom/cy.

gera: <saida>/completo/shotNN.mp4, <saida>/limpo/shotNN.mp4, corte_completo.mp4, corte_limpo.mp4
"""
import argparse, json, os, re, subprocess, sys
from collections import defaultdict
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("edl")
ap.add_argument("--saida", required=True)
ap.add_argument("--pausas")
ap.add_argument("--dur", type=float, help="duracao da narracao final")
ap.add_argument("--so-checar", action="store_true")
ap.add_argument("--shots", default="")
ap.add_argument("--sem-bordas", action="store_true", help="pula a checagem de corte/fade dentro dos shots")
a = ap.parse_args()
from pasta_job import dentro_do_job
dentro_do_job(a.saida)
W_OUT, H_OUT, FPS = 1440, 2560, 60
edl = json.load(open(a.edl, encoding="utf-8"))
base = os.path.dirname(os.path.abspath(a.edl))

def caminho(p):
    return p if os.path.isabs(p) else os.path.join(base, p)

def probe(p):
    o = subprocess.run(["ffprobe", "-v", "quiet", "-select_streams", "v", "-show_entries",
                        "stream=width,height", "-show_entries", "format=duration", "-of", "json", p],
                       capture_output=True, text=True).stdout
    j = json.loads(o)
    return j["streams"][0]["width"], j["streams"][0]["height"], float(j["format"]["duration"])

def foto_para_clipe(p):
    """Foto (clipes/fotos/*.jpg) vira um clipe parado de 12s a 30fps, para o resto do pipeline
    tratar igual a video (zoom/cx/cy/in funcionam do mesmo jeito)."""
    dst = os.path.join(base, "_fotos", os.path.splitext(os.path.basename(p))[0] + ".mp4")
    if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(p):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-framerate", "30", "-i", p, "-t", "12",
                        "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p", "-c:v", "libx264",
                        "-crf", "14", "-preset", "fast", dst], check=True)
    return dst

meta = {}
for k, p in edl["clips"].items():
    if not os.path.exists(caminho(p)):
        sys.exit(f"ERRO: clipe {k} nao existe: {p}")
    if os.path.splitext(p)[1].lower() in (".jpg", ".jpeg", ".png", ".webp"):
        edl["clips"][k] = p = foto_para_clipe(caminho(p))
    meta[k] = probe(caminho(p))

# ---------------- auditoria ----------------
S = edl["shots"]
err, avisos = [], []
mids = [p["mid"] for p in json.load(open(a.pausas))] if a.pausas else []
for i, s in enumerate(S):
    s.setdefault("rate", 1.0); s.setdefault("zoom", 1.0); s.setdefault("cx", 0.5)
    s.setdefault("cy", 0.5); s.setdefault("tracking", "fixo")
    s["dur"] = round(s["tEnd"] - s["tStart"], 4)
    if s.get("keys") and s["tStart"] > 0 and min(k[0] for k in s["keys"]) >= s["tStart"] - 0.01 and max(k[0] for k in s["keys"]) > s["dur"] + 0.05:
        s["keys"] = [[round(k[0] - s["tStart"], 3), *k[1:]] for k in s["keys"]]
        avisos.append(f"shot {s['id']}: keys estavam em tempo do video final - convertidas para tempo do shot (0 = inicio)")
    s["out"] = round(s["in"] + s["dur"] * s["rate"], 4)
    w, h, d = meta[s["clip"]]
    if s["dur"] <= 0: err.append(f"shot {s['id']}: tEnd <= tStart")
    if s["in"] < 0 or s["out"] > d - 0.02: err.append(f"shot {s['id']}: {s['in']}-{s['out']}s fora do clipe ({d:.2f}s)")
    if i and abs(s["tStart"] - S[i - 1]["tEnd"]) > 0.001: err.append(f"shot {s['id']}: buraco/sobreposicao com o anterior")
    if mids and s.get("tipo") == "A" and i and min(abs(s["tStart"] - m) for m in mids) > 0.12:
        err.append(f"shot {s['id']}: corte de conteudo em {s['tStart']}s fora de pausa da narracao")
    rw, rh = w, h
    if s.get("recorte"): rw, rh = s["recorte"][2] * w, s["recorte"][3] * h
    _cw = min(rw, rh * 9 / 16) / max(1.0, s["zoom"])
    if W_OUT / _cw > 2.6:
        avisos.append(f"shot {s['id']}: upscale {W_OUT / _cw:.1f}x ({s['clip']}) - procure o mesmo momento numa fonte onde o assunto ocupa mais pixels")
    if s["zoom"] > 1.6 and s["tracking"] == "fixo":
        avisos.append(f"shot {s['id']}: zoom {s['zoom']} com centro fixo - confira se o assunto nao sai do quadro")
# loop visual (regra do usuario): o ultimo shot termina no quadro em que o primeiro comeca, no mesmo clipe
if not edl.get("sem_loop") and (S[-1]["clip"] != S[0]["clip"] or abs(S[-1]["out"] - S[0]["in"]) > 0.02):
    err.append(f"loop visual: o ultimo shot ({S[-1]['clip']} ate {S[-1]['out']:.2f}s) nao emenda no primeiro "
               f"({S[0]['clip']} a partir de {S[0]['in']:.2f}s) - use o mesmo clipe, saida do ultimo = entrada do primeiro")
if a.dur and abs(S[-1]["tEnd"] - a.dur) > 0.2:
    err.append(f"EDL termina em {S[-1]['tEnd']}s, narracao tem {a.dur}s")
por_clip = defaultdict(list)
for s in S:
    if not s.get("flashforward"): por_clip[s["clip"]].append((s["in"], s["out"], s["id"]))
for c, ws in por_clip.items():
    ws.sort()
    for x in range(len(ws) - 1):
        if ws[x][1] > ws[x + 1][0] + 0.001:
            err.append(f"{c}: shots {ws[x][2]} e {ws[x+1][2]} repetem os mesmos frames")

# Corte de cena ou fade DENTRO do trecho de um shot: vira 1 quadro de outra cena "piscando"
# ou um quadro escuro na virada (video do Matheuzinho: o hino cortava para outra cena em 3,18s
# e o shot ia ate 3,20s; compilados com fade para preto nas pontas).
def bordas(src, ini, seg):
    import re as _re, statistics
    o = subprocess.run(["ffmpeg", "-hide_banner", "-ss", f"{ini:.3f}", "-t", f"{seg:.3f}", "-i", src, "-vf",
                        "fps=30,signalstats,metadata=print:key=lavfi.signalstats.YAVG,select='gt(scene,0.25)',showinfo",
                        "-f", "null", "-"], capture_output=True, text=True).stderr
    y = [float(v) for v in _re.findall(r"YAVG=([0-9.]+)", o)]
    cortes = [round(ini + float(v), 2) for v in _re.findall(r"\] n:\s*\d+ pts:\s*\d+ pts_time:([0-9.]+)", o)]
    med = statistics.median(y) if y else 0
    escuros = sum(1 for v in y if v < 0.6 * med)
    return cortes, escuros, (min(y) if y else 0), med
if not a.sem_bordas:
    for s in S:
        if s.get("ignorar_bordas"):  # alarme falso ja conferido a 30fps (fila, camisa 10, out/2026)
            avisos.append(f"shot {s['id']}: checagem de corte/fade desligada so neste shot (ignorar_bordas)"); continue
        cortes, escuros, mn, med = bordas(caminho(edl["clips"][s["clip"]]), s["in"], s["dur"] * s["rate"])
        if cortes: err.append(f"shot {s['id']} ({s['clip']} {s['in']:.2f}s): corte de cena da fonte em {cortes} - mude in/duracao")
        if escuros: err.append(f"shot {s['id']} ({s['clip']} {s['in']:.2f}s): {escuros} quadros escuros (fade; min {mn:.0f} vs mediana {med:.0f})")

tot = S[-1]["tEnd"]
torc = sum(s["dur"] for s in S if s.get("fonte") == "torcida")
prot = sum(s["dur"] for s in S if s.get("protagonista"))
dur_med = np.mean([s["dur"] for s in S])
print(f"{len(S)} shots em {tot:.2f}s | plano medio {dur_med:.2f}s | {60*len(S)/tot:.0f} planos/min")
print(f"torcida {100*torc/tot:.0f}% do tempo | protagonista na tela {100*prot/tot:.0f}% do tempo")
print("  referencia (montagem do usuario): ~23 planos/min, plano medio ~2,6s, maior parte torcida")
if dur_med < 1.8: avisos.append("plano medio curto demais - prefira segurar takes continuos da torcida")
for x in avisos: print("AVISO:", x)
if err:
    print("\nERROS - corrija a EDL antes de renderizar:"); [print("  -", e) for e in err]; sys.exit(1)
print("auditoria OK")
if a.so_checar:
    sys.exit(0)

# ---------------- pre-processamento ----------------
OUT_C, OUT_L, TMP = (os.path.join(a.saida, x) for x in ("completo", "limpo", "_tmp"))
for d in (OUT_C, OUT_L, TMP): os.makedirs(d, exist_ok=True)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit("ffmpeg falhou:\n" + r.stderr[-1500:])

def even(v): return int(round(v / 2.0)) * 2

def janela(w, h, zoom):
    cw = min(w, h * 9 / 16); ch = cw * 16 / 9
    if ch > h: ch = h; cw = ch * 9 / 16
    return even(min(cw / zoom, w)), even(min(ch / zoom, h))

def trajetoria(tmp, cw, w, seg):
    """centro X pelo centroide do movimento; ajuste linear, pan limitado a 15% da janela/s"""
    import cv2
    cap = cv2.VideoCapture(tmp); fps = cap.get(cv2.CAP_PROP_FPS) or 30
    passo = max(1, round(fps * 0.25)); prev = None; pts = []; n = 0
    while True:
        ok, fr = cap.read()
        if not ok: break
        if n % passo == 0:
            g = cv2.cvtColor(cv2.resize(fr, (192, 342)), cv2.COLOR_BGR2GRAY)
            if prev is not None:
                _, th = cv2.threshold(cv2.GaussianBlur(cv2.absdiff(prev, g), (9, 9), 0), 18, 255, cv2.THRESH_BINARY)
                m = cv2.moments(th)
                if m["m00"] > 500: pts.append((n / fps, m["m10"] / m["m00"] / 192 * w))
            prev = g
        n += 1
    cap.release()
    if len(pts) < 4: return None
    t = np.array([p[0] for p in pts]); x = np.array([p[1] for p in pts])
    x = np.array([np.median(x[max(0, i - 2):i + 3]) for i in range(len(x))])
    k, b = np.polyfit(t, x, 1); x0, x1 = b, k * seg + b
    vmax = 0.15 * cw * seg
    if abs(x1 - x0) > vmax:
        m = (x0 + x1) / 2; x0, x1 = m - vmax / 2 * np.sign(x1 - x0), m + vmax / 2 * np.sign(x1 - x0)
    return x0, x1

def expr_lin(k):
    """keyframes [(t, v)] -> expressao ffmpeg linear por partes em t (v constante antes/depois)."""
    k = sorted(k)
    if len(k) == 1 or all(abs(v - k[0][1]) < 1 for _, v in k):
        return f"{even(k[0][1])}"
    e = f"{k[0][1]:.1f}"
    for (t0, v0), (t1, v1) in zip(k, k[1:]):
        d = max(t1 - t0, 1e-3)
        e += f"+({(v1 - v0) / d:.3f})*clip(t-{t0:.3f}\\,0\\,{d:.3f})"
    return f"'{e}'"

def seguir(tmp, cw, w, rate, x_ini):
    """acompanha o lance: fluxo optico com o pan da camera descontado (mediana do fluxo);
    o centro vai para onde os jogadores/bola se movem em relacao ao fundo. Suavizado,
    com velocidade limitada (sem chicote). Devolve keyframes [(t_final, x_centro)]."""
    import cv2
    cap = cv2.VideoCapture(tmp); fps = cap.get(cv2.CAP_PROP_FPS) or 30
    passo = max(1, round(fps * 0.1)); prev = None; pts = []; n = 0; sw = 240
    while True:
        ok, fr = cap.read()
        if not ok: break
        if n % passo == 0:
            sh = max(2, int(fr.shape[0] * sw / fr.shape[1]))
            g = cv2.cvtColor(cv2.resize(fr, (sw, sh)), cv2.COLOR_BGR2GRAY)
            if prev is not None:
                fl = cv2.calcOpticalFlowFarneback(prev, g, None, 0.5, 3, 15, 3, 5, 1.2, 0)
                res = fl - np.median(fl.reshape(-1, 2), axis=0)
                mag = np.linalg.norm(res, axis=2)
                mag[:int(sh * 0.08)] = 0; mag[-int(sh * 0.05):] = 0
                thr = max(np.percentile(mag, 97), 0.6)
                m = np.where(mag >= thr, mag, 0)
                if m.sum() > 3:
                    xs = (m.sum(0) * np.arange(sw)).sum() / m.sum()
                    pts.append((n / fps / rate, xs / sw * w))
            prev = g
        n += 1
    cap.release()
    if len(pts) < 5: return None
    t = np.array([p[0] for p in pts]); x = np.array([p[1] for p in pts])
    x = np.array([np.median(x[max(0, i - 3):i + 4]) for i in range(len(x))])       # tira picos
    ker = np.exp(-0.5 * (np.arange(-6, 7) / 3.0) ** 2); ker /= ker.sum()             # ~0,6s de suavizacao
    xp = np.pad(x, 6, mode="edge"); x = np.convolve(xp, ker, mode="valid")
    vmax = 0.9 * cw                                                                  # no maximo 0,9 janela/s
    out = [x[0]]
    for i in range(1, len(x)):
        d = x[i] - out[-1]; lim = vmax * (t[i] - t[i - 1])
        out.append(out[-1] + max(-lim, min(lim, d)))
    ks = [(0.0, out[0])] + [(t[i], out[i]) for i in range(0, len(t), 3)] + [(t[-1] + 0.2, out[-1])]
    return ks

def desenha_destaque(d, png):
    """seta ou circulo vermelho (contorno preto) no quadro FINAL 1440x2560, como o usuario faz a mao
    no CapCut para apontar o protagonista num quadro confuso (Palermo embaixo da grade).
    d = {"tipo": "seta"|"circulo", "x": .., "y": .. (ponta da seta / centro do circulo, fracao do quadro),
         "ang": graus (de onde a seta vem; 135 = do canto superior esquerdo), "tam": fracao da largura,
         "t0": s, "t1": s}"""
    from PIL import Image, ImageDraw
    import math
    im = Image.new("RGBA", (W_OUT, H_OUT), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    x, y = d["x"] * W_OUT, d["y"] * H_OUT; tam = d.get("tam", 0.30) * W_OUT
    VERM, PRETO = (235, 20, 20, 255), (0, 0, 0, 255)
    if d.get("tipo") == "icone":
        # simbolo sobre a cabeca do protagonista (Raphinha, set/2026: escudo da CBF com X vermelho em
        # "foi cortado da Selecao", no gancho e no shot de loop). "arquivo": PNG com fundo transparente;
        # "riscar": true desenha o X vermelho por cima. x/y = centro do icone; tam = largura.
        ic = Image.open(d["arquivo"]).convert("RGBA")
        ic = ic.resize((int(tam), max(1, int(tam * ic.height / ic.width))), Image.LANCZOS)
        im.alpha_composite(ic, (int(x - ic.width / 2), int(y - ic.height / 2)))
        if d.get("riscar"):
            r, e = tam * 0.5, max(8, int(tam * 0.16))
            for (x0, y0, x1, y1) in ((x - r, y - r, x + r, y + r), (x - r, y + r, x + r, y - r)):
                dr.line([x0, y0, x1, y1], fill=PRETO, width=e + 8)
            for (x0, y0, x1, y1) in ((x - r, y - r, x + r, y + r), (x - r, y + r, x + r, y - r)):
                dr.line([x0, y0, x1, y1], fill=(225, 30, 40, 235), width=e)
        im.save(png); return
    if d.get("tipo", "seta") == "circulo":
        r = tam / 2
        for e, cor in ((int(tam * 0.09), PRETO), (int(tam * 0.06), VERM)):
            dr.ellipse([x - r, y - r * 0.8, x + r, y + r * 0.8], outline=cor, width=e)
    else:
        a = math.radians(d.get("ang", 135)); ux, uy = math.cos(a), -math.sin(a)   # direcao de onde a seta vem
        px, py = -uy, ux
        L, hw, cab, cw_ = tam, tam * 0.13, tam * 0.45, tam * 0.32
        bx, by = x + ux * cab, y + uy * cab                                          # base da cabeca
        pts = [(x, y), (bx + px * cw_, by + py * cw_), (bx + px * hw, by + py * hw),
               (x + ux * L + px * hw, y + uy * L + py * hw), (x + ux * L - px * hw, y + uy * L - py * hw),
               (bx - px * hw, by - py * hw), (bx - px * cw_, by - py * cw_)]
        dr.polygon(pts, fill=VERM, outline=PRETO, width=max(4, int(tam * 0.035)))
    im.save(png)

def tampar(tmp, clip, shot):
    """marcas d'agua de terceiros (WAMO, ge, sportv, Paramount+...): clona textura vizinha da
    propria cena por cima (limpar_marcas.py), sem o borrao do delogo. edl["tampar"] =
    {"CLIPE": [[x, y, larg, alt] | {"box": [...], "de": "esq|dir|baixo|cima"}, ...]} em fracao
    do quadro-fonte. Vale para o completo e para o limpo."""
    caixas = shot.get("tampar", edl.get("tampar", {}).get(clip))   # "tampar" no shot sobrepoe o do clipe
    if not caixas:
        return tmp
    limpo = tmp[:-4] + "_semmarca.mp4"
    run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "limpar_marcas.py"),
         tmp, limpo, json.dumps(caixas)])
    return limpo

SHARP = "unsharp=5:5:0.55:5:5:0.0"
ENC = ["-fps_mode", "cfr", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv", "-c:v", "libx264", "-g", "12", "-pix_fmt", "yuv420p",
       "-video_track_timescale", "60000", "-movflags", "+faststart", "-an"]
# aceita "01,41", "1 41" ou "1;41" (o PowerShell transforma 01,41 em array e o 01 era pulado sem aviso)
alvo = {f"{int(x):02d}" for x in re.split(r"[,; ]+", a.shots) if x.strip()}
for s in S:
    nome = f"shot{s['id']:02d}"
    if alvo and f"{s['id']:02d}" not in alvo: continue
    src = caminho(edl["clips"][s["clip"]]); w, h, _ = meta[s["clip"]]
    seg = s["dur"] * s["rate"]; tmp = os.path.join(TMP, nome + ".mp4")
    rec = s.get("recorte")   # [x, y, larg, alt] em fracao do fonte: tira borda com marca d'agua/texto do repost
    vf_rec = []
    if rec:
        rw, rh = even(rec[2] * w), even(rec[3] * h)
        vf_rec = ["-vf", f"crop={rw}:{rh}:{even(rec[0] * w)}:{even(rec[1] * h)}"]
        w, h = rw, rh
    run(["ffmpeg", "-y", "-v", "error", "-ss", f"{s['in']:.3f}", "-i", src, "-t", f"{seg:.3f}", *vf_rec,
         "-c:v", "libx264", "-crf", "14", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-an", tmp])
    tmp = tampar(tmp, s["clip"], s)
    pts = "setpts=PTS-STARTPTS," if s["rate"] == 1.0 else f"setpts=(PTS-STARTPTS)/{s['rate']},"
    cw, ch = janela(w, h, s["zoom"])
    # centro da janela ao longo do tempo (tempo do video final): "keys" manuais [[t, cx] | [t, cx, cy]]
    # ou tracking "segue" (acompanha o lance: movimento dos jogadores descontado o pan da camera)
    kx, ky = [(0.0, s["cx"] * w)], [(0.0, s["cy"] * h)]
    if s.get("keys"):
        kx = [(k[0], k[1] * w) for k in s["keys"]]
        ky = [(k[0], (k[2] if len(k) > 2 else s["cy"]) * h) for k in s["keys"]]
    elif s["tracking"] == "segue" and cw < w - 2:
        tr = seguir(tmp, cw, w, s["rate"], s["cx"] * w)
        if tr: kx = tr
    elif s["tracking"] == "mov" and cw < w - 2:
        tr = trajetoria(tmp, cw, w, seg)
        if tr: kx = [(0.0, tr[0]), (s["dur"], tr[1])]
    kx = [(t, min(max(x - cw / 2, 0), w - cw)) for t, x in kx]
    ky = [(t, min(max(y - ch / 2, 0), h - ch)) for t, y in ky]
    xexpr, yexpr = expr_lin(kx), expr_lin(ky)
    borrar = ""
    if s.get("borrar"):
        # desfoca uma area (ex.: o dedo ferido) - [[t, x, y, larg, alt], ...] em fracao do quadro FINAL
        # mascara que desvanece para FORA da caixa (centro 100% borrado, sem retangulo), caixa animada no tempo
        bk = sorted(s["borrar"])
        def lt(vals):
            e = f"{vals[0][1]:.1f}"
            for (t0, v0), (t1, v1) in zip(vals, vals[1:]):
                d = max(t1 - t0, 1e-3); e += f"+({(v1 - v0) / d:.3f})*clip(T-{t0:.3f},0,{d:.3f})"
            return e
        X0 = lt([(k[0], k[1] * W_OUT) for k in bk]); X1 = lt([(k[0], (k[1] + k[3]) * W_OUT) for k in bk])
        Y0 = lt([(k[0], k[2] * H_OUT) for k in bk]); Y1 = lt([(k[0], (k[2] + k[4]) * H_OUT) for k in bk])
        fe = 0.12 * W_OUT
        borrar = (f",split[m][n];[n]boxblur=60:6,format=yuva444p,"
                  f"geq=lum='p(X,Y)':cb='p(X,Y)':cr='p(X,Y)':"
                  f"a='255*clip(1+min(min(X-({X0}),({X1})-X),min(Y-({Y0}),({Y1})-Y))/{fe:.0f},0,1)'[bl];"
                  f"[m][bl]overlay=0:0,format=yuv420p")
    pts = "setpts=PTS-STARTPTS," if s["rate"] == 1.0 else f"setpts=(PTS-STARTPTS)/{s['rate']},"
    dest_in, dest_f = [], ""
    for k, d in enumerate(s.get("destaque", [])):
        png = os.path.join(TMP, f"{nome}_dest{k}.png"); desenha_destaque(d, png)
        dest_in += ["-loop", "1", "-framerate", str(FPS), "-i", png]
        t0, t1 = d.get("t0", 0.0), d.get("t1", s["dur"])
        dest_f += f"[d{k}];[{k + 1}:v]format=rgba[p{k}];[d{k}][p{k}]overlay=0:0:enable='between(t,{t0:.3f},{t1:.3f})':shortest=1"
    run(["ffmpeg", "-y", "-v", "error", "-i", tmp, *dest_in, "-filter_complex",
         f"[0:v]{pts}crop={cw}:{ch}:{xexpr}:{yexpr},scale={W_OUT}:{H_OUT}:flags=lanczos,setsar=1,{SHARP}{borrar}{dest_f},"
         f"fps={FPS},tpad=stop_mode=clone:stop_duration=0.25[v]", "-map", "[v]",
         "-t", f"{s['dur']:.3f}", "-crf", "15", "-preset", "medium", *ENC, os.path.join(OUT_C, nome + ".mp4")])
    borrar_l = ""
    if s.get("borrar"):
        # no limpo (letterbox) a mesma area vira a regiao correspondente do quadro inteiro: desfoca o quadro todo
        # na janela do tempo em que ha borrao seria impreciso; desfoca a caixa convertida pro letterbox
        sc = min(W_OUT / w, H_OUT / h); ox = (W_OUT - w * sc) / 2; oy = (H_OUT - h * sc) / 2
        def conv(k):
            x0 = kx[0][1] if len(kx) == 1 else np.interp(k[0], [a for a, _ in kx], [b for _, b in kx])
            y0 = ky[0][1] if len(ky) == 1 else np.interp(k[0], [a for a, _ in ky], [b for _, b in ky])
            fx = x0 + k[1] * cw; fy = y0 + k[2] * ch
            return (k[0], ox + fx * sc, oy + fy * sc, k[3] * cw * sc, k[4] * ch * sc)
        ck = [conv(k) for k in s["borrar"]]; lw = even(max(max(c[3] for c in ck), 16)); lh = even(max(max(c[4] for c in ck), 16))
        lx = expr_lin([(c[0], min(max(c[1] + c[3] / 2 - lw / 2, 0), W_OUT - lw)) for c in ck])
        ly = expr_lin([(c[0], min(max(c[2] + c[4] / 2 - lh / 2, 0), H_OUT - lh)) for c in ck])
        borrar_l = (f",split[m][n];[n]crop={lw}:{lh}:{lx}:{ly},boxblur=20:4,boxblur=15:3[bl];[m][bl]overlay=x={lx}:y={ly}")
    run(["ffmpeg", "-y", "-v", "error", "-i", tmp, "-filter_complex",
         f"[0:v]{pts}scale={W_OUT}:{H_OUT}:force_original_aspect_ratio=decrease:flags=lanczos,{SHARP},"
         f"pad={W_OUT}:{H_OUT}:(ow-iw)/2:(oh-ih)/2:black,setsar=1{borrar_l},fps={FPS},tpad=stop_mode=clone:stop_duration=0.25[v]",
         "-map", "[v]", "-t", f"{s['dur']:.3f}", "-crf", "17", "-preset", "medium", *ENC, os.path.join(OUT_L, nome + ".mp4")])
    up = W_OUT / cw
    print(f"{nome} {s['clip']:<8} {s['in']:6.2f}s +{s['dur']:.2f}s x{s['rate']} janela {cw}x{ch} upscale {up:.2f}x"
          + ("  <- MOLE (upscale > 2.2x)" if up > 2.2 else ""))

# tpad: fonte a 25/30fps cortada com -t perdia 1-2 frames por shot (0,16s em 33 shots);
# congela o ultimo quadro por ate 0,25s e o -t corta na duracao exata.
# concat sem re-encode (todos os shots tem parametros identicos).
# NAO regenerar timestamps com setpts=N/FRAME_RATE/TB aqui: isso ja derrubou 1/3 dos frames.
for modo, pasta in (("completo", OUT_C), ("limpo", OUT_L)):
    lista = os.path.join(a.saida, f"lista_{modo}.txt")
    with open(lista, "w") as f:
        for s in S: f.write(f"file '{modo}/shot{s['id']:02d}.mp4'\n")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy",
         "-movflags", "+faststart", os.path.join(a.saida, f"corte_{modo}.mp4")])
    _, _, d = probe(os.path.join(a.saida, f"corte_{modo}.mp4"))
    print(f"corte_{modo}.mp4: {d:.2f}s" + ("" if abs(d - tot) < 0.15 else f"  <- ERRO: esperado {tot:.2f}s"))
