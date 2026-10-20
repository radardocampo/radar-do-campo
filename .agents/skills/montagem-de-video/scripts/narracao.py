# -*- coding: utf-8 -*-
"""Prepara a narracao: corta as pausas entre os trechos (velocidade original), marca os
pontos de corte e transcreve com tempo por palavra. Todo o resto da montagem usa ESTA linha do tempo.

Regra do canal (set/2026): a narracao NAO e acelerada. Cada silencio >= --min-pausa vira uma
respiracao curta de --manter segundos (metade depois da fala, metade antes da proxima);
silencio do comeco e do fim sai quase inteiro. Pausas curtas dentro da frase ficam como estao.

uso:
  python narracao.py "<pasta do job>/Narração.wav" <pasta_saida> [--manter 0.12]
                     [--min-pausa=0.12] [--ruido=-30dB] [--vel 1.0] [--sem-whisper]
  valor negativo vai com "=" (--ruido=-30dB); "--ruido -30dB" da erro no argparse

gera em <pasta_saida>:
  narracao_final.wav   48 kHz estereo, com as pausas cortadas
  pausas.json          [{ini, fim, mid, dur}]  as emendas na linha do tempo nova (pontos de corte)
  palavras.json        [{w, ini, fim}]         (faster-whisper, word_timestamps)
"""
import argparse, json, os, re, subprocess, sys, wave
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("narracao")
ap.add_argument("saida")
ap.add_argument("--manter", type=float, default=0.12, help="silencio que sobra em cada pausa cortada (s)")
ap.add_argument("--vel", type=float, default=1.0, help="so mude se o usuario pedir")
ap.add_argument("--ruido", default="-30dB", help="limiar do silencedetect (use --ruido=-30dB)")
# set/2026: -35dB/0.15s achou so 2 pausas nas narracoes do Kane e do Atletico-GO; -30dB/0.12s achou 22 e 38
ap.add_argument("--min-pausa", type=float, default=0.12)
ap.add_argument("--sem-whisper", action="store_true")
a = ap.parse_args()
from pasta_job import dentro_do_job
dentro_do_job(a.saida)
os.makedirs(a.saida, exist_ok=True)
out_wav = os.path.join(a.saida, "narracao_final.wav")
SR = 48000

# 1) decodifica (e aplica velocidade, se pedida) para PCM MONO na memoria.
# Nao pedir "-ac 2" ao ffmpeg: o upmix mono->estereo dele abaixa 3 dB (0,707), e o limiar
# do silencedetect passava a valer -32 dB do original. O estereo e montado no numpy no fim.
filtro = f"atempo={a.vel}" if abs(a.vel - 1.0) > 1e-3 else "anull"
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", a.narracao, "-af", filtro, "-ar", str(SR), "-ac", "1",
                      "-f", "s16le", "-"], capture_output=True, check=True).stdout
x = np.frombuffer(raw, dtype=np.int16).reshape(-1, 1)
dur_orig = len(x) / SR

# 2) silencios no audio original
tmp = os.path.join(a.saida, "_narracao_orig.wav")
with wave.open(tmp, "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(x.tobytes())
log = subprocess.run(["ffmpeg", "-i", tmp, "-af", f"silencedetect=noise={a.ruido}:d={a.min_pausa}",
                      "-f", "null", "-"], capture_output=True, text=True).stderr
os.remove(tmp)
sil, ini = [], None
for l in log.splitlines():
    m = re.search(r"silence_start: (-?[\d.]+)", l)
    if m:
        ini = max(0.0, float(m.group(1))); continue
    m = re.search(r"silence_end: ([\d.]+)", l)
    if m and ini is not None:
        sil.append((ini, min(float(m.group(1)), dur_orig))); ini = None
if ini is not None:                      # silencio que vai ate o fim do arquivo
    sil.append((ini, dur_orig))

# 3) monta a narracao nova: fala inteira + respiracao curta no lugar de cada pausa
meio = a.manter / 2
trechos, pausas, cur = [], [], 0.0      # trechos: (ini, fim) no original que ficam
pos = 0.0                               # onde estamos no original
for s0, s1 in sil:
    borda_ini, borda_fim = s0 <= 0.02, s1 >= dur_orig - 0.02
    if borda_ini:                       # silencio de abertura: deixa so 0,05s
        pos = max(pos, s1 - 0.05); continue
    if borda_fim:                       # silencio final: deixa so 0,15s
        trechos.append((pos, min(s0 + 0.15, dur_orig))); pos = dur_orig; break
    corte_a, corte_b = s0 + meio, s1 - meio
    if corte_b <= corte_a:              # pausa ja e curta: nao mexe
        continue
    trechos.append((pos, corte_a))
    cur += corte_a - pos
    pausas.append({"ini": round(cur - meio, 3), "fim": round(cur + meio, 3), "mid": round(cur, 3),
                   "dur": round(a.manter, 3), "orig": round(s1 - s0, 3)})
    pos = corte_b
if pos < dur_orig:
    trechos.append((pos, dur_orig))

FADE = int(0.006 * SR)                  # 6 ms nas emendas para nao estalar
partes = []
for t0, t1 in trechos:
    seg = x[int(t0 * SR):int(t1 * SR)].astype(np.float32)
    if len(seg) > 2 * FADE:
        r = np.linspace(0, 1, FADE)[:, None]
        seg[:FADE] *= r; seg[-FADE:] *= r[::-1]
    partes.append(seg)
y = np.repeat(np.concatenate(partes).clip(-32768, 32767).astype(np.int16), 2, axis=1)  # mono -> L=R
with wave.open(out_wav, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(y.tobytes())
dur = len(y) / SR
print(f"narracao_final.wav: {dur:.2f}s (original {dur_orig:.2f}s, velocidade {a.vel}x, "
      f"{len(pausas)} pausas cortadas para {a.manter}s, {dur_orig - dur:.2f}s de silencio removidos)")

json.dump(pausas, open(os.path.join(a.saida, "pausas.json"), "w"), indent=0)
print(f"pausas.json: {len(pausas)} pontos de corte (limiar {a.ruido}, pausas >= {a.min_pausa}s)")
if len(pausas) < dur / 4:
    print("  AVISO: poucas pausas para a duracao - tente --ruido=-28dB ou --min-pausa=0.10")

if a.sem_whisper:
    sys.exit(0)

from faster_whisper import WhisperModel
m = WhisperModel("medium", device="cpu", compute_type="int8")
segs, _ = m.transcribe(out_wav, language="pt", word_timestamps=True, beam_size=5)
palavras = [{"w": w.word.strip(), "ini": round(w.start, 3), "fim": round(w.end, 3)}
            for s in segs for w in s.words]
json.dump(palavras, open(os.path.join(a.saida, "palavras.json"), "w", encoding="utf-8"),
          indent=0, ensure_ascii=False)
print(f"palavras.json: {len(palavras)} palavras")
