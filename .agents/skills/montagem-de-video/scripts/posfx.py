# -*- coding: utf-8 -*-
"""Transicoes pedidas pelo usuario (Ronaldo/Oslo, 28/09/2026), aplicadas depois do prep_shots:
  fx "flash"        : clarao branco (~0,13s) + soco de zoom 1,14x -> 1x (0,33s) no inicio do shot
  fx "flashback_in" : clarao + zoom + grade de arquivo (P&B quente, granulado, vinheta)
  fx "flashback"    : so a grade de arquivo
Regrava completo/shotNN.mp4 e limpo/shotNN.mp4 com os mesmos parametros e refaz os cortes (-c copy).
uso: python posfx.py edl.json --saida render   (sempre depois do prep_shots; pode rodar de novo
     a qualquer momento: shot rerenderizado e detectado e o fx e reaplicado sobre a versao nova)"""
import argparse, json, os, shutil, subprocess, sys
ap = argparse.ArgumentParser(); ap.add_argument("edl"); ap.add_argument("--saida", required=True)
a = ap.parse_args()
from pasta_job import dentro_do_job
dentro_do_job(a.saida)
ENC = ["-fps_mode", "cfr", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
       "-c:v", "libx264", "-g", "12", "-pix_fmt", "yuv420p", "-video_track_timescale", "60000", "-movflags", "+faststart", "-an"]
PUNCH = ("zoompan=z='if(lte(on,20),1+0.14*pow(1-on/20,2),1)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
         ":d=1:s=1440x2560:fps=60")
FLASH = "eq=brightness='0.9*max(0,1-t/0.13)':saturation='1-0.8*max(0,1-t/0.13)':eval=frame"
ARQ = ("hue=s=0.12,colorchannelmixer=rr=1.07:gg=0.99:bb=0.84,eq=contrast=1.12,"
       "noise=alls=16:allf=t+u,vignette=angle=PI/4.2")
FX = {"flash": f"{PUNCH},{FLASH}", "flashback_in": f"{ARQ},{PUNCH},{FLASH}", "flashback": ARQ}
edl = json.load(open(a.edl, encoding="utf-8"))
for s in edl["shots"]:
    fx = s.get("fx")
    if not fx: continue
    for modo, crf, pre in (("completo", "15", "medium"), ("limpo", "17", "medium")):
        f = os.path.join(a.saida, modo, f"shot{s['id']:02d}.mp4")
        orig = f[:-4] + "_semfx.mp4"
        marca = f[:-4] + "_fx.txt"
        # shot rerenderizado pelo prep_shots depois do ultimo posfx: o _semfx antigo ficou velho
        feito = open(marca).read().strip() if os.path.exists(marca) else ""
        if not os.path.exists(orig) or feito != f"{os.path.getmtime(f):.3f}":
            shutil.copy(f, orig)
        r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", orig, "-vf", FX[fx] + ",setsar=1,format=yuv420p",
                            "-t", f"{s['tEnd'] - s['tStart']:.3f}", "-crf", crf, "-preset", pre, *ENC, f],
                           capture_output=True, text=True)
        if r.returncode: sys.exit(r.stderr[-1500:])
        open(marca, "w").write(f"{os.path.getmtime(f):.3f}")
    print(f"shot{s['id']:02d}: {fx}")
for modo in ("completo", "limpo"):
    lista = os.path.join(a.saida, f"lista_{modo}.txt")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy",
                    "-movflags", "+faststart", os.path.join(a.saida, f"corte_{modo}.mp4")], check=True)
    d = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0",
                        os.path.join(a.saida, f"corte_{modo}.mp4")], capture_output=True, text=True).stdout.strip()
    print(f"corte_{modo}.mp4: {d}s")
