"""Transcreve o audio de um video/wav com tempo por palavra, SEM cortar nada
(a linha do tempo e a do arquivo). Roda no PC: a nuvem nao baixa o modelo do Whisper.

  python ferramentas/tempos_audio.py "<video ou wav>" "<saida/palavras.json>"
gera palavras.json [{w, ini, fim}] e, ao lado, frases.srt
"""
import json, os, subprocess, sys, tempfile
from faster_whisper import WhisperModel

src, out = sys.argv[1], sys.argv[2]
os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
wav = os.path.join(tempfile.gettempdir(), "tempos_audio.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
modelo = WhisperModel("medium", device="cpu", compute_type="int8")
segs, _ = modelo.transcribe(wav, language="pt", word_timestamps=True, vad_filter=False)
palavras, srt = [], []


def ts(t):
    return f"{int(t // 3600):02d}:{int(t % 3600 // 60):02d}:{int(t % 60):02d},{int(t * 1000 % 1000):03d}"


for i, s in enumerate(segs, 1):
    palavras += [{"w": p.word.strip(), "ini": round(p.start, 3), "fim": round(p.end, 3)} for p in s.words]
    srt.append(f"{i}\n{ts(s.start)} --> {ts(s.end)}\n{s.text.strip()}\n")
    print(f"{s.start:6.2f}-{s.end:6.2f} {s.text.strip()}")
json.dump(palavras, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(os.path.join(os.path.dirname(out), "frases.srt"), "w", encoding="utf-8").write("\n".join(srt))
os.remove(wav)
