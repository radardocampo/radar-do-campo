---
name: skill-montagem-versao-nova-local
description: A skill montagem-de-video instalada ainda é a antiga (Remotion); a versão nova com scripts está no HUB (instalada v12 em 2026-09-27 = HUB)
metadata:
  node_type: memory
  type: project
  originSessionId: 28d61b0f-8ec4-43d3-8538-39bc650fdb15
  modified: 2026-10-01T21:57:12.184Z
---

Em 2026-09-23 a skill `montagem-de-video` carregada ainda era a antiga (Remotion, legenda a 74%). Ou seja, o usuário não gravou o `.skill` novo de [[referencia-montagem-carrascal]]. A versão nova (pipeline ffmpeg + PIL, narração 1,2x, karaokê a 54%) foi copiada do scratchpad temporário para:
`HUB Radar do Campo\Claude\skills claude\versao-nova-2026-09-22\` (pastas `montagem-de-video/`, `garimpo-de-videos/` e os `.skill`).

Correções feitas nos scripts dessa cópia durante o vídeo da camisa amarela. O `.skill` empacotado NÃO tem essas correções:
- `render_final.py`: a marca d'água sumia depois de ~10s (overlay de PNG único). Agora entra com `-loop 1 -framerate 60` e `shortest=1`.
- `render_final.py`: com o áudio no mesmo `filter_complex` da logo e da legenda, o ffmpeg descartou ~9s de narração no Completo sem dar erro (o arquivo continuava com 62s; foi o usuário que percebeu o pulo). Agora o áudio é renderizado num passo separado (`audio_final.wav`), e o script compara o envelope de cada entrega com a narração segundo a segundo, abortando se divergir. Duração igual não prova que o áudio está inteiro.
- `prep_shots.py`: `tpad` no fim de cada shot. Fontes de 25/30fps perdiam 1-2 quadros por shot, somando 0,16s a menos.
- `legenda_karaoke.py`: não chuta mais nome próprio pela maiúscula de início de frase ("Dezesseis", "Naquela" saíam maiúsculos). Nome que só abre frase vai por `--nomes`.

Em 2026-09-24 (vídeo do Faiq Bolkiah) o usuário mudou a entrega padrão, e `render_final.py` + SKILL.md da cópia do HUB foram alterados. São 4 arquivos em `<job>/Videos prontos/`, sem nenhum outro arquivo misturado:
- `video pronto para o TIKTOK.mp4`: completo com a marca da lupa, `logos\Logo sem fundo maior.png`, 17% da largura
- `video pronto para o YOUTUBE.mp4`: completo com a marca horizontal, `logos\Radar_do_Campo branco sem fundo.png`, recortada no alpha; desde 2026-09-24 pequena no canto superior direito (28% da largura, centro 80%/9,7%), como o usuário usa
- `<nome>-completo-sem-legenda.mp4`: base de edição, SEM marca (desde 2026-09-24; antes tinha a lupa e ela vazou para o YouTube dele)
- `<nome>-limpo.mp4`

**Why:** ele posta o mesmo vídeo no TikTok e no YouTube com marcas diferentes para as redes não cruzarem os arquivos.

A prévia 720p e o `_checagem_marca.png` vão para `_montagem/render/`. Com 4 encodes o render passa de 10 min: rode em background.

Também em 2026-09-24 o usuário trocou a regra da narração: **não acelerar mais a 1,2x**. `narracao.py` agora mantém a velocidade original e corta os silêncios entre trechos. Cada pausa de 0,15s ou mais (a -35 dB) vira uma respiração de 0,12s (`--manter`), e o `pausas.json` guarda essas emendas como pontos de corte. Testado na narração do Faiq: 65,3s viraram 60,8s, sem nenhuma fala perdida. Cuidado: pedir `-ac 2` ao ffmpeg numa narração mono abaixa 3 dB (0,707); o script decodifica em mono e duplica o canal no numpy.

Folha de contato com `-ss` antes do `-i` engana sobre onde começa cada foto em slideshow de TikTok. Para escolher o ponto de entrada, confira com seek preciso (`-ss` depois do `-i`) e olhe o primeiro quadro do shot renderizado.

**How to apply:** ao montar, use os scripts dessa pasta. Ofereça reempacotar o `.skill` com as correções para o usuário gravar.

Em 2026-09-25 o usuário pediu que as skills de garimpo e montagem **só gravem dentro de `Videos prontos\Shorts\<vídeo>\`**, sem jogar arquivo em pasta geral (logos, Sons, Músicas, HUB, raiz de Videos prontos, Downloads = só leitura). A regra entrou nos dois SKILL.md do HUB, e os scripts ganharam a trava `scripts/pasta_job.py`, que aborta saída fora do job. Os `.skill` foram reempacotados (backup `.skill.bak-2026-09-24`). O único resto antigo fora do Shorts é `HUB\Claude\remotion-radar\` (da skill antiga, não usado mais).

Também em 2026-09-25 (Rayan x Austrália) o usuário pediu que **só a marca do canal apareça**: marcas de perfis/emissoras (WAMO, ge, sportv, ESPN, Paramount+) devem ser escondidas. O `prep_shots.py` ganhou a chave `"tampar"` na EDL (delogo no fonte, por clipe), e a regra entrou no SKILL.md (Passo 5 + bloqueio).

Em 2026-09-25 o usuário definiu que **a imagem sempre faz loop, mesmo quando o roteiro não tem frase-ponte**: o último plano é o trecho do mesmo clipe logo antes da entrada do primeiro (a saída do último é igual à entrada do primeiro). No vídeo do Rayan: fecha no close da sportv em 9,5–11,69s e abre em 11,69s. A regra está no SKILL.md (Passo 3 item 4 + bloqueio), e o `prep_shots.py` barra a EDL que não emenda (`"sem_loop": true` desliga).

**Atualização 2026-09-25 (fim do dia):** a pedido do usuário, instalei as versões novas pelo claude.ai (Configurações > Habilidades > Fazer upload > Substituir): `montagem-de-video` e `garimpo-de-videos` instaladas agora = cópia do HUB (com trava de pasta, limpar_marcas, loop visual). As versões antigas ficam no histórico de versões da skill. Se a skill carregada voltar a mostrar Remotion, reinstalar a partir do HUB.

**2026-09-25 (vídeo Matheuzinho):** o usuário reclamou que a clonagem do `limpar_marcas` ("tampar") deixa **"reflexo muito aparente"**. Regra: esconder marca de terceiro **por enquadramento** (zoom + cx/cy deixando a marca fora). "Tampar" só sobre fundo liso (ex.: logo em card branco com `"de": "cor"`). Se o enquadramento não tira a marca sem cortar o assunto, troque o trecho. Ele também viu uma **piscada no começo**: o shot atravessava um corte interno da fonte (1 quadro de outra cena), e outros shots pegavam fade para preto de compilado. Criei `_montagem/scripts/checa_bordas.py` no job, que acusa corte de cena e quadro escuro dentro do trecho de cada shot. Rode antes de renderizar. Também corrigi no `prep_shots.py` do job o `setsar=1` e as tags de cor fixas: SAR diferente entre shots (1756:1755) reiniciava os filtros no meio do vídeo. Levar essas duas correções para a cópia do HUB/skill.

**2026-09-27 (após a comparação do Palermo/Diogo):** HUB atualizado e `.skill` reempacotado (backup em `versao-nova-2026-09-22\_bak-2026-09-27\`). O `prep_shots.py` ganhou `keys`/`tracking "segue"` (zoom acompanhando o lance), `recorte`, `borrar` (ferimento, borda suave), `destaque` (seta/círculo vermelho), `flashforward` (gancho pode repetir quadros) e aviso de upscale > 2,6x. O modo "faixa" com fundo desfocado foi removido, porque o usuário rejeitou. O SKILL.md ganhou a 3ª referência (Palermo/Diogo), o item 9 (gancho) e as regras de replay fechado no gol e de fonte pela resolução efetiva. LUFS e altura da legenda ficam com o usuário, que ajusta no CapCut. Em 2026-09-27 instalei pelo claude.ai (Personalizar > Habilidades > + Adicionar > Fazer upload de habilidade > "Fazer upload e substituir"): montagem-de-video v12, que inclui também as correções do Matheuzinho, que nunca tinham subido. A garimpo-de-videos instalada já era igual à do HUB. Ver [[referencia-montagem-palermo-diogo]].

**2026-09-27 (noite, após Kane e Atlético-GO):** HUB atualizado (backup em `versao-nova-2026-09-22\_bak-2026-09-27-noite\`), cópia local sincronizada e as 3 skills reenviadas pelo claude.ai: montagem-de-video v13, garimpo-de-videos v4, garimpo-de-temas v7. A `garimpo-de-temas` agora também tem cópia no HUB. O que mudou:
- **Montagem:**
  - `narracao.py` com padrão -30dB/0,12s.
  - `render_final.py`: só "fala sumida" bloqueia; correlação baixa virou aviso (falso alarme do limitador). A imagem de checagem da marca é gerada antes da checagem de áudio.
  - Novo `grade.py`.
  - SKILL.md: itens 10 (fato = imagem do fato) e 11 (prévia de suspense) do Passo 3, gancho no auge, dissolve não detectado, renumeração de shots, medir marcas e card de início, legenda queimada da fonte, nomes que o Whisper erra.
- **Garimpo de vídeos:** Passo 3c (fatos de outras datas e coletiva transcrita), filtro de data, vlog do YouTube.
- **Garimpo de temas:** resumo de busca não é fonte; Data FIFA.

Ver [[montagem-gancho-e-contexto-literal]].

**2026-09-29 (tarde, v15 e v16):** v15 = lições do Vini x Austrália ([[referencia-edicao-vini-penalti]]). v16 = velocidade: o usuário notou montagens de 1h30–2h. Causa: cada correção refazia os 4 arquivos (~20 min cada) + revisão inteira. Agora: `render_final.py --rascunho` (só TikTok ultrafast em ~2 min, em `_montagem/render/rascunho_tiktok.mp4`) → `revisao.py` no rascunho (inteira na 1ª vez, `--shots N,M` depois de correção) → 4 arquivos UMA vez no fim; presets slow→medium (render_final, prep_shots, posfx). Backups em `_bak-2026-09-29-vini\`.

**2026-09-29 (noite, após o Endrick) — INSTALADO:** HUB atualizado (backup `_bak-2026-09-29-endrick\`) e enviado pelo claude.ai: montagem-de-video (claude.ai v18 = "Versão v17" no SKILL.md) e garimpo-de-videos (claude.ai v5). Entrou: keys com t relativo ao shot (prep_shots converte keys absolutas), ponte de continuação no loop_final, números por extenso automáticos na legenda, folhas `bordas_XX.jpg` no revisao.py (viradas de shot a 30fps), isenção da meta de torcida para lance que só a TV pegou, checagem de versão HUB x instalada no Passo 0; no garimpo: tiktokuser:<channel_id>, reaproveitar inventário de outro job do mesmo jogo, marcar fusão na borda das janelas. Cuidado ao editar SKILL.md via python: "\v" em caminho vira tabulação vertical (0x0b).

**Antes disso, no mesmo dia:** a skill instalada NÃO tinha a v16 (sem `--rascunho`, revisão no final, presets slow): o HUB estava na frente. Montei usando os scripts e o SKILL.md do HUB. Se o usuário pedir "versão atualizada", compare com `diff -rq` o HUB e a pasta da skill instalada e use o HUB; ofereça reenviar o `.skill` pelo claude.ai.

**2026-09-29 (após Ronaldo e Arrascaeta):** HUB atualizado (backup em `versao-nova-2026-09-22\_bak-2026-09-29\`), `.skill` reempacotado e instalado pelo claude.ai como **montagem-de-video v14**. Entrou: 5ª referência, itens 12 (lance do gancho volta em take contínuo) e 13 (assistência/gol = lance com qualidade, senão close da emoção) do Passo 3, loop pelo rosto, fato emocional = rosto dele, transições `posfx.py` como padrão, 5º arquivo COM EFEITOS opcional, assinaturas pequenas de perfil, aviso da legenda do CapCut, e os scripts `posfx.py` (agora detecta shot rerenderizado), `compara_edicao.py` e `lado_a_lado.py`. Ver [[referencia-edicao-ronaldo-arrascaeta]].

**2026-10-01 (noite) — VERSÃO POR DATA + PASSO ZERO:** a versão agora é a data ("Versão 2026-10-01" na linha 8 do SKILL.md); o usuário confundia "v19" do claude.ai com "Versão v18" do texto (eram o mesmo). O SKILL.md tem um PASSO ZERO: ler a data do SKILL.md do HUB e, se for mais nova, seguir o HUB e usar os scripts dele. Toda atualização vai primeiro no HUB e muda a data. Entraram também: `guia_trilha.py` (chamado pelo render_final, grava "guia da trilha.txt"), `ignorar_bordas` por shot, `--shots` aceita "1 41", gancho = ação nunca objeto parado, "Aprendizado diário" + `_montagem/cmp/comparado.txt`. garimpo-de-temas ganhou Passo 0 (oferece comparar edições dele ainda não comparadas). Backup `_bak-2026-10-01-licoes\`. `.skill` de montagem e garimpo-de-temas reempacotados; INSTALADOS por mim pelo Chrome em 2026-10-01: montagem-de-video = claude.ai v20, garimpo-de-temas = claude.ai v8 (upload em claude.ai/customize/skills/new/upload, file_upload no input "Arquivo de habilidade", depois "Fazer upload e substituir").

**2026-10-01 (Argentina sem a camisa 10) — ENTREGA NOVA:** o usuário trocou o 4º arquivo. O `<nome>-limpo.mp4` (corte + narração) saiu e entrou **`<nome>-com-legenda-sem-marca.mp4`** (completo com cor + legenda + narração, SEM lupa e SEM "Radar Do Campo"). `render_final.py` (flag `--sem-limpo` virou `--sem-legsemmarca`; a checagem de marca ganhou a linha 4) e SKILL.md atualizados no HUB, `.skill` reempacotado (backup `_bak-2026-10-01-entrega\`). AINDA NÃO instalado pelo claude.ai: a skill carregada continua gerando o "limpo" até reenviar. Se a skill instalada ainda tiver o limpo, use o `render_final.py` do HUB.
Também: no PowerShell, `--shots 01,41` vira array e o `prep_shots` recebe "1 41" (o 01 é pulado sem aviso); passe entre aspas: `--shots "01,41"`.

**2026-09-30 (após o Raphinha cortado, montado do zero pelo usuário):** HUB atualizado (backup `_bak-2026-09-30-raphinha\`) e `.skill` reempacotados e INSTALADOS pelo claude.ai em 2026-09-30 (montagem-de-video = claude.ai v19, garimpo-de-videos = claude.ai v6): montagem-de-video "v18" (itens 15–20, `destaque` tipo `icone`, `legenda_capcut.srt` + cópia para "<job>/legenda para o CapCut.srt", ritmo 22–30/min, replay do lance-chave com `flashforward`) e garimpo-de-videos (Passo 3c: fato antigo pelo rival, lugar, infográfico, escudo; id completo no nome; inventário por lote; máx. 4 imagens/mensagem; cotas de escudo/lugar/infográfico são CONDICIONAIS, só quando o roteiro tem o elemento — o usuário perguntou se era obrigatório sempre). Ver [[referencia-edicao-raphinha-cortado]].

**2026-10-05 (limpeza de disco):** HUB "Versão 2026-10-05", com backup em `_bak-2026-10-05-limpeza\`:
- `render_final.py` manda os cortes regeneráveis para a Lixeira na entrega final e refaz o `corte_completo` pela lista se faltar.
- Novos scripts `fechar_videos.py` e `lixeira.py`.
- Nova seção "Espaço em disco" no SKILL.md.
- `.skill` reempacotado e INSTALADO pelo claude.ai no mesmo dia (instalada = HUB 2026-10-05). Ver [[limpeza-disco-registro-videos]].
