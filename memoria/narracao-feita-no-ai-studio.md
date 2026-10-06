---
name: narracao-feita-no-ai-studio
description: "O usuário gera a narração ele mesmo no Google AI Studio (Gemini 2.5 Pro TTS, voz Puck); a skill de narração via API foi criada e excluída a pedido dele"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 65ce680f-fd21-4e90-a903-8a565318bd79
  modified: 2026-09-24T22:58:21.643Z
---

A narração dos vídeos é o próprio usuário quem gera, no site do Google AI Studio: `gemini-2.5-pro-preview-tts`, voz Puck, com um "Sample Context" de influencer esportivo acelerado. Em 2026-09-24 criei a skill `narracao-gemini`, que gerava pela API. O projeto da chave dele está na camada gratuita, onde o Pro TTS não tem cota (erro 429 `...-FreeTier`), e o Flash leu o roteiro 2x e errou "Premier League". Ele pediu para excluir a skill, e ela foi apagada do HUB.

**Why:** pela API ele só teria acesso ao Pro pagando, e prefere continuar gerando no site.

**How to apply:**
- Não gere narração nem ofereça a skill de novo; peça a narração a ele.
- Ajude no texto: sugerir a frase-ponte de loop no fim do roteiro e conferir a narração contra o roteiro.
- A `GEMINI_API_KEY` continua gravada no Windows.
- O ambiente de clonagem local (Chatterbox, ~4 GB em `C:\Users\bruno\radar-tts` + cache do Hugging Face) ficou pendente: perguntei se ele quer manter.

Relacionado: [[skill-montagem-versao-nova-local]], [[referencia-montagem-faiq]].
