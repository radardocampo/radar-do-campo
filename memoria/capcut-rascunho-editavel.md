---
name: capcut-rascunho-editavel
description: "rascunho editável no CapCut (Passo 9 da skill de montagem, HUB 2026-10-18): capcut_projeto.py sobre o modelo dele; keyframes em tempo da fonte; oferecer no fim de toda entrega; gerar com CapCut fechado"
metadata:
  node_type: memory
  type: project
  originSessionId: 9ea89624-719f-49b0-9bae-3f94d60de664
  modified: 2026-10-18T22:20:45.805Z
---

Em 2026-10-18 (Andreas Pereira) o usuário pediu a timeline editável no CapCut em vez do Concat ([[concat-timeline-editavel]]). A 1ª versão tinha o corte renderizado por cima, e ele reclamou: "não consigo mexer no zoom, enquadramento e efeitos, a legenda está diferente, e quero a música do meu rascunho anterior igual". A versão aprovada parte do rascunho-modelo dele e deixa tudo nativo. No Bernal x Yamal ele pediu de novo ("como fizemos na última").

**Agora é parte da skill (HUB "Versão 2026-10-18", Passo 9):**
- Comando: `scripts/capcut_projeto.py "<job>" --nome "Radar - <título>" [--modelo ...] [--sfx-mudo]`, mais a fonte `assets/Montserrat-ExtraBoldItalic.ttf`.
- **Oferecer no fim de toda entrega** e gerar quando ele aceitar. Não gerar sem perguntar, porque precisa fechar o CapCut.
- Os detalhes técnicos e as pegadinhas estão no Passo 9: modelo "0417-cópia… (15)", cor gravada nas cópias, flash em PNG, filtro 褪色黑白, cards nas faixas CARDS, legenda com um trecho por palavra.

**Corrigido em 2026-10-18, depois de comparar as edições dele:**
- O CapCut lê o `time_offset` do keyframe em **tempo da fonte**, não relativo ao segmento. O script gravava relativo, então o pan e o soco ficavam parados em todo clipe com entrada > 0. Ele refez o pan do gol do Abde à mão.
- Agora o script converte (`in + t × velocidade`). Conferi no JSON gerado, mas ainda não abri no CapCut.
- A faixa SFX vem ligada, porque ele ligou nos dois rascunhos.

**O que ele fez nos rascunhos:** reenquadrou e fez punch-in em alguns shots, ligou o SFX, ocultou a lupa e exportou um arquivo só (-14,4 e -13,3 LUFS, porque o CapCut não normaliza). Não mexeu na legenda nem no volume da trilha do modelo.

**Para comparar a edição dele:** use o `draft_content.json` do "Radar - <título>" contra o mesmo script rodado numa raiz temporária no job (`_montagem/cmp/capcut_orig`). O resumo que usei está em `_montagem/cmp/resumo_*.txt` do Andreas e do Bernal.

**How to apply / pegadinhas:**
- Rodar com o CapCut FECHADO: `taskkill //F //IM CapCut.exe` se só o meu rascunho estiver aberto; se o projeto dele estiver aberto, pedir antes. Com o CapCut aberto, o root_meta_info.json é reescrito e o rascunho some ou abre a versão velha.
- A home do CapCut abre no monitor VX-215X e o editor no 27G2G4.
- O computer-use precisa de "CapCut", "capcut.exe" e "File Explorer" (barra de tarefas).
