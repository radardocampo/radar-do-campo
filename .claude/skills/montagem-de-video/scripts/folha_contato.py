# -*- coding: utf-8 -*-
"""Folha de contato com o tempo queimado em cada miniatura. Serve para achar as
janelas limpas de um clipe (garimpo) e os pontos de entrada exatos (montagem).

uso:
  python folha_contato.py <video> <saida.jpg> [--passo 1.0] [--ini 0] [--fim <s>]
                          [--cols 6] [--largura 240]
Para um clipe longo, use --passo 2 ou 3 no clipe inteiro; depois --passo 0.25 no trecho critico.
"""
import argparse, math, subprocess

ap = argparse.ArgumentParser()
ap.add_argument("video"); ap.add_argument("saida")
ap.add_argument("--passo", type=float, default=1.0)
ap.add_argument("--ini", type=float, default=0.0)
ap.add_argument("--fim", type=float)
ap.add_argument("--cols", type=int, default=6)
ap.add_argument("--largura", type=int, default=240)
a = ap.parse_args()
from pasta_job import dentro_do_job, ARIAL
dentro_do_job(a.saida)

dur = float(subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0",
                            a.video], capture_output=True, text=True).stdout)
fim = min(a.fim or dur, dur)
n = max(1, int((fim - a.ini) / a.passo))
linhas = math.ceil(n / a.cols)
# no Windows o drawtext precisa de fontfile explicito (fontconfig nao esta configurado)
fonte = "fontfile='" + ARIAL.replace(":", "\\:") + "':"
t0, p = a.ini, a.passo
rotulo = (f"text='%{{eif\\:trunc({t0}+n*{p})\\:d}}.%{{eif\\:(({t0}+n*{p})-trunc({t0}+n*{p}))*10\\:d\\:1}}s'")
vf = (f"fps={1/p:.5f},scale={a.largura}:-2,drawtext={fonte}fontcolor=yellow:fontsize={a.largura//10}:"
      f"box=1:boxcolor=black@0.75:x=4:y=4:{rotulo},tile={a.cols}x{linhas}")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", str(a.ini), "-to", str(fim), "-i", a.video,
                "-vf", vf, "-frames:v", "1", "-q:v", "3", a.saida], check=True)
print(f"{a.saida}: {n} quadros de {a.ini:.1f}s a {fim:.1f}s (passo {p}s)")
