---
name: antigravity-plano-b
description: 2026-10-20 — Antigravity (Gemini) é o plano B quando o Claude fica sem limite, principalmente para montagem; repo HUBadar-do-campo com GEMINI.md + .agents/skills
metadata:
  type: project
---

O usuário deixou o Antigravity IDE pronto como reserva para quando os tokens do Claude acabarem; uso principal = montagem (garimpo continua no Claude).
Workspace: `HUB Radar do Campoadar-do-campo` (mesmo repo do GitHub). `GEMINI.md` = regras do Antigravity (rodando no PC, sem RADAR_BASE, ignora CLAUDE.md da nuvem); skills espelhadas em `.agents/skills/`.
O Antigravity não altera skills/memórias: regras novas dadas a ele ficam em `memoria/pendente-antigravity.md`.

**Why:** ele quer o plano B sempre atualizado sem lembrar disso.
**How to apply:** toda mudança de skill ou memória → rodar `ferramentas\sincronizar.ps1` ([[atualizar-skill-em-todos-lugares]]). Ao começar sessão, checar se existe `memoria/pendente-antigravity.md` e incorporar as regras.
