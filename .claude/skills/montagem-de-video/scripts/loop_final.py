# -*- coding: utf-8 -*-
"""Corta o fim da narracao para o video emendar no comeco quando repete (loop).

Recurso da montagem a mao do usuario (Faiq Bolkiah, set/2026): o roteiro termina com uma frase-ponte
que repete a abertura ("E por esse motivo que o jogador mais rico do mundo ta desempregado."), e o
video acaba cortado no comeco da palavra que emenda ("...que o J|"). Quando o video repete, a fala
continua em "o jogador mais rico do mundo...".

Roda DEPOIS de narracao.py, na pasta _montagem:
  python loop_final.py <pasta _montagem> [--palavras-abertura 3] [--sobra 0.10]

Acha, no ultimo terco da narracao, a repeticao das primeiras palavras da abertura e corta em
<inicio da 2a palavra repetida> + --sobra segundos. Atualiza narracao_final.wav, palavras.json e
pausas.json (a versao anterior fica em *_sem_loop.*). Se nao achar a repeticao, nao mexe em nada.
"""
import argparse, json, os, re, shutil, sys, unicodedata, wave
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("pasta")
ap.add_argument("--palavras-abertura", type=int, default=3, help="quantas palavras da abertura precisam repetir")
ap.add_argument("--sobra", type=float, default=0.10, help="quanto da palavra de emenda fica no fim (s)")
a = ap.parse_args()
from pasta_job import dentro_do_job
dentro_do_job(a.pasta)

def n(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(c for c in s if unicodedata.category(c) != "Mn"))

wav_p, pal_p, pau_p = (os.path.join(a.pasta, f) for f in ("narracao_final.wav", "palavras.json", "pausas.json"))
W = json.load(open(pal_p, encoding="utf-8"))
with wave.open(wav_p) as w:
    sr, ch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).reshape(-1, ch)
dur = len(x) / sr

k = a.palavras_abertura
alvo = [n(p["w"]) for p in W[:k]]
achou = None
for i in range(len(W) - k, 0, -1):
    if W[i]["ini"] < dur * 2 / 3: break
    if [n(p["w"]) for p in W[i:i + k]] == alvo:
        achou = i; break
if achou is None:
    # Ponte de CONTINUACAO (Endrick, set/2026): o fim fica em aberto e a abertura completa a frase
    # ("...so o dia em que..." -> "O Endrick levou a mao na cara"). Nao ha o que cortar.
    ult = W[-1]["w"].strip().lower()
    CONECT = {"que", "quando", "onde", "porque", "em", "de", "do", "da", "o", "a", "e", "pra", "com", "foi", "era"}
    if ult.endswith("...") or ult.endswith("…") or n(ult) in CONECT:
        print(f"loop: ponte de CONTINUACAO - a narracao termina em aberto ('...{' '.join(p['w'] for p in W[-4:])}') "
              f"e emenda na abertura ('{' '.join(p['w'] for p in W[:k])}...'). Nada cortado; faca o loop visual.")
        sys.exit(0)
    print(f"AVISO: a abertura ({' '.join(p['w'] for p in W[:k])}) nao se repete no fim da narracao e o fim nao "
          "fica em aberto - sem frase-ponte, nada foi cortado. Sugira ao usuario incluir a frase-ponte no roteiro.")
    sys.exit(0)

corte = min(W[achou + 1]["ini"] + a.sobra, dur)
for p in (wav_p, pal_p, pau_p):
    b, e = os.path.splitext(p); shutil.copy(p, f"{b}_sem_loop{e}")
y = x[:int(corte * sr)].copy()
f = int(0.008 * sr)                      # 8 ms de fade so para nao estalar; o corte continua seco
y[-f:] = (y[-f:].astype(np.float32) * np.linspace(1, 0, f)[:, None]).astype(np.int16)
with wave.open(wav_p, "wb") as w:
    w.setnchannels(ch); w.setsampwidth(sw); w.setframerate(sr); w.writeframes(y.tobytes())
# a palavra de emenda (cortada no meio) sai da legenda
W2 = [p for p in W[:achou + 1]]
json.dump(W2, open(pal_p, "w", encoding="utf-8"), indent=0, ensure_ascii=False)
P = [p for p in json.load(open(pau_p)) if p["fim"] < corte]
json.dump(P, open(pau_p, "w"), indent=0)
print(f"loop: fim cortado em {corte:.2f}s (era {dur:.2f}s), dentro de '{W[achou + 1]['w']}'; "
      f"ultima palavra na legenda: '{W2[-1]['w']}'")
