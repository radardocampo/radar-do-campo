---
name: fluxo-automatico-pos-jogo
description: 2026-10-06 (despedida do Messi) — fluxo agendado na nuvem depois do jogo; a sessão do PC faz redes+garimpo por mensagem; narração = alarme só de bipe no PC (sem voz), ele mesmo gera no AI Studio
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

**Narração:** ele continua gerando no AI Studio. Quando não estiver olhando, avise de forma **barulhenta**: `ferramentas/alarme_narracao.ps1` (só bipes a cada 30 s, SEM VOZ, pedido dele em 06/10; aviso por cima de tudo, texto já copiado, AI Studio aberto) até o .wav aparecer em Downloads. Não gere a voz por conta própria.

**Quando escrever o roteiro (regra dele, 06/10/2026, 21h40):** só depois do apito final **e** de o protagonista sair do estádio, quando acabarem as homenagens. Aí refazer a busca nas redes (o que está rolando no fim) e só então escrever. No Messi eu adiantei o roteiro no intervalo para o alarme tocar mais cedo, e ele mandou parar: "espere o minuto final e até o Messi sair do estádio". Velocidade do alarme vale **depois** desse ponto, não antes.

**Lições da 1ª vez (06/10, Messi):**
- A sessão do PC rodou o alarme como tarefa de fundo com timeout de 10 min; ele morreria antes da narração. Timeout de 2 h (está no fluxo-automatico-pc.md).
- A 1ª narração que chegou era do roteiro antigo (ele tinha gerado no 1º alarme). Antes de montar, confira o `palavras.json` contra o roteiro atual; se não bater, mande o texto novo no chat e peça para gerar de novo.
- A fala/discurso do protagonista no fim é o clipe mais importante e não tinha sido garimpada: peça-a nominalmente ao PC assim que o roteiro sair.
- Reiniciar o PC derruba a extensão Claude in Chrome: ele precisa reconectar; o garimpo segue só com yt-dlp (busca ytsearch) até lá.
- Da nuvem só dá para usar WebSearch (sites de notícia e ESPN bloqueados); a ESPN funciona pelo PowerShell do PC.

**Why:** ele fica perto do PC mas esquece do jogo; sem a voz não há montagem.
Ele quer o máximo na nuvem (crédito); o PC só para o que a nuvem não alcança (redes logadas, download de clipes, bipe). A nuvem não abre sessão no PC: ele precisa abrir a sessão Remote Control lá.
**How to apply:** em pedido de "programar" vídeo de jogo futuro, repita esse desenho; escolha o ângulo sozinho (sem a prévia de candidatos) e avise na entrega o que decidiu. Relacionado: [[fluxo-nuvem-github]], [[narracao-feita-no-ai-studio]], [[garimpo-temas-todas-as-redes]].
