# -*- coding: utf-8 -*-
"""Render final: corte + cor + legenda + narracao, as 2 entregas.

uso:
  python render_final.py --render <pasta do prep_shots> --narracao narracao_final.wav \
      --legenda <pasta do legenda_karaoke> --saida <pasta do job> --nome carrascal \
      [--sfx sfx.json] [--rascunho]
  --rascunho: so o com-legenda em encode rapido (<render>/rascunho.mp4) para a revisao.
  Fluxo: rascunho -> revisao -> corrige -> rascunho de novo -> ... -> SO NO FIM as 2 entregas (sem --rascunho).

sfx.json: [{"t": 1.6, "arquivo": "C:/.../Sons edição/impact-cinematic-boom-352465.mp3", "vol": 0.6}]
  (padrao: NAO passe --sfx; os SFX vao so na faixa SFX do rascunho do CapCut)
gera em <saida>/Videos prontos/ (so as entregas, nada de arquivo de trabalho):
  <nome>-com-legenda.mp4   completo: cor + legenda + narracao
  <nome>-sem-legenda.mp4   base de edicao: cor + narracao, sem legenda
NENHUMA leva logo do canal (pedido do usuario em 21/10/2026: ele refina e exporta tudo no CapCut
e deixou de usar a logo; acabaram os arquivos TIKTOK/YOUTUBE e o com-legenda-sem-marca).
e em <saida>/ (raiz do job): "legenda para o CapCut.srt" (grafia certa, para importar no CapCut)
e em <render>/: <nome>-preview.mp4 (720p)
"""
import argparse, json, os, shutil, subprocess, sys, wave
import numpy as np

BASE = os.environ.get("RADAR_BASE", r"C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo")
ap = argparse.ArgumentParser()
ap.add_argument("--render", required=True)
ap.add_argument("--narracao", required=True)
ap.add_argument("--legenda", required=True)
ap.add_argument("--saida", required=True)
ap.add_argument("--nome", required=True)
ap.add_argument("--sfx")
ap.add_argument("--lufs", type=float, default=-10.0, help="o usuario publica em -10 LUFS")
ap.add_argument("--rascunho", action="store_true",
                help="so o com-legenda, rapido (ultrafast), em <render>/rascunho.mp4, para a revisao a cada 0,1s. "
                     "As 2 entregas saem UMA vez, depois que a revisao do rascunho estiver limpa")
a = ap.parse_args()
from pasta_job import dentro_do_job
dentro_do_job(a.saida); dentro_do_job(a.render); dentro_do_job(a.legenda)
W, H, SR = 1440, 2560, 48000

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: sys.exit("ffmpeg falhou:\n" + r.stderr[-1500:])
    return r

def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", p], capture_output=True, text=True).stdout)

corte = os.path.join(a.render, "corte_completo.mp4")
# a entrega final manda o corte para a Lixeira (05/10/2026); numa correcao depois da entrega,
# ele e emendado de novo dos shots (-c copy, segundos), igual ao fim do prep_shots/posfx
if not os.path.exists(corte):
    lista_c = os.path.join(a.render, "lista_completo.txt")
    if not os.path.exists(lista_c):
        sys.exit(f"falta {corte} e {lista_c}: rode o prep_shots.py antes")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lista_c, "-c", "copy",
         "-movflags", "+faststart", corte])
    print("corte_completo.mp4 refeito a partir dos shots")
D = dur(corte)

# ---- cama de SFX montada em numpy (adelay+amix descartou efeitos com offset grande)
cama = np.zeros((int((D + 1) * SR), 2), dtype=np.float32)
if a.sfx:
    for s in json.load(open(a.sfx, encoding="utf-8")):
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", s["arquivo"], "-ac", "2", "-ar", str(SR),
                              "-f", "s16le", "-"], capture_output=True).stdout
        x = np.frombuffer(raw, dtype=np.int16).astype(np.float32).reshape(-1, 2) / 32768 * s.get("vol", 0.5)
        i = int(s["t"] * SR); n = min(len(x), len(cama) - i)
        if n > 0: cama[i:i + n] += x[:n]
        print(f"SFX {s['t']:6.2f}s  {os.path.basename(s['arquivo'])}")
