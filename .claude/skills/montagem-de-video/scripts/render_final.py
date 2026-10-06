# -*- coding: utf-8 -*-
"""Render final: corte + cor + marca d'agua + legenda + narracao + SFX, e as outras versoes.

uso:
  python render_final.py --render <pasta do prep_shots> --narracao narracao_final.wav \
      --legenda <pasta do legenda_karaoke> --saida <pasta do job> --nome carrascal \
      [--sfx sfx.json] [--sem-legsemmarca] [--rascunho]
  --rascunho: so o TIKTOK em encode rapido (<render>/rascunho_tiktok.mp4) para a revisao.
  Fluxo: rascunho -> revisao -> corrige -> rascunho de novo -> ... -> SO NO FIM os 4 arquivos (sem --rascunho).

sfx.json: [{"t": 1.6, "arquivo": "C:/.../Sons edição/impact-cinematic-boom-352465.mp3", "vol": 0.6}]
gera em <saida>/Videos prontos/ (so as entregas, nada de arquivo de trabalho):
  video pronto para o TIKTOK.mp4    completo (cor + legenda + narracao + SFX) com a marca da lupa
  video pronto para o YOUTUBE.mp4   o mesmo completo, com a marca horizontal "Radar Do Campo" no topo direito
  <nome>-completo-sem-legenda.mp4   base de edicao: 9:16 cheio, cor + narracao, SEM legenda e SEM marca
  <nome>-com-legenda-sem-marca.mp4  o completo (cor + legenda + narracao + SFX) SEM marca d'agua do canal
                                    (troca pedida em 01/10/2026: substituiu o antigo <nome>-limpo.mp4)
Marcas diferentes por rede para o TikTok e o YouTube nao cruzarem os arquivos (pedido do usuario).
O sem-legenda NAO leva marca: o usuario edita a partir dele, e com a lupa gravada ela vazou para
metade da versao dele do YouTube (Faiq Bolkiah, set/2026).
e em <saida>/ (raiz do job): "legenda para o CapCut.srt" (grafia certa, para importar no CapCut)
e em <render>/: <nome>-preview.mp4 (720p) e _checagem_marca.png
"""
import argparse, json, os, shutil, subprocess, sys, wave
import numpy as np
from PIL import Image

BASE = os.environ.get("RADAR_BASE", r"C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo")
ap = argparse.ArgumentParser()
ap.add_argument("--render", required=True)
ap.add_argument("--narracao", required=True)
ap.add_argument("--legenda", required=True)
ap.add_argument("--saida", required=True)
ap.add_argument("--nome", required=True)
ap.add_argument("--sfx")
ap.add_argument("--logo", default=os.path.join(BASE, "logos", "Logo sem fundo maior.png"),
                help="marca do TikTok (lupa)")
ap.add_argument("--logo-youtube", default=os.path.join(BASE, "logos", "Radar_do_Campo branco sem fundo.png"),
                help="marca do YouTube (horizontal, lupa + texto)")
ap.add_argument("--opacidade", type=float, default=0.20)
ap.add_argument("--lufs", type=float, default=-10.0, help="o usuario publica em -10 LUFS")
ap.add_argument("--sem-legsemmarca", action="store_true", help="nao gera o com-legenda-sem-marca")
ap.add_argument("--rascunho", action="store_true",
                help="so o TIKTOK, rapido (ultrafast), em <render>/rascunho_tiktok.mp4, para a revisao a cada 0,1s. "
                     "Os 4 arquivos finais saem UMA vez, depois que a revisao do rascunho estiver limpa")
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

# ---- marca d'agua, opacidade 0,20. Posicoes medidas nas montagens do usuario:
# TikTok: lupa com 17% da largura, centralizada, centro a 86,5% da altura.
# YouTube: logo horizontal "Radar Do Campo" com 28% da largura, canto superior direito
#          (centro em 80% da largura e 9,7% da altura), discreta como a que ele usa.
# A logo e recortada no bbox do alpha antes (a horizontal tem ~60% de borda transparente).
# alpha_composite, NAO paste(logo, pos, logo): o paste com mascara aplica o alpha duas vezes
# e a logo fica praticamente invisivel (aconteceu: opacidade efetiva ~0,03).
def faz_marca(arquivo, largura, nome_png, cx=0.5, cy=0.865):
    logo = Image.open(arquivo).convert("RGBA")
    logo = logo.crop(logo.split()[3].getbbox())
    lw = round(W * largura); lh = round(logo.height * lw / logo.width)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    arr = np.array(logo); arr[..., 3] = (arr[..., 3].astype(float) * a.opacidade).astype(np.uint8)
    marca = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    marca.alpha_composite(Image.fromarray(arr), (round(W * cx - lw / 2), round(H * cy - lh / 2)))
    png = os.path.join(a.render, nome_png); marca.save(png)
    amax = int(np.array(marca)[..., 3].max())
    if amax < 255 * a.opacidade * 0.8:
        sys.exit(f"{nome_png} com alpha maximo {amax} - a logo vai sumir no video")
    return png
marca_png = faz_marca(a.logo, 0.17, "marca.png")
marca_yt_png = faz_marca(a.logo_youtube, 0.28, "marca_youtube.png", cx=0.80, cy=0.097)

# PNG da marca entra em loop a 60fps: como imagem unica, o overlay perdia a marca
# depois dos ~10s (camisa amarela, set/2026) e a checagem mostrava recorte vazio.
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
saida_c = os.path.join(pasta_entrega, "video pronto para o TIKTOK.mp4")
saida_y = os.path.join(pasta_entrega, "video pronto para o YOUTUBE.mp4")
saida_s = os.path.join(pasta_entrega, f"{a.nome}-completo-sem-legenda.mp4")
saida_l = os.path.join(pasta_entrega, f"{a.nome}-com-legenda-sem-marca.mp4")
# AUDIO EM PASSO SEPARADO. Com o audio no mesmo filter_complex da logo em loop e da faixa de
# legenda, o ffmpeg descartou ~9s de narracao em silencio (camisa amarela, set/2026): o arquivo
# tinha 62s, mas a fala pulava de "de um empate" para "o simbolo do maior trauma" e acabava em 53s.
audio_final = os.path.join(a.render, "audio_final.wav")
run(["ffmpeg", "-y", "-v", "error", "-i", a.narracao, "-i", cama_wav, "-filter_complex",
     f"[0:a][1:a]amix=inputs=2:normalize=0:duration=first,{LN}[a]", "-map", "[a]",
     "-ar", str(SR), "-ac", "2", "-c:a", "pcm_s16le", audio_final])
filtro = (f"[0:v]eq=saturation=1.18:contrast=1.12[c];[c][1:v]overlay=0:0:format=auto:shortest=1[m];"
          f"[m][2:v]overlay=0:{banda['y']}:format=auto:shortest=0[v]")
if a.rascunho:
    # mesma composicao do TIKTOK final (cor + lupa + legenda + audio), encode rapido, fora de "Videos prontos"
    rasc = os.path.join(a.render, "rascunho_tiktok.mp4")
    run(["ffmpeg", "-y", "-v", "error", "-i", corte, "-loop", "1", "-framerate", "60", "-i", marca_png, "-i", faixa,
         "-i", audio_final, "-filter_complex", filtro, "-map", "[v]", "-map", "3:a",
         "-c:v", "libx264", "-crf", "20", "-preset", "ultrafast", "-pix_fmt", "yuv420p", "-r", "60", *ENC_A,
         "-t", f"{D:.3f}", rasc])
    print("rascunho:", rasc, f"({dur(rasc):.2f}s, corte {D:.2f}s)")
    print("rode revisao.py nele; so depois de limpo rode render_final.py SEM --rascunho (4 arquivos, uma vez)")
    sys.exit(0)
# legenda com a grafia certa, para importar no CapCut (fica na raiz do job: "Videos prontos" so leva os 4 videos)
srt_leg = os.path.join(a.legenda, "legenda_capcut.srt")
if os.path.exists(srt_leg):
    shutil.copyfile(srt_leg, os.path.join(a.saida, "legenda para o CapCut.srt"))
    print("ok:", os.path.join(a.saida, "legenda para o CapCut.srt"))
for png, destino in ((marca_png, saida_c), (marca_yt_png, saida_y)):
    run(["ffmpeg", "-y", "-v", "error", "-i", corte, "-loop", "1", "-framerate", "60", "-i", png, "-i", faixa,
         "-i", audio_final, "-filter_complex", filtro, "-map", "[v]", "-map", "3:a", *ENC_V, *ENC_A,
         "-t", f"{D:.3f}", "-movflags", "+faststart", destino])
    print("ok:", destino)

