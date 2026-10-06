# -*- coding: utf-8 -*-
"""Guia da trilha: os tempos em que o usuario poe a musica no CapCut, calculados pela EDL deste video.
Padrao medido nas edicoes dele (Ronaldo/Arrascaeta, Vini, camisa 10 em out/2026):
  - entra ~1s depois do inicio (o 1o segundo e so voz), ~17 dB abaixo da voz
  - abaixa/some ~4s antes da revelacao
  - batida/impacto em cada transicao do canal (fx flash / flashback_in)
  - sobe em degrau ~3s depois da revelacao para ~11-12 dB abaixo da voz
  - sai ~2s antes do fim (o loop fica so com a voz)
  - Modric e Endrick (comparados em 02/out/2026, mesma faixa nos dois): tres degraus, -18 dB ate ~53% do video,
    queda curta (~1s) e sobe para ~-12 dB; em ~83% sobe de novo para ~-9 dB
Revelacao = shot com "revelacao": true na EDL; sem marca, o 1o shot com fx "flash" depois de 40% do video.
uso: python guia_trilha.py edl.json <pasta do job>    -> grava "<job>/guia da trilha.txt"
"""
import json, os, sys
from pasta_job import dentro_do_job
edl = json.load(open(sys.argv[1], encoding="utf-8")); job = sys.argv[2]
saida = os.path.join(job, "guia da trilha.txt"); dentro_do_job(saida)
S = edl["shots"]; D = S[-1]["tEnd"]
rev = next((s for s in S if s.get("revelacao")), None) or \
      next((s for s in S if s.get("fx") == "flash" and s["tStart"] > 0.4 * D), None)
fx = [s["tStart"] for s in S if s.get("fx") in ("flash", "flashback_in") and s["tStart"] > 0.5]
def mmss(t): return f"{int(t // 60)}:{t % 60:05.2f}"
L = ["GUIA DA TRILHA (padrao das suas edicoes; ajuste o que quiser no CapCut)", "",
     f"{mmss(1.0)}  musica entra, ~17 dB abaixo da voz"]
if rev:
    r = rev["tStart"]
    L += [f"{mmss(max(1.5, r - 4))}  abaixa/some (suspense antes da revelacao)",
          f"{mmss(r)}  revelacao: batida/impacto e musica volta",
          f"{mmss(min(D - 3, max(r + 3, D * 0.83)))}  sobe para ~9 dB abaixo da voz (degrau final)"]
L += [f"{mmss(D * 0.53)}  queda curta (~1s) e sobe para ~12 dB abaixo da voz (degrau do meio)"]
if not rev:
    L.append(f"{mmss(D * 0.83)}  sobe para ~9 dB abaixo da voz (degrau final)")
for t in fx:
    if not rev or abs(t - rev["tStart"]) > 0.3:
        L.append(f"{mmss(t)}  batida/impacto na transicao")
L += [f"{mmss(D - 2.3)}  musica sai (loop so com voz)", f"{mmss(D)}  fim"]
L = L[:3] + sorted(L[3:-1]) + L[-1:]
open(saida, "w", encoding="utf-8").write("\n".join(L) + "\n")
print("ok:", saida); print("\n".join(L))
