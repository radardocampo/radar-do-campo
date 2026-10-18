# -*- coding: utf-8 -*-
"""Artes a partir de prints reais (Bernal x Yamal, 18/10/2026): quando a narracao cita um comentario,
um documento (sumula/acta, comunicado) ou um story, a imagem e o print de verdade.

  card      - recorta um comentario do print e vira um card arredondado com sombra (PNG com alpha),
              para entrar na EDL como destaque "icone" por cima do shot:
      python artes_print.py card <print.jpg> <x0,y0,x1,y1> <saida.png> [--largura 1100]

  documento - tela 1440x2560 com o documento no alto, o trecho que a narracao le realcado em amarelo
              (marca-texto) e, atras, um quadro do lance desfocado e escurecido; entra como clipe (foto):
      python artes_print.py documento <doc.jpg> <saida.png> --fundo "<clipe.mp4>|<seg>" | --fundo <img>
             [--realce x0,y0,x1,y1 ...] [--topo 300] [--largura 1340] [--variantes]

Caixas em pixels do print original. --variantes grava tambem <saida>_limpo.png (sem realce), para o
documento aparecer limpo e o realce entrar na palavra (corte seco, como no Bernal).
O script avisa se algum realce cair na faixa da legenda (48-60% da altura): suba o --topo.
"""
import argparse, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from pasta_job import dentro_do_job

W, H = 1440, 2560
AMARELO = np.array([250, 254, 5], np.float32) / 255

def caixa(txt): return tuple(int(float(v)) for v in txt.split(","))

def card(src, box, out, largura):
    im = Image.open(src).convert("RGB").crop(box)
    s = largura / im.width
    im = im.resize((largura, int(im.height * s)), Image.LANCZOS)
    pad = 36
    c = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
    m = Image.new("L", c.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, c.width - 1, c.height - 1], 42, fill=255)
    bg = Image.new("RGBA", c.size, (243, 243, 243, 255)); bg.paste(im, (pad, pad))
    c.paste(bg, (0, 0), m)
    sh = Image.new("RGBA", (c.width + 60, c.height + 60), (0, 0, 0, 0))
    sm = Image.new("L", sh.size, 0); ImageDraw.Draw(sm).rounded_rectangle([30, 36, 30 + c.width, 36 + c.height], 42, fill=150)
    sh.putalpha(sm.filter(ImageFilter.GaussianBlur(18)))
    sh.alpha_composite(c, (30, 30)); sh.save(out)
    print(out, sh.size, "-> EDL: destaque tipo icone, tam ~0,8-0,9 da largura")

def fundo_de(spec):
    if "|" in spec:
        clip, t = spec.rsplit("|", 1)
        raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", t, "-i", clip, "-frames:v", "1", "-f", "image2pipe",
                              "-vcodec", "png", "-"], capture_output=True).stdout
        import io
        f = Image.open(io.BytesIO(raw)).convert("RGB")
    else:
        f = Image.open(spec).convert("RGB")
    fw = int(f.height * W / H)
    if fw <= f.width: f = f.crop(((f.width - fw) // 2, 0, (f.width + fw) // 2, f.height))
    f = f.resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(28))
    return Image.blend(f, Image.new("RGB", (W, H), (0, 0, 0)), 0.55)

def documento(src, out, fundo, realces, topo, largura, variantes):
    doc = Image.open(src).convert("RGB")
    s = largura / doc.width
    def gera(caixas, destino):
        a = np.asarray(doc).astype(np.float32)
        for x0, y0, x1, y1 in caixas: a[y0:y1, x0:x1] *= AMARELO
        img = Image.fromarray(a.clip(0, 255).astype(np.uint8)).resize((largura, int(doc.height * s)), Image.LANCZOS)
        m = Image.new("L", img.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, img.width - 1, img.height - 1], 36, fill=255)
        o = fundo.copy(); o.paste(img, ((W - img.width) // 2, topo), m); o.save(destino)
    gera(realces, out)
    if variantes: gera([], os.path.splitext(out)[0] + "_limpo.png")
    for x0, y0, x1, y1 in realces:
        a, b = (topo + y0 * s) / H, (topo + y1 * s) / H
        aviso = "  <- CAI NA LEGENDA (48-60%, com zoom 1,0 no shot): suba --topo ou suba com cy/zoom na EDL" if a < 0.60 and b > 0.48 else ""
        print(f"realce {x0},{y0},{x1},{y1}: {a:.3f}-{b:.3f} da altura{aviso}")
    if topo + doc.height * s > H: print("aviso: o documento passa do fim da tela; reduza --largura ou recorte o print")
    print(out)

ap = argparse.ArgumentParser()
sub = ap.add_subparsers(dest="modo", required=True)
c = sub.add_parser("card"); c.add_argument("print"); c.add_argument("caixa"); c.add_argument("saida"); c.add_argument("--largura", type=int, default=1100)
d = sub.add_parser("documento"); d.add_argument("doc"); d.add_argument("saida"); d.add_argument("--fundo", required=True)
d.add_argument("--realce", nargs="*", default=[]); d.add_argument("--topo", type=int, default=300)
d.add_argument("--largura", type=int, default=1340); d.add_argument("--variantes", action="store_true")
a = ap.parse_args()
dentro_do_job(a.saida)
if a.modo == "card": card(a.print, caixa(a.caixa), a.saida, a.largura)
else: documento(a.doc, a.saida, fundo_de(a.fundo), [caixa(x) for x in a.realce], a.topo, a.largura, a.variantes)
