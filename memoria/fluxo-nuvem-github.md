---
name: fluxo-nuvem-github
description: 2026-10-06 — roteiro e montagem rodam na nuvem (crédito US$100 até 05/11) via repo privado radardocampo/radar-do-campo; garimpo e narração no PC
metadata:
  node_type: memory
  type: project
  originSessionId: 5be9d2cd-f179-4624-8be6-f1f0696a45a2
  modified: 2026-10-06T18:31:15.268Z
---

Repo local: `Radar do Campo\nuvem\` → github.com/radardocampo/radar-do-campo (privado). Tem cópia das 4 skills (caminhos via env RADAR_BASE), logos, Sons edição, memórias (`memoria/`).
PC → nuvem: `ferramentas\enviar.ps1 "<vídeo>"` (branch video/<nome>, arquivos >90MB partidos por pacote.py). Nuvem → PC: `ferramentas\receber.ps1 "<vídeo>"`.

Ele NÃO quer alternar entre o chat do PC e o da nuvem: tudo resolvido lá. Por isso enviar.ps1 já prepara a narração no PC (narracao.py → _montagem/, ou tempos_audio.py se houver "pré feito"), porque a nuvem não baixa o Whisper. Atalhos na raiz: "Enviar para nuvem.bat" / "Receber da nuvem.bat" (pasta/branch mais recente). .claude/settings.json com permissões para a nuvem foi bloqueado pelo classificador — depende do usuário.

**Why:** usuário quer gastar o crédito de sessão na nuvem antes de expirar (05/11/2026 04:59).
**How to apply:** ao mudar skill ou memória aqui no PC, copiar também para `nuvem\` e dar push; antes de usar a nuvem, `git pull` no PC traz memórias novas de lá.
