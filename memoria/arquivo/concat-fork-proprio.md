---
name: concat-fork-proprio
description: "Fork do Concat (editor AGPL) na conta radardocampo, clonado em Desktop/Concat-fonte; regras de nome/licença"
metadata:
  node_type: memory
  type: project
  originSessionId: 98672698-da20-4796-8713-95e0baef05a4
  modified: 2026-10-16T18:16:39.689Z
---

2026-10-16: fork criado em github.com/radardocampo/Concat (upstream jub0t/Concat, AGPL-3.0, remote `upstream` configurado). Clone local: `C:\Users\bruno\Desktop\Concat-fonte`. Uso só pessoal, sem vender.

**Why:** ele quer modificar o editor por conta própria; autoria original (jub0t) permanece, as alterações dele são dele.
**How to apply:** manter LICENSE e avisos; TRADEMARK.md pede outro nome/ícone só se distribuir build modificada a terceiros (uso pessoal ok). Rust não está instalado (sem cargo) — instalar rustup antes de compilar; versão em uso é o instalador em AppData\Local\Programs\Concat. Ver [[concat-timeline-editavel]].

**Atualização 2026-10-16:** compilado e testado. Usar a branch `meu-concat` (base tag v0.2.7); o `main` do fork/upstream (pós-0.2.7) crashava ao abrir (0xC0000005). Build: `powershell -File Desktop\Concat-fonte\compilar.ps1` (cmake do winget, LLVM, FFmpeg n8.1 em Concat-fonte-deps; usar `--release`, não `--profile app`; ~45 min na 1ª vez). Exe: `Concat-fonte\src\target\release\concat.exe`. O instalado em AppData\Local\Programs\Concat NÃO foi substituído.
