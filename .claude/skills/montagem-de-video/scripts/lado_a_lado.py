# -*- coding: utf-8 -*-
"""Folha lado a lado: linha de cima = nosso, linha de baixo = do usuario, mesmo tempo.
uso: python lado_a_lado.py <nosso> <dele> <saida.jpg> <t0> <t1> [passo]"""
import subprocess, sys
from PIL import Image, ImageDraw
A, B, OUT, t0, t1 = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5])
p = float(sys.argv[6]) if len(sys.argv) > 6 else 0.3
from pasta_job import dentro_do_job
dentro_do_job(OUT)
W, H = 150, 267
ts = []
t = t0
while t < t1 - 1e-6: ts.append(round(t, 2)); t += p
img = Image.new("RGB", (W * len(ts), H * 2 + 16), "black"); d = ImageDraw.Draw(img)
for i, t in enumerate(ts):
    for r, src in enumerate((A, B)):
        raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", src, "-frames:v", "1",
                              "-vf", f"scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                             capture_output=True).stdout
        if len(raw) == W * H * 3:
            img.paste(Image.frombytes("RGB", (W, H), raw), (i * W, 16 + r * H))
    d.text((i * W + 3, 2), f"{t:.1f}", fill="yellow")
img.save(OUT, quality=88)
