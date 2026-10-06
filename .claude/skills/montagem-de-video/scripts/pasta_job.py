# -*- coding: utf-8 -*-
"""Trava de pasta: os scripts do canal so gravam dentro da pasta do video,
em Videos prontos\\Shorts\\<nome do video>\\. Logos, sons, musicas, HUB, a raiz de
Videos prontos e a propria Shorts sao so leitura.

uso: from pasta_job import dentro_do_job
     dentro_do_job(caminho)            # arquivo ou pasta que o script vai gravar
"""
import os, sys

SHORTS = os.path.join(os.environ.get("RADAR_BASE", r"C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo"), "Videos prontos", "Shorts")


def dentro_do_job(caminho):
    raiz = os.path.normcase(os.path.abspath(SHORTS))
    alvo = os.path.normcase(os.path.abspath(caminho))
    rel = os.path.relpath(alvo, raiz)
    partes = [p for p in rel.split(os.sep) if p not in ("", ".")]
    # precisa estar abaixo de Shorts e dentro de uma subpasta de video (nunca solto em Shorts)
    if rel.startswith("..") or os.path.isabs(rel) or len(partes) < 1 or (len(partes) == 1 and os.path.splitext(partes[0])[1]):
        sys.exit(f"ERRO: '{caminho}' fica fora da pasta do video.\n"
                 f"Esta skill so grava em {SHORTS}\\<nome do video>\\...")
    return caminho

# fontes: Arial no Windows, Liberation Sans (mesmas medidas) na nuvem
_WIN = os.path.exists("C:/Windows/Fonts/arial.ttf")
ARIAL = "C:/Windows/Fonts/arial.ttf" if _WIN else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
ARIAL_BD = "C:/Windows/Fonts/arialbd.ttf" if _WIN else "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"