# sem legenda = base de edicao do usuario: mesma cor, SEM legenda e SEM marca d'agua
run(["ffmpeg", "-y", "-v", "error", "-i", corte, "-i", audio_final, "-vf", "eq=saturation=1.18:contrast=1.12",
     "-map", "0:v", "-map", "1:a", *ENC_V, *ENC_A, "-t", f"{D:.3f}", "-movflags", "+faststart", saida_s])
print("ok:", saida_s)

# com legenda e SEM marca d'agua (pedido do usuario em 01/10/2026, no lugar do antigo "limpo"):
# mesma cor e mesma faixa de legenda do TIKTOK, sem a lupa e sem o "Radar Do Campo"
if not a.sem_legsemmarca:
    run(["ffmpeg", "-y", "-v", "error", "-i", corte, "-i", faixa, "-i", audio_final, "-filter_complex",
         f"[0:v]eq=saturation=1.18:contrast=1.12[c];[c][1:v]overlay=0:{banda['y']}:format=auto:shortest=0[v]",
         "-map", "[v]", "-map", "2:a", *ENC_V, *ENC_A, "-t", f"{D:.3f}", "-movflags", "+faststart", saida_l])
    print("ok:", saida_l)

run(["ffmpeg", "-y", "-v", "error", "-i", saida_c, "-vf", "scale=720:1280:flags=lanczos", "-c:v", "libx264",
     "-crf", "27", "-preset", "fast", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
     os.path.join(a.render, f"{a.nome}-preview.mp4")])


# guia da trilha (raiz do job): tempos de entrada/queda/subida/saida da musica, padrao das edicoes dele
_edl = os.path.join(os.path.dirname(os.path.abspath(a.render)), "edl.json")
if os.path.exists(_edl):
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "guia_trilha.py"), _edl, a.saida])

# ---- checagens objetivas
lf = run(["ffmpeg", "-i", saida_c, "-vn", "-af", "ebur128=framelog=quiet", "-f", "null", "-"]).stderr
integ = [l for l in lf.splitlines() if l.strip().startswith("I:")]
print("loudness:", integ[-1].strip() if integ else "?", f"(alvo {a.lufs} LUFS)")
for p in [saida_c, saida_y, saida_s] + ([saida_l] if not a.sem_legsemmarca else []):
    print(f"duracao {os.path.basename(p)}: {dur(p):.2f}s (corte {D:.2f}s)")
# recorte da regiao da marca em 3 momentos. Linhas: TIKTOK (embaixo no centro, TEM que ter a lupa),
# YOUTUBE (topo direito, TEM que ter "Radar Do Campo"), sem legenda (embaixo no centro, NAO pode ter marca).
Y_LUPA, Y_YT = round(H * 0.865) - 210, max(0, round(H * 0.097) - 210)
chk = Image.new("RGB", (3 * 900, 4 * 420))
for lin, (fonte, x0, y0) in enumerate([(saida_c, 270, Y_LUPA), (saida_y, W - 900, Y_YT), (saida_s, 270, Y_LUPA)] + ([(saida_l, 270, Y_LUPA)] if not a.sem_legsemmarca else [])):
    for i, t in enumerate((D * 0.2, D * 0.5, D * 0.8)):
        png = os.path.join(a.render, "_m.png")
        run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.2f}", "-i", fonte, "-frames:v", "1",
             "-vf", f"crop=900:420:{x0}:{y0}", png])
        chk.paste(Image.open(png).convert("RGB"), (i * 900, lin * 420))
chk_png = os.path.join(a.render, "_checagem_marca.png"); chk.save(chk_png)
print(f"abra {chk_png}: linha 1 lupa visivel, linha 2 'Radar Do Campo' visivel, linha 3 SEM marca, linha 4 SEM marca (com legenda)")

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
for nome_arq in [saida_c, saida_y, saida_s] + ([saida_l] if not a.sem_legsemmarca else []):
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
# A saida com SFX (_montagem/com_sfx) roda DEPOIS desta e refaz o corte pela lista, sem problema.
from lixeira import para_lixeira, tamanho
regen = [os.path.join(a.render, n) for n in ("corte_completo.mp4", "corte_limpo.mp4", "rascunho_tiktok.mp4")]
regen = [p for p in regen if os.path.exists(p)]
liberado = sum(tamanho(p) for p in regen)
movidos, falhou = para_lixeira(regen)
print(f"limpeza: {len(movidos)} arquivo(s) regeneraveis na Lixeira ({liberado / 1e9:.1f} GB)"
      + (f"; nao saiu: {falhou}" if falhou else ""))
