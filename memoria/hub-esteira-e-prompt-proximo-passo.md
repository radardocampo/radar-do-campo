---
name: hub-esteira-e-prompt-proximo-passo
description: "2026-10-31 — cada skill fecha com \"Fechamento obrigatório: Hub\" (avança a etapa) e grava o prompt do próximo passo na pauta; o Hub mostra com botão de copiar"
metadata:
  node_type: memory
  type: project
  originSessionId: 24561cc2-bfab-46bb-ae25-a4525407b99f
  modified: 2026-10-31T16:48:38.127Z
---

Pedido do usuário em 31/10/2026: a esteira do Hub anda sozinha quando cada fluxo termina, e cada pauta traz o prompt pronto para colar no próximo chat.

- Coluna `proximo_prompt` + `proximo_prompt_etapa` em `content_ideas`; `hub.py --proximo-prompt-arquivo F` (criar/atualizar) ou `hub.py prompt <id> <arquivo>`.
- Etapas: garimpo-de-temas → Roteiro (roteiro, notas, prompt de garimpo); garimpo-de-videos → Garimpo (pasta, clipes, prompt de montagem em `_registro/prompt_montagem.txt`); montagem → Pronto na entrega (arquivos + `prompt titulos e tags.txt`), volta a Montagem ao gerar o rascunho do CapCut; titulos-e-tags → Pronto com `titulos e tags.txt` anexado.
- O Hub só usa o prompt gravado se ele for da mesma etapa (montagem e pronto contam como uma só); senão monta um próprio.
- As migrations do Hub não estão alinhadas no histórico remoto: aplicar SQL novo com `supabase db query --linked -f`, nunca `db push`.

**Why:** antes dependia de alguém lembrar de chamar o `hub.py`.
**How to apply:** ao mexer numa skill, manter a seção final "Fechamento obrigatório: Hub". Relacionado: [[atualizar-skill-em-todos-lugares]], [[entrega-prompt-titulos-tags]].
