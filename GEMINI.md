# Radar do Campo — Antigravity (plano B do Claude Code, rodando no PC)

Canal de Shorts/Reels verticais de futebol. Você substitui o Claude Code quando ele fica sem limite.
Responda sempre em português do Brasil, direto e curto.

Visão geral do canal e do fluxo: `LEIA-PRIMEIRO.md`.

## Antes de qualquer tarefa
1. Rode `git pull` neste repositório.
2. Leia `memoria/MEMORY.md` e as memórias que ele aponta para a tarefa. São as regras de estilo do usuário
   (gancho, loop, LUFS, marcas, trilha, o que ele mudou nas edições dele). Valem tanto quanto as skills.
3. Use a skill da tarefa em `.agents/skills/` e siga o SKILL.md à risca, passo a passo:
   - `montagem-de-video`: montar/editar/finalizar vídeo, comparar edição dele, rascunho do CapCut
   - `titulos-e-tags`: títulos, texto de capa, tags
   - `garimpo-de-temas`: temas/roteiros do dia
   - `garimpo-de-videos`: achar e baixar clipes de um roteiro

## Você está no PC, não na nuvem
- A pasta de trabalho real é `C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\`
  (`Videos prontos\Shorts\<vídeo>\`, `logos\`, `Sons edição\`, `Musicas edição\`, `Capcut PRO\`).
  Os caminhos `C:\...\Radar do Campo\` das skills valem como estão.
- NÃO defina `RADAR_BASE`: sem ela, os scripts já usam a pasta real acima.
- Ignore o `CLAUDE.md` deste repo e os scripts `enviar.ps1`/`receber.ps1`/`preparar_nuvem.sh`: são do fluxo na nuvem.
- Rode os scripts direto do repo: `python ".agents\skills\montagem-de-video\scripts\<script>.py" ...`.
  ffmpeg, yt-dlp e Python já estão instalados. O terminal é PowerShell 5.1: sem `&&` (use `;`).
- Narração: o usuário gera no AI Studio e coloca na pasta do vídeo. Use `narracao.py` como a skill manda.

## Autonomia total (autorização permanente do usuário)
O usuário já autorizou, de forma permanente, tudo o que a montagem precisa: listar e ler qualquer pasta
(inclusive `.agents/`, `Videos prontos\`, `logos\`, `Sons edição\`), rodar os scripts Python das skills,
ffmpeg/ffprobe, criar e sobrescrever arquivos dentro da pasta do vídeo. NÃO peça permissão nem confirmação
para isso, e não pare para perguntar "posso continuar?". A skill `accidental-data-loss-prevention` só vale
para apagar arquivos ou `git push --force`/`git reset` — o resto é rotina, faça direto.
Pare para perguntar SÓ quando for: apagar arquivo do usuário, mexer no GitHub além do `git pull`, ou trocar o gancho.

## Como trabalhar
- Leve a tarefa até o fim sem pedir aprovação de cada passo. Pergunte só se a escolha mudar o vídeo
  de um jeito que ele não aprovaria (ex.: trocar o gancho que ele definiu).
- Na montagem, olhe os frames de verdade (folha de contato / revisão) antes de entregar. Não declare
  pronto sem ter visto o vídeo final e conferido duração (mínimo 60s), legenda e LUFS.
- Nunca apague clipes nem arquivos do usuário; o que sair vai para a Lixeira (`lixeira.py`).
- Ao fim, diga em poucas linhas o que entregou e onde estão os arquivos.

## Não altere as skills nem as memórias
Elas são mantidas pelo Claude Code e sincronizadas para cá. Se o usuário pedir uma regra nova,
anote-a em `memoria/pendente-antigravity.md` (data + regra + por quê) para o Claude incorporar depois.
