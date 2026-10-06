---
name: narracao-le-rotulos-do-roteiro
description: O AI Studio narra os rótulos (Gancho/Contexto/Reviravolta/Payoff) se o roteiro for colado com eles; entregar também a versão limpa
metadata:
  node_type: memory
  type: feedback
  originSessionId: ff64ded1-225b-40fc-90a7-3673d8735510
  modified: 2026-10-02T04:43:52.638Z
---

Em 02/10/2026 (Højlund x Jorge Jesus), o usuário colou no AI Studio o roteiro com as etiquetas da skill garimpo-de-temas, e a voz leu "Contexto", "Reviravolta" e "Payoff". A palavra "Gancho:" e o início "Todo mundo viu o" também sumiram. Na montagem cortei os rótulos do áudio, e o usuário aprovou seguir assim.

**Why:** as etiquetas existem só para a revisão do roteiro; narradas, viram palavras soltas que precisam ser cortadas à mão.

**How to apply:** ao entregar um roteiro (skill garimpo-de-temas), inclua logo abaixo um bloco "texto para o AI Studio", corrido e sem etiquetas. Na montagem, se a narração tiver rótulos, corte-os nos silêncios em volta (medir a energia), e não pelos tempos do Whisper, porque a pausa logo depois do rótulo some. Relacionado: [[narracao-feita-no-ai-studio]].
