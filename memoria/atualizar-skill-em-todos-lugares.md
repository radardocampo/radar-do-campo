---
name: atualizar-skill-em-todos-lugares
description: "quando o usuário pede para atualizar uma skill, trocar em TODOS os lugares (HUB + .skill, nuvem/GitHub) e fazer o upload no claude.ai por ele"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 65b0ee74-e63b-423f-8d9a-40e9bb91b1df
  modified: 2026-10-08T20:29:59.002Z
---

Regra do usuário de 2026-10-08: "quando eu peço pra atualizar uma skill, você troca em todos os lugares em que ela está, na pasta, no GitHub, e faz o upload dela pra mim".

Todo pedido de atualização de skill (ou mudança de regra que vai para uma skill) só termina quando a skill está igual nestes lugares:
1. **HUB:** `HUB Radar do Campo\Claude\skills claude\versao-nova-2026-09-22\<skill>\`.
   - Backup antes de mexer: `_bak-AAAA-MM-DD-<motivo>`.
   - Na montagem-de-video, mudar a data da linha "Versão".
   - Reempacotar `<skill>.skill` (zip com a pasta `<skill>/` na raiz, sem `__pycache__`).
2. **Nuvem/GitHub:** copiar o `SKILL.md` para `nuvem\.claude\skills\<skill>\` e as memórias novas para `nuvem\memoria\`.
   - Commit e push no repo radardocampo/radar-do-campo.
   - Os scripts da nuvem são adaptados ao `RADAR_BASE`: só copie script se a mudança for nele, e mantenha a adaptação.
   - Não incluir no commit alterações dele que já estavam pendentes (ex.: `ferramentas/enviar.ps1`).
2b. **Antigravity (plano B):** rodar `HUB Radar do Campoadar-do-campoerramentas\sincronizar.ps1` — copia SKILL.md do HUB para `.claude/skills` e `.agents/skills`, memórias para `memoria/`, commit+push. Rodar também ao criar memória nova. Ver [[antigravity-plano-b]].
3. **claude.ai:** fazer o upload pelo Claude in Chrome.
   - Endereço: claude.ai/customize/skills/new/upload.
   - Mandar o arquivo com `file_upload` no input "Arquivo de habilidade" e clicar em "Fazer upload e substituir".
   - Isso também atualiza a cópia instalada no PC (AppData\...\skills-plugin).
   - Conferir a versão nova na lista de habilidades.

**Why:** ele não quer ter que lembrar de reenviar o `.skill`. Antes ficavam versões diferentes no HUB, na nuvem e no claude.ai.

**How to apply:**
- No fim de qualquer atualização de skill, faça os 3 passos sem perguntar.
- Entregue uma linha por lugar dizendo o que foi feito.
- O pedido dele de atualizar a skill vale como autorização para o upload daquela skill.
- Relacionado: [[skill-montagem-versao-nova-local]], [[fluxo-nuvem-github]].
