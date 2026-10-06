---
name: limpeza-disco-registro-videos
description: "2026-10-05 limpeza do C: (22→~240 GB livres); vídeo postado vira \"registro final\" (_registro + CSV) e perde clipes/_montagem; Lixeira em 150 GB"
metadata:
  node_type: memory
  type: project
  originSessionId: 4a58b344-206f-4137-aa3a-30597786cdc1
  modified: 2026-10-05T19:52:04.104Z
---

Em 2026-10-05 o C: (930 GB) estava com 22,8 GB livres. Cada vídeo da skill ocupava ~5 GB: ~2,3 GB de `clipes`, ~3 GB de `_montagem\render` e só ~1 GB de finais.

O usuário pediu um **"end-point" (registro final) de cada vídeo postado** antes de limpar:
- **O que fica na pasta:** `Videos prontos\`, ROTEIRO.txt, Narração.wav, capa, .srt e MP4 finais soltos na raiz.
- **`_registro\`:** os arquivos de trabalho pequenos da raiz, os textos de `_montagem` (edl.json, cmp, scripts), as transcrições e `lista_clipes.txt`.
- **O que vai para a Lixeira:** `clipes`, `_montagem`, `frames`, `transcricoes`.
- **Índice geral:** `Shorts\Registro dos vídeos postados.csv` (separador `;`).

Os scripts usados (`registro.ps1`, `lixeira.ps1`) ficaram no scratchpad da sessão, ou seja, não persistem.

**Why:** ele quer poder rever ou remontar um vídeo antigo sem guardar 5 GB por vídeo.

**How to apply:**
- **Lixeira:** ele aumentou a do C: para 150 GB. Nunca mandar à Lixeira mais do que a capacidade dela, senão o Windows apaga o excedente para sempre. Quem esvazia é sempre ele.
- **Skill de montagem (HUB "Versão 2026-10-05", FEITO):** o usuário recusou limpar tudo na entrega porque pode pedir correção ou remontagem. Ficou assim:
  - Na entrega, o `render_final.py` manda para a Lixeira só `corte_completo`, `corte_limpo` e `rascunho_tiktok`, e refaz o corte pela `lista_completo.txt` se faltar.
  - Os clipes só saem com o `fechar_videos.py --executar`: vídeos com mais de 15 dias, e só quando ele pedir. Ele cria o `_registro` e atualiza o CSV.
  - Helper `lixeira.py`. `.skill` INSTALADO por mim no claude.ai em 2026-10-05 (pelo Chrome, "Fazer upload e substituir").
- **92 vídeos manuais antigos (25,6 GB, 98% são os próprios finais 1440x2560 a 20 Mbps):** ele disse "depois eu resolvo". Opções que ofereci: comprimir em H.265, manter um final só, ou mandar para o Drive.
- **ComfyUI:** os modelos (183 GB) já foram para a Lixeira em 2026-10-05. O Comfy Desktop continua instalado (3 instalações de ~21 GB) e ele ainda não quer desinstalar.
- **Defender:** o acesso controlado a pastas protege `Documents` e bloqueia o terminal em silêncio (Set-Content "funciona", mas o arquivo não aparece). Ele desligou a proteção para a limpeza. Recomendei religar.
- **Pendência do usuário:** limpar o cache do CapCut por dentro do app.
- **CapCut:** ele quer só os 10 projetos mais recentes.
- **Downloads:** MP4 de nome numérico são downloads do TikTok, descartáveis.

Ver [[skill-montagem-versao-nova-local]].