pico = np.abs(cama).max()
if pico > 0.9: cama *= 0.9 / pico
cama_wav = os.path.join(a.render, "sfx_cama.wav")
with wave.open(cama_wav, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((cama * 32767).astype(np.int16).tobytes())

banda = json.load(open(os.path.join(a.legenda, "banda.json")))
faixa = os.path.join(a.legenda, "faixa_legenda.mov")
# preset medium (era slow): ~30-40% mais rapido, diferenca invisivel com crf 17 / 24M (set/2026)
ENC_V = ["-c:v", "libx264", "-crf", "17", "-preset", "medium", "-maxrate", "24M", "-bufsize", "48M",
         "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", "60"]
ENC_A = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000"]
LN = f"loudnorm=I={a.lufs}:TP=-1.5:LRA=11"

pasta_entrega = os.path.join(a.saida, "Videos prontos")
os.makedirs(pasta_entrega, exist_ok=True)
saida_l = os.path.join(pasta_entrega, f"{a.nome}-com-legenda.mp4")
saida_s = os.path.join(pasta_entrega, f"{a.nome}-sem-legenda.mp4")
ENTREGAS = [saida_l, saida_s]
# AUDIO EM PASSO SEPARADO. Com o audio no mesmo filter_complex da logo em loop e da faixa de
# legenda, o ffmpeg descartou ~9s de narracao em silencio (camisa amarela, set/2026): o arquivo
# tinha 62s, mas a fala pulava de "de um empate" para "o simbolo do maior trauma" e acabava em 53s.
audio_final = os.path.join(a.render, "audio_final.wav")
run(["ffmpeg", "-y", "-v", "error", "-i", a.narracao, "-i", cama_wav, "-filter_complex",
     f"[0:a][1:a]amix=inputs=2:normalize=0:duration=first,{LN}[a]", "-map", "[a]",
     "-ar", str(SR), "-ac", "2", "-c:a", "pcm_s16le", audio_final])
filtro = f"[0:v]eq=saturation=1.18:contrast=1.12[c];[c][1:v]overlay=0:{banda['y']}:format=auto:shortest=0[v]"
if a.rascunho:
    # mesma composicao do com-legenda final (cor + legenda + audio), encode rapido, fora de "Videos prontos"
    rasc = os.path.join(a.render, "rascunho.mp4")
    run(["ffmpeg", "-y", "-v", "error", "-i", corte, "-i", faixa, "-i", audio_final, "-filter_complex", filtro,
         "-map", "[v]", "-map", "2:a", "-c:v", "libx264", "-crf", "20", "-preset", "ultrafast", "-pix_fmt", "yuv420p",
         "-r", "60", *ENC_A, "-t", f"{D:.3f}", rasc])
    print("rascunho:", rasc, f"({dur(rasc):.2f}s, corte {D:.2f}s)")
    print("rode revisao.py nele; so depois de limpo rode render_final.py SEM --rascunho (2 arquivos, uma vez)")
    sys.exit(0)
# legenda com a grafia certa, para importar no CapCut (fica na raiz do job: "Videos prontos" so leva os videos)
srt_leg = os.path.join(a.legenda, "legenda_capcut.srt")
if os.path.exists(srt_leg):
    shutil.copyfile(srt_leg, os.path.join(a.saida, "legenda para o CapCut.srt"))
    print("ok:", os.path.join(a.saida, "legenda para o CapCut.srt"))
run(["ffmpeg", "-y", "-v", "error", "-i", corte, "-i", faixa, "-i", audio_final, "-filter_complex", filtro,
     "-map", "[v]", "-map", "2:a", *ENC_V, *ENC_A, "-t", f"{D:.3f}", "-movflags", "+faststart", saida_l])
print("ok:", saida_l)
run(["ffmpeg", "-y", "-v", "error", "-i", corte, "-i", audio_final, "-vf", "eq=saturation=1.18:contrast=1.12",
     "-map", "0:v", "-map", "1:a", *ENC_V, *ENC_A, "-t", f"{D:.3f}", "-movflags", "+faststart", saida_s])
print("ok:", saida_s)

run(["ffmpeg", "-y", "-v", "error", "-i", saida_l, "-vf", "scale=720:1280:flags=lanczos", "-c:v", "libx264",
     "-crf", "27", "-preset", "fast", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
     os.path.join(a.render, f"{a.nome}-preview.mp4")])


# guia da trilha (raiz do job): tempos de entrada/queda/subida/saida da musica, padrao das edicoes dele
_edl = os.path.join(os.path.dirname(os.path.abspath(a.render)), "edl.json")
if os.path.exists(_edl):
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "guia_trilha.py"), _edl, a.saida])

