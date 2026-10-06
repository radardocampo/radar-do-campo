# -*- coding: utf-8 -*-
"""Fecha os videos ja postados: cria o "registro final" e manda o material pesado para a Lixeira.
So roda quando o usuario pede ("fecha os videos antigos"); nunca no fim da montagem, porque ate
la ele pode pedir correcao/remontagem e os clipes tem que estar no lugar (pedido de 05/10/2026).

Fecha cada <Shorts>/<video>/ que tem a pasta clipes E cujo final mais novo tem mais de --dias:
  fica na pasta: Videos prontos/, MP4 finais soltos na raiz, capa (png e pasta), Narracao*.wav,
                 ROTEIRO.txt, .srt
  _registro/   : os arquivos de trabalho pequenos da raiz (inventario, links baixados, notas...),
                 montagem/ (textos de _montagem, inclusive edl.json, cmp/ e scripts/),
                 scripts/, transcricoes/ e lista_clipes.txt (o nome traz o id da fonte: da para baixar de novo)
  Lixeira      : clipes/, _montagem/, frames/, transcricoes/ e arquivos soltos > 20 MB que nao sao finais
E refaz o indice "Shorts/Registro dos videos postados.csv" (unico arquivo que a skill grava na raiz
de Shorts, autorizado pelo usuario).

uso: python fechar_videos.py                      # so mostra o que faria (nao mexe em nada)
     python fechar_videos.py --executar           # faz
     [--dias 15] [--limite-gb 140] [--so "nome da pasta"]
--limite-gb: total maximo por rodada. A Lixeira do C: tem 150 GB; passando disso o Windows apaga
para sempre o que estiver la dentro. Peca ao usuario para esvaziar a Lixeira ANTES de rodar.
"""
import argparse, csv, json, os, re, shutil, subprocess, sys, time
from lixeira import para_lixeira, tamanho
from pasta_job import SHORTS, dentro_do_job

ap = argparse.ArgumentParser()
ap.add_argument("--dias", type=float, default=15)
ap.add_argument("--limite-gb", type=float, default=140)
ap.add_argument("--executar", action="store_true")
ap.add_argument("--so", action="append", default=[], help="fecha so esta(s) pasta(s), ignorando --dias")
a = ap.parse_args()

KEEP_DIRS = {"Videos prontos", "capa", "_registro"}
PESADAS = {"clipes", "_montagem", "frames", "transcricoes"}
TEXTO = re.compile(r"\.(json|txt|log|srt|py|csv|sh|err|md)$", re.I)
EXCLUIR_MP4 = re.compile(r"[\\/](clipes|_montagem|frames|_comparacao)[\\/]", re.I)


def eh_final(nome):
    n = nome.lower()
    return (n.endswith(".mp4") or (n.startswith("capa") and n.endswith(".png")) or
            (n.startswith("narra") and n.endswith(".wav")) or n == "roteiro.txt" or n.endswith(".srt"))


def finais(job):
    out = []
    for raiz, _, arqs in os.walk(job):
        for f in arqs:
            p = os.path.join(raiz, f)
            if f.lower().endswith(".mp4") and not EXCLUIR_MP4.search(p):
                out.append(p)
    return out


def copia_textos(src, dst):
    if not os.path.isdir(src):
        return
    txt = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f)) and TEXTO.search(f)
           and os.path.getsize(os.path.join(src, f)) <= 20e6]
    if txt:
        os.makedirs(dst, exist_ok=True)
        for f in txt:
            shutil.copy2(os.path.join(src, f), os.path.join(dst, f))


