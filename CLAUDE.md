# Radar do Campo — sessão na nuvem

Canal de Shorts/Reels de futebol. Este repositório leva para a nuvem as skills,
os assets e as memórias que, no PC do usuário, ficam em
`C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\`.

Visão geral do canal e do fluxo para qualquer IA: `LEIA-PRIMEIRO.md`.

## Regra principal: resolver tudo aqui
O usuário não quer alternar entre esta sessão e a do PC. Leve cada tarefa até o fim nesta sessão.
Quando faltar algo, decida pelo padrão das skills e das memórias e siga em frente, avisando na entrega o que decidiu.
Só pare para perguntar se a escolha mudar o vídeo de forma que ele não aprovaria (ex.: trocar o gancho que ele montou).
Nunca peça para ele rodar algo no PC no meio do trabalho. A única ação dele no PC é, no fim, dar dois cliques em
`Receber da nuvem.bat` (ou, no meio, `Enviar para nuvem.bat` para mandar a pasta).

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
   No Linux a caixa importa: a subpasta pode se chamar `Videos Prontos` ou `Videos prontos`; use a que existir.

## Montagem de um vídeo
O usuário sobe a pasta do vídeo num branch `video/<nome>` com `Videos prontos/Shorts/<nome>/`
(roteiro, narração, `clipes/`, inventário `clipes/LEIA - onde esta cada trecho.txt`).
1. `git fetch origin video/<nome> && git checkout video/<nome>`
2. `python ferramentas/pacote.py juntar "Videos prontos/Shorts/<nome>"` (as partes `.parteNNN` ficam; não apague nem commite exclusão delas).
3. **Narração: já vem pronta do PC. Não rode `narracao.py` aqui e não baixe modelos (o Hugging Face é bloqueado).**
   - Caso normal: `<job>/_montagem/` já tem `narracao_final.wav`, `pausas.json` e `palavras.json`, gerados pelo `narracao.py` no PC. Pule esse passo da skill e siga dele.
   - Montagem parcial do usuário (arquivo `*pré feito*.mp4` / `*pre-feito*`): a narração completa, já cortada, e a música estão no áudio desse vídeo. `tempos do pre-feito/palavras.json` e `frases.srt` têm os tempos por palavra sobre esse áudio, sem cortes. Use esse áudio como está (sem normalizar se já estiver perto de -10 LUFS), mantenha intacto o trecho que ele montou e monte o resto em cima dessa linha do tempo.
   - Em todos os casos, corrija a grafia das palavras pelo roteiro (nomes de jogadores, acentos).
   - Se não houver tempos nenhum: alinhe o roteiro pelas pausas (`ffmpeg silencedetect`) e pela energia da voz e avise na entrega que a legenda pode estar 0,1–0,2s fora.
4. Siga a skill `montagem-de-video` (rascunho, revisão visual, 2 entregas: com legenda e sem legenda, sem logo). Faça a revisão você mesmo pelos frames; não espere aprovação do rascunho.
5. Entrega: `python ferramentas/pacote.py partir "<job>/<subpasta Videos prontos>"`, depois `git add -f` **apenas** dessa subpasta,
   de `<job>/legenda para o CapCut.srt` e de `<job>/_montagem/*.json` (receita, pequenos). Commit e push no mesmo branch.
   Nunca `git add -A` e nunca commite `clipes/` (já está no PC).
6. Termine com um resumo curto do que montou e das decisões, e diga: "Pronto. No PC, dê dois cliques em `Receber da nuvem.bat`."

## Não versionar
`clipes/`, `_montagem/`, `frames/` só sobem no branch do vídeo. Nunca faça merge de `video/*` na `main`.
Trilhas (`Musicas edição/`) não estão aqui: o usuário coloca a trilha no CapCut (a menos que já venha no pré-feito).

## Memórias novas
Quando o usuário der uma regra nova, grave em `memoria/` (mesmo formato), atualize `memoria/MEMORY.md`
e commite na `main` (`git stash` / troque de branch se precisar, sem levar arquivos do vídeo).

- Comparar a edição dele (desde 18/10 feita no rascunho do CapCut que geramos): comparar o projeto com `compara_capcut.py` da skill montagem-de-video, salvar a lição numa memória a cada vídeo (`comparacao-lote-*`), gravar `<job>/_montagem/cmp/comparado.txt` e só no fim atualizar a skill (versão 2026-10-21).