# ---- checagens objetivas
lf = run(["ffmpeg", "-i", saida_l, "-vn", "-af", "ebur128=framelog=quiet", "-f", "null", "-"]).stderr
integ = [l for l in lf.splitlines() if l.strip().startswith("I:")]
print("loudness:", integ[-1].strip() if integ else "?", f"(alvo {a.lufs} LUFS)")
for p in ENTREGAS:
    print(f"duracao {os.path.basename(p)}: {dur(p):.2f}s (corte {D:.2f}s)")

# audio de cada entrega tem que seguir a narracao do comeco ao fim (envelope por segundo).
# Duracao igual NAO prova nada: o arquivo com 9s de fala faltando tambem tinha 62s.
# ERRO (bloqueia) = fala SUMIDA: janela de 1s em que a narracao tem voz e a entrega quase nao tem.
# AVISO (nao bloqueia) = correlacao < 0,9: o limitador achata os picos da voz e derruba a
# correlacao sem faltar nada (Kane, set/2026: 4 janelas "divergentes", transcricao 100% inteira).
# Se so aparecer AVISO, confirme transcrevendo a entrega (faster-whisper) antes de entregar.
def env_arr(p):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-vn", "-ac", "1", "-ar", "8000", "-f", "s16le", "-"],
                       capture_output=True).stdout
    x = np.abs(np.frombuffer(r, dtype=np.int16).astype(np.float32))
    return x[: len(x) // 80 * 80].reshape(-1, 80).mean(1)
ref = env_arr(a.narracao); falhas = []
for nome_arq in ENTREGAS:
    e = env_arr(nome_arq); n = min(len(e), len(ref)); e, r_ = e[:n], ref[:n]
    voz = r_ > np.percentile(r_, 40)
    g = float(np.median(e[voz] / np.maximum(r_[voz], 1))) if voz.any() else 1.0
    sumida, diverge = [], []
    for s0 in range(0, n - 100, 100):
        rr, ee = r_[s0:s0 + 100], e[s0:s0 + 100] / max(g, 1e-6)
        if rr.mean() > np.percentile(r_, 50) and ee.mean() < 0.3 * rr.mean():
            sumida.append(s0 / 100)
        elif np.std(rr) > 1 and np.std(ee) > 0 and np.corrcoef(ee, rr)[0, 1] < 0.9:
            diverge.append(s0 / 100)
    msg = "OK" if not (sumida or diverge) else ""
    if sumida: msg += f"FALA SUMIDA em {sumida}s "
    if diverge: msg += f"(aviso: correlacao baixa em {diverge}s - provavel limitador; confirme transcrevendo)"
    print(f"audio x narracao {os.path.basename(nome_arq)}: {msg}")
    if sumida: falhas.append(nome_arq)

if falhas:
    sys.exit("ERRO: falta fala da narracao no audio final - nao entregue")

# ---- limpeza da entrega (pedido do usuario, 05/10/2026: cada video ocupava ~5 GB).
# So o que se refaz sozinho vai para a Lixeira: os cortes emendados (refeitos dos shots em segundos)
# e o rascunho (refeito a cada correcao). Os shots (render/completo, render/limpo), os clipes,
# a EDL e a previa ficam: correcao e remontagem continuam iguais. Clipes so saem no fechar_videos.py.
from lixeira import para_lixeira, tamanho
regen = [os.path.join(a.render, n) for n in ("corte_completo.mp4", "corte_limpo.mp4", "rascunho.mp4", "rascunho_tiktok.mp4")]
regen = [p for p in regen if os.path.exists(p)]
liberado = sum(tamanho(p) for p in regen)
movidos, falhou = para_lixeira(regen)
print(f"limpeza: {len(movidos)} arquivo(s) regeneraveis na Lixeira ({liberado / 1e9:.1f} GB)"
      + (f"; nao saiu: {falhou}" if falhou else ""))
