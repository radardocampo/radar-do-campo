# Radar do Campo — sessão na nuvem

Canal de Shorts/Reels de futebol. Este repositório leva para a nuvem as skills,
os assets e as memórias que, no PC do usuário, ficam em
`C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\`.

## Divisão do trabalho
- **Nuvem (aqui):** garimpo de temas, roteiros, títulos/tags e **montagem**.
- **PC do usuário:** garimpo/download dos clipes (Chrome logado + yt-dlp) e narração (AI Studio).
  Não tente baixar clipes daqui: as redes bloqueiam IP de servidor.

## Antes de qualquer coisa
1. Leia `memoria/MEMORY.md` e as memórias que ele aponta. São as regras de estilo do usuário
   (gancho, loop, LUFS, marcas, o que ele mudou nas edições). Valem tanto quanto as skills.
2. Rode `bash ferramentas/preparar_nuvem.sh` (instala ffmpeg e libs Python, exporta `RADAR_BASE`).
3. As skills estão em `.claude/skills/`. Os caminhos `C:\...\Radar do Campo\` delas
   equivalem à raiz deste repositório (`$RADAR_BASE`). Barras invertidas viram `/`.

## Montagem de um vídeo
O usuário sobe a pasta do vídeo num branch `video/<nome>` com
`Videos prontos/Shorts/<nome>/` (roteiro, narração, `clipes/`, inventário).
1. `git fetch origin video/<nome> && git checkout video/<nome>`
2. `python ferramentas/pacote.py juntar "Videos prontos/Shorts/<nome>"`
3. Siga a skill `montagem-de-video` normalmente (rascunho, revisão, 4 entregas).
4. Para devolver só as entregas, commite **apenas** `Videos prontos/Shorts/<nome>/Videos prontos/`
   e `legenda para o CapCut.srt` (nunca `clipes/` nem `_montagem/` de volta, já estão no PC):
   `python ferramentas/pacote.py partir "Videos prontos/Shorts/<nome>/Videos prontos"`, commit, push no mesmo branch.
5. Diga ao usuário para rodar no PC: `ferramentas\receber.ps1 "<nome>"`.

## Tempos da narração (a nuvem não baixa o Whisper)
O Hugging Face é bloqueado aqui. Se o branch tiver `tempos do pre-feito/palavras.json` (ou `palavras.json` na pasta do vídeo), use esses tempos: foram transcritos no PC com faster-whisper medium sobre o áudio do arquivo, sem cortar nada. Corrija a grafia pelo roteiro. Se faltar, peça ao usuário para rodar no PC `python ferramentas/tempos_audio.py <áudio ou vídeo> <pasta do vídeo>/palavras.json` e subir. Não baixe modelos de fora.

## Não versionar
`clipes/`, `_montagem/`, `frames/` só sobem no branch do vídeo. Nunca faça merge de `video/*` na `main`.
Trilhas (`Musicas edição/`) não estão aqui: o usuário coloca a trilha no CapCut.

## Memórias novas
Quando o usuário der uma regra nova, grave em `memoria/` (mesmo formato) e atualize `memoria/MEMORY.md`,
commitando na `main`. No PC, ele roda `git pull` para trazer de volta.
