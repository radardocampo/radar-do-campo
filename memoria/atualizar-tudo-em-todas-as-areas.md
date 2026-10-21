---
name: atualizar-tudo-em-todas-as-areas
description: "2026-10-21 — toda atualização (skill, regra, memória, fluxo, contexto) deve ser revisada e propagada a TODAS as áreas e locais, incluindo LEIA-PRIMEIRO.md/CLAUDE.md/GEMINI.md/AGENTS.md do repo"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0bcd4986-e6a0-4f99-afda-d6249f77164e
  modified: 2026-10-21T21:55:03.212Z
---

Pedido do usuário em 2026-10-21: "toda vez que a gente for atualizar alguma coisa, tu atualize todas as áreas, em todos os locais e todas as áreas dentro do repositório do GitHub — skills, memória, contexto, tudo; verifica e vê o que tem que atualizar".

Ele quer que outra IA (Gemini, ChatGPT etc.) tenha o mesmo conhecimento que o Claude, lendo só o repo radar-do-campo.

**Why:** se trocar de IA um dia, o repo tem que ser a cópia completa e atual do conhecimento do canal.
**How to apply:** em toda mudança, sem perguntar, revisar e atualizar o que for afetado:
- skill no HUB + `.skill` + upload claude.ai ([[atualizar-skill-em-todos-lugares]]);
- memória local + `memoria/` + `MEMORY.md`;
- `LEIA-PRIMEIRO.md` (canal, fluxo, onde está cada coisa, regras de ouro), `CLAUDE.md`, `GEMINI.md`, `AGENTS.md` quando o fluxo/contexto mudar;
- depois rodar `ferramentas\sincronizar.ps1` ([[antigravity-plano-b]]). Na entrega, uma linha por lugar.
