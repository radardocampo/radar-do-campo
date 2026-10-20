# -*- coding: utf-8 -*-
"""Quadros lado a lado com grade de 10% (ciano) para medir enquadramento, zoom/cx/cy, recorte e
onde fica cada marca d'agua ANTES de escrever a EDL (set/2026: logo ITV, 'diariodegoias.com.br'
no rodape, assinatura @perfil e card de post no inicio do clipe escaparam do enquadramento).

uso: python grade.py <saida.jpg> "<clipe>|<segundo>|<rotulo>" ["<clipe>|<segundo>|<rotulo>" ...]
     (rotulo opcional; separador e a barra vertical)
Meca tambem o INICIO do clipe (0-5s): repost de emissora costuma ter card de texto ali, e o
shot de loop - que volta alguns segundos antes da entrada do primeiro - cai nele.
"""
import sys, subprocess, io
from PIL import Image, ImageDraw, ImageFont
from pasta_job import dentro_do_job, ARIAL_BD
out=sys.argv[1]; dentro_do_job(out)
font=ImageFont.truetype(ARIAL_BD,18); H=520; ims=[]
for arg in sys.argv[2:]:
    f,t,*lab=arg.split("|")
    png=subprocess.run(["ffmpeg","-v","error","-ss",t,"-i",f,"-frames:v","1","-vf",f"scale=-2:{H}","-f","image2pipe","-vcodec","png","-"],capture_output=True).stdout
    im=Image.open(io.BytesIO(png)).convert("RGB"); d=ImageDraw.Draw(im); w,h=im.size
    for k in range(1,10):
        d.line([(w*k/10,0),(w*k/10,h)],fill=(0,255,255),width=1); d.line([(0,h*k/10),(w,h*k/10)],fill=(0,255,255),width=1)
    d.rectangle([0,0,w,22],fill="black"); d.text((3,1),(lab[0] if lab else "")+f" {t}s",fill="yellow",font=font); ims.append(im)
W=sum(i.width for i in ims)+4*len(ims); o=Image.new("RGB",(W,H),"gray"); x=0
for i in ims: o.paste(i,(x,0)); x+=i.width+4
o.save(out,quality=85)
