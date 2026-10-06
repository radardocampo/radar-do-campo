# -*- coding: utf-8 -*-
"""Compara a entrega automatica (use a versao que ele usou de base: normalmente o
<apelido>-completo-sem-legenda.mp4) com a versao que o usuario refinou no editor (mesma duracao).
Aponta, a cada 0,1s, onde a imagem mudou (diferenca media em miniatura cinza) e,
a cada 0,5s, onde o audio mudou (energia de banda e residuo depois de alinhar ganho).
uso: python compara_edicao.py <nosso.mp4> <dele.mp4> <saida_prefixo>
"""
import subprocess, sys, json
import numpy as np

A, B, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
from pasta_job import dentro_do_job
dentro_do_job(OUT + ".json")

def thumbs(p):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-vf", "fps=10,scale=72:128,format=gray",
                          "-f", "rawvideo", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, 128, 72).astype(np.float32)

def audio(p):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                         capture_output=True).stdout
    return np.frombuffer(raw, np.float32)

ta, tb = thumbs(A), thumbs(B)
n = min(len(ta), len(tb))
d = np.abs(ta[:n] - tb[:n]).mean(axis=(1, 2))
# regioes da tela: topo 0-25%, meio 25-75%, baixo 75-100%
reg = {}
for nome, (y0, y1) in {"topo": (0, 32), "meio": (32, 96), "baixo": (96, 128)}.items():
    reg[nome] = np.abs(ta[:n, y0:y1] - tb[:n, y0:y1]).mean(axis=(1, 2))
seg = []
ini = None
for i, v in enumerate(d):
    if v > 6 and ini is None: ini = i
    if (v <= 6 or i == n - 1) and ini is not None:
        j = i if v <= 6 else i + 1
        if j - ini >= 2:
            r = {k: round(float(reg[k][ini:j].mean()), 1) for k in reg}
            seg.append({"t0": ini / 10, "t1": j / 10, "dif": round(float(d[ini:j].mean()), 1), "regiao": r})
        ini = None
aa, ab = audio(A), audio(B)
m = min(len(aa), len(ab)); aa, ab = aa[:m], ab[:m]
W = 8000
res = []
for k in range(0, m - W, W):
    x, y = aa[k:k + W], ab[k:k + W]
    g = float(np.dot(x, y) / (np.dot(x, x) + 1e-9))
    r = y - g * x
    rdb = 10 * np.log10((r ** 2).mean() + 1e-12) - 10 * np.log10((y ** 2).mean() + 1e-12)
    res.append((k / 16000, round(g, 2), round(float(rdb), 1)))
json.dump({"video": seg, "audio": res}, open(OUT + ".json", "w"), indent=0)
print("VIDEO: trechos com imagem diferente (dif>6)")
for s in seg: print(f"  {s['t0']:5.1f}-{s['t1']:5.1f}s dif {s['dif']:5.1f}  {s['regiao']}")
print("AUDIO: janelas 0,5s onde o dele tem som que o nosso nao tem (residuo > -12 dB)")
print("  ", [(t, g, r) for t, g, r in res if r > -12])
print("ganho medio dele/nosso:", round(float(np.median([g for _, g, _ in res])), 2))
