---
name: concat-timeline-editavel
description: Concat (editor open source) instalado em 2026-10-15; gera projeto de timeline editável a partir da EDL pra ele refinar sem gastar uso
metadata:
  node_type: memory
  type: project
  originSessionId: ae7a13dd-5a42-4e8e-b50a-ca721995bb0e
  modified: 2026-10-18T22:20:47.563Z
---

**Substituído em 2026-10-18 pelo rascunho no CapCut** ([[capcut-rascunho-editavel]]), a pedido dele. O Concat só volta se ele pedir.

Pedido do usuário (2026-10-15): fluxo normal intacto (4 arquivos em Videos prontos/), e **além disso** um projeto do Concat com a mesma montagem em camadas, pra ele ajustar zoom/corte/legenda sozinho em vez de me pedir de novo.

**Estado:** Concat 0.2.7 instalado em `%LOCALAPPDATA%\Programs\Concat\concat.exe` (hash conferido). Configurações › Remoto ligado em 127.0.0.1:7420, token que EU defini: `radar-do-campo-local-2026` (só loopback). Gerador: `HUB Radar do Campo/concat/concat_build.py <pasta_do_video> --nome X` — lê `_montagem/edl.json`, `narracao_final.wav`, `blocos_legenda.json`; grava `<pasta>/Projeto Concat/<nome>/concat.json`. Testado no Endrick/Roma: quadros batem com o vídeo final.

**Why:** o usuário quer economizar uso; o ajuste fino passa a ser dele no Concat.

**How to apply / pegadinhas da API (aprendidas na marra):**
- O app precisa estar aberto com Remoto ligado (o exe instalado NÃO tem o CLI `api`). Aberto no Windows pelo exe: `concat.exe --project <pasta>` abre o projeto.
- **Precisa `project.save` antes de `project.close`**, senão o concat.json fica vazio.
- **A ÚLTIMA faixa da lista fica POR CIMA** (contrário da doc). Legenda = `addTrack` novo no topo.
- `moveClips` pra faixa ocupada empurra o clipe pro fim; não existe sourceStart no addClip: faz `addClip` em faixa de staging → `trimClip start` (delta = in/rate) → `trimClip end` → `setClipTransform` → `moveClips` pra faixa final.
- Cover 9:16: scale = (cover/contain)·zoom; offset = (0.5−cx)·w·contain·mult/W. Funciona.
- Diálogo de arquivo do Windows não aceita digitação minha (restrição do computer-use): abrir projeto via `--project`.
- Ainda NÃO replica: karaokê palavra a palavra (hoje é 1 título por bloco), tampar marca d'água (clone), flash/SFX, trilha, marca d'água do Radar, setas. Export do Concat não foi testado.

**Atualização 2026-10-16 (Rossi):** ele quer o projeto "igual à entrega" (mesma legenda, zoom, tudo). Feito SEM o modo Remoto (a porta 7420 não subiu e os cliques na tela de config não respondiam): `_montagem/scripts/concat_projeto.py <pasta> --nome X` grava o concat.json direto e abre com `concat.exe --project <pasta do projeto>` (carrega em ~1 min). Faixas: FONTES (oculta, clipes brutos com zoom/cx/cy da EDL), VIDEO (o `-completo-sem-legenda.mp4` cortado por shot = cor, pan, flash, tampar iguais), NARRACAO, TEXTO (oculta, blocos editáveis), LEGENDA (faixa karaokê em ProRes 4444 tela cheia, alpha funciona), MARCA (lupa em qtrle tela cheia). Conferido na prévia do Concat: legenda, lupa e flashback iguais. Não abrir o Concat duas vezes (open_application cria outra instância).