def registrar(job):
    """cria o _registro e devolve a lista do que e pesado (vai para a Lixeira)"""
    dentro_do_job(job)
    reg = os.path.join(job, "_registro")
    os.makedirs(reg, exist_ok=True)
    pesados = []
    for f in os.listdir(job):
        p = os.path.join(job, f)
        if not os.path.isfile(p) or eh_final(f):
            continue
        if os.path.getsize(p) <= 20e6:
            shutil.move(p, os.path.join(reg, f))
        else:
            pesados.append(p)
    m = os.path.join(job, "_montagem")
    copia_textos(m, os.path.join(reg, "montagem"))
    for sub in ("cmp", "scripts"):
        copia_textos(os.path.join(m, sub), os.path.join(reg, "montagem", sub))
    for sub in ("scripts", "transcricoes"):
        copia_textos(os.path.join(job, sub), os.path.join(reg, sub))
    cl = os.path.join(job, "clipes")
    with open(os.path.join(reg, "lista_clipes.txt"), "w", encoding="utf-8") as fh:
        for raiz, _, arqs in os.walk(cl):
            for f in sorted(arqs):
                p = os.path.join(raiz, f)
                fh.write(f"{os.path.getsize(p) / 1e6:10.1f} MB  {os.path.relpath(p, cl)}\n")
    pesados += [os.path.join(job, d) for d in os.listdir(job)
                if d in PESADAS and os.path.isdir(os.path.join(job, d))]
    return pesados


def duracao(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                       capture_output=True, text=True).stdout.strip()
    try: return f"{float(r):.1f}".replace(".", ",")
    except ValueError: return ""


def indice():
    linhas = []
    for nome in sorted(os.listdir(SHORTS)):
        job = os.path.join(SHORTS, nome)
        if not os.path.isdir(job):
            continue
        mp4 = finais(job)
        tem_reg = os.path.isdir(os.path.join(job, "_registro"))
        tem_cl = os.path.isdir(os.path.join(job, "clipes"))
        status = ("registrado" if tem_reg else "postado, com clipes" if tem_cl and mp4
                  else "em produção" if tem_cl else "manual (antigo)")
        tt = [p for p in mp4 if "TIKTOK" in os.path.basename(p)]
        princ = next((p for p in tt if not os.path.basename(p).startswith("video pronto")), None) or \
            (tt[0] if tt else (mp4[0] if mp4 else None))
        titulo = re.sub(r"\s*(TIKTOK|YOUTUBE)\.*$", "", os.path.splitext(os.path.basename(princ))[0]) if princ else ""
        data = time.strftime("%Y-%m-%d", time.localtime(max((os.path.getmtime(p) for p in mp4),
                                                            default=os.path.getmtime(job))))
        linhas.append({"Data": data, "Pasta": nome, "Titulo": titulo, "Duracao_s": duracao(princ) if princ else "",
                       "Status": status, "Arquivos_finais": " | ".join(os.path.relpath(p, job) for p in mp4),
                       "Tamanho_finais_MB": round(sum(os.path.getsize(p) for p in mp4) / 2**20),
                       "Roteiro": any(f.lower() == "roteiro.txt" for f in os.listdir(job)), "Registro": tem_reg})
    linhas.sort(key=lambda r: r["Data"], reverse=True)
    with open(os.path.join(SHORTS, "Registro dos vídeos postados.csv"), "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(linhas[0]), delimiter=";")
        w.writeheader(); w.writerows(linhas)
    return len(linhas)


agora = time.time()
candidatos = []
for nome in sorted(os.listdir(SHORTS)):
    job = os.path.join(SHORTS, nome)
    if not os.path.isdir(os.path.join(job, "clipes")):
        continue
    mp4 = finais(job)
    if not mp4:
        continue                                   # sem final = ainda em producao
    idade = (agora - max(os.path.getmtime(p) for p in mp4)) / 86400
    if (a.so and nome in a.so) or (not a.so and idade >= a.dias):
        candidatos.append((nome, job, idade))

total = 0
for nome, job, idade in candidatos:
    est = sum(tamanho(os.path.join(job, d)) for d in PESADAS if os.path.isdir(os.path.join(job, d)))
    if total + est > a.limite_gb * 1e9:
        print(f"PARA AQUI: o proximo passaria de {a.limite_gb:.0f} GB. Esvazie a Lixeira e rode de novo.")
        break
    total += est
    print(f"{'FECHANDO' if a.executar else 'fecharia'}  {idade:5.1f} dias  {est / 1e9:5.1f} GB  {nome}")
    if a.executar:
        movidos, falhas = para_lixeira(registrar(job))
        if falhas:
            print("   nao saiu (Defender/arquivo aberto?):", falhas)
print(f"total: {total / 1e9:.1f} GB {'na Lixeira' if a.executar else '(nada foi mexido: use --executar)'}")
if a.executar:
    print("indice atualizado:", indice(), "videos")
