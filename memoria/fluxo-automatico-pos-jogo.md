---
name: fluxo-automatico-pos-jogo
description: 2026-10-06 (despedida do Messi) — fluxo agendado na nuvem depois do jogo; a sessão do PC faz redes+garimpo por mensagem; narração = alarme em voz alta no PC, ele mesmo gera no AI Studio
metadata:
  node_type: memory
  type: feedback
  originSessionId: session_01S14iVJBPGyyxJY9hNAMV9m
  modified: 2026-10-06T21:00:00.000Z
---

O usuário quer poder agendar um vídeo inteiro para depois de um jogo, sem estar no PC: garimpo de temas → roteiro → garimpo de vídeos → montagem, sem pedir permissão no meio.

Como ficou (primeira vez em 06/10/2026, Argentina x Benin, despedida do Messi, 20h):
- Routine (`create_trigger`, one-shot) acorda a sessão da nuvem ~40 min depois do apito final.
- A nuvem manda as etapas por `send_message` para a sessão do Claude no PC (Remote Control, pasta `nuvem`), que tem o Chrome logado e o yt-dlp. A sessão do PC **só segue mensagem de outra sessão se o usuário autorizar no chat dela** (ela recusou em 06/10 sem isso). O roteiro do PC está em `ferramentas/fluxo-automatico-pc.md`.
- A nuvem não recebe resposta: lê a última mensagem do PC com `list_events`/`get_session`, e o envio da pasta aparece como branch `video/<nome>`.

**Narração:** ele continua gerando no AI Studio. Quando não estiver olhando, avise de forma **barulhenta**: `ferramentas/alarme_narracao.ps1` (voz alta + bipes a cada 2 min, aviso por cima de tudo, texto já copiado, AI Studio aberto) até o .wav aparecer em Downloads. Não gere a voz por conta própria.

**Why:** ele fica perto do PC mas esquece do jogo; sem a voz não há montagem.
**How to apply:** em pedido de "programar" vídeo de jogo futuro, repita esse desenho; escolha o ângulo sozinho (sem a prévia de candidatos) e avise na entrega o que decidiu. Relacionado: [[fluxo-nuvem-github]], [[narracao-feita-no-ai-studio]], [[garimpo-temas-todas-as-redes]].
