---
name: hub-esteira-e-prompt-proximo-passo
description: "2026-10-31 — selo trabalhando/aguardando em cada pauta (hub.py status); Pronto só vem da titulos-e-tags; cada skill fecha com \"Fechamento obrigatório: Hub\" (avança a etapa) e grava o prompt do próximo passo na pauta; o Hub mostra com botão de copiar"
metadata:
  node_type: memory
  type: project
  originSessionId: 24561cc2-bfab-46bb-ae25-a4525407b99f
  modified: 2026-10-31T16:48:38.127Z
---

Pedido do usuário em 31/10/2026: a esteira do Hub anda sozinha quando cada fluxo termina, e cada pauta traz o prompt pronto para colar no próximo chat.

- Coluna `proximo_prompt` + `proximo_prompt_etapa` em `content_ideas`; `hub.py --proximo-prompt-arquivo F` (criar/atualizar) ou `hub.py prompt <id> <arquivo>`.
- Etapas: garimpo-de-temas → Roteiro (roteiro, notas, prompt de garimpo); garimpo-de-videos → Garimpo (pasta, clipes, prompt de montagem em `_registro/prompt_montagem.txt`); montagem → fica em Montagem na entrega (arquivos + `prompt titulos e tags.txt`) e no rascunho do CapCut, nunca marca Pronto (31/10, ele viu o Kaio Jorge ir Pronto → Montagem → Pronto e pediu um padrão); titulos-e-tags → Pronto com `titulos e tags.txt` anexado.
- O Hub só usa o prompt gravado se ele for da mesma etapa (montagem e pronto contam como uma só); senão monta um próprio.
- **Selo de andamento (31/10/2026, pedido dele: "bater o olho e saber se o Claude está trabalhando nela ou esperando o próximo passo"):** colunas `andamento` ('trabalhando' | 'aguardando'), `andamento_texto`, `andamento_em` em `content_ideas` (a etapa continua em `status`). `hub.py status <id> trabalhando|aguardando [--texto]` ou `--status S [--status-texto]` em criar/etapa/atualizar. Toda skill: `trabalhando` na abertura, `--status aguardando` no fechamento (montagem: "Esperando refinamento no CapCut"; rascunho do CapCut: "No CapCut · esperando títulos e tags"; titulos-e-tags: `--etapa pronto --status aguardando`). Sem texto, o banco põe o padrão da etapa; mudar a etapa sem `--status` vira aguardando (gatilho). O Hub mostra bolinha pulsando em trabalhando, "sem notícias há Xh" depois de 3 h, e filtro "Trabalhando agora" / "Esperando" em Vídeos → Pautas.
- As migrations do Hub não estão alinhadas no histórico remoto: aplicar SQL novo com `supabase db query --linked -f`, nunca `db push`.

**Why:** antes dependia de alguém lembrar de chamar o `hub.py`.
**How to apply:** ao mexer numa skill, manter a seção final "Fechamento obrigatório: Hub". Relacionado: [[atualizar-skill-em-todos-lugares]], [[entrega-prompt-titulos-tags]].
