---
name: montagem-de-video
description: "Monta Shorts/Reels verticais de futebol do canal Radar do Campo a partir de roteiro + clipes garimpados + narração, no estilo das montagens feitas à mão pelo usuário: narração na velocidade original com as pausas entre trechos cortadas, protagonista sempre na tela, imagem literal de cada frase, gancho no pico do material, legenda karaokê (palavra falada em amarelo) no meio da tela, e entrega como rascunho editável no CapCut. Use sempre que o usuário pedir para montar, editar, cortar ou finalizar o vídeo de um roteiro, mesmo que ele não diga 'montagem'. Use também quando ele pedir para comparar/estudar a edição que ele fez (compara minha edição, vê o que eu mudei) ou para abrir a montagem no CapCut."
---

# Montagem de vídeo — Radar do Campo

**Versão 2026-11-07** (07/11: vídeo em movimento em todo shot, imagem parada só quando não existe vídeo do fato. 06/11 limpeza: a skill ficou só com as regras que valem hoje; a história de cada regra foi para `referencias/historico.md`. A entrega deixou de gerar os 2 MP4: sai a prévia, e o rascunho do CapCut é gerado sempre. Padrões fixos de SFX e P&B, sem meta de % de torcida, referências novas). A versão é identificada pela DATA.

## Passo zero — usar sempre a versão mais nova

A cópia-mestre fica no HUB: `C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\Claude\skills claude\versao-nova-2026-09-22\montagem-de-video\`. Antes de tudo, compare a linha "Versão" do `SKILL.md` do HUB com a desta cópia. Se o HUB for mais novo, siga o SKILL.md do HUB e use os `scripts/`, `assets/` e `referencias/` de lá. Diga ao usuário, em uma linha, qual versão está usando.

Monta o vídeo vertical 9:16 a partir de três insumos: roteiro, clipes brutos (da skill `garimpo-de-videos`) e a narração gravada. Buscar e baixar clipe é trabalho do garimpo; aqui é montagem.

## Padrões fixos (decididos com o usuário em 06/11/2026; não pergunte)

- **Entrega = rascunho do CapCut + prévia.** Ele refina e exporta o vídeo que vai ao ar do CapCut, e posta o mesmo arquivo nas 7 redes. Não existem mais os MP4 com-legenda/sem-legenda (`--mp4` só se ele pedir).
- **Rascunho do CapCut sempre**, no fim da entrega, sem perguntar (Passo 9). Se o CapCut estiver aberto, pergunte antes de fechar.
- **SFX:** 2 a 4 impactos (gancho, revelação, lance-chave), só na faixa SFX do rascunho do CapCut, ligada. Grave sempre o `_montagem/sfx.json`.
- **Flashback P&B:** só em foto antiga e em trecho de arquivo curto (até ~8 s), cobrindo o trecho inteiro (`flashback_in` no 1º shot, `flashback` em todos os seguintes até o último). Arquivo longo (> 8 s) ou vídeo de arquivo com placar/telão fica colorido.
- **Sem logo do canal** em nada (desde 21/10/2026) e **sem marca de terceiros** (Passo 5).
- **Duração final ≥ 60 s** e, de preferência, até ~66 s (Passo 1).
- **Vídeo em movimento em todo shot (regra do usuário, 07/11/2026):** a montagem é feita de vídeo, não de imagem. Quadro congelado, gráfico parado, card, foto ou close sem ação só entram quando não existe vídeo daquele fato, e por no máximo ~0,5–1 s. Coletiva = trecho em que a pessoa fala/gesticula; banco/reação = take em que ela se mexe; frase de regra/VAR = o lance ou o jogo andando, com o gráfico só na palavra. Antes do rascunho, meça o movimento do corte (Passo 8, item 0) e troque todo trecho parado por vídeo.
- **Torcida é preferência, não meta:** use filmagem de arquibancada quando ela pega o mesmo momento com o protagonista legível; transmissão quando só ela tem o lance ou o rosto.

## Referências que mandam

Em dúvida de estilo, compare com estes dois (folhas com `scripts/folha_contato.py`). Eles valem mais que qualquer número escrito aqui.
- **Bruno Duarte apagou** (08/10/2026, aprovado "perfeito", sem mudança): `Videos prontos\Shorts\Bruno Duarte apagou e ninguem viu\Videos prontos\Apagou em campo e os médicos foram atender outro jogador TIKTOK.mp4`. Modelo de incidente: gancho = prévia da queda; depois o evento inteiro em ordem, cada frase com o momento seguinte; zoom 1,2–1,6 seguindo a bola.
- **Argentina sem a camisa 10** (01/10/2026, publicado sem trocar nenhum quadro): `Videos prontos\Shorts\Argentina jogou sem a camisa 10\Videos prontos\Nenhum jogador da Argentina usou a 10 contra a Bolívia (e foi de propósito) TIKTOK.mp4`. Modelo de detalhe escondido: gancho em ação com a pista visual, revelação marcada.

## Onde trabalhar (regra fixa do usuário)

Tudo o que esta skill grava fica **dentro da pasta do vídeo**: `C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\Videos prontos\Shorts\<nome do vídeo>\` (`_montagem/`, `render/`, prévias, folhas, EDL, JSONs, scripts auxiliares).
- **Só leitura:** `logos\`, `Sons edição\`, `Musicas edição\`, `HUB Radar do Campo\`, a raiz de `Videos prontos\`, a pasta `Shorts\` e `Downloads\`. Material que chegou em `Downloads\`: copie para a pasta do vídeo.
- Temporário também vai para `_montagem/`, nunca `/tmp` ou scratchpad. Os scripts têm a trava `scripts/pasta_job.py`; não contorne.
- Nunca apague de vez: o que sai vai para a Lixeira (`scripts/lixeira.py`).

## Ambiente (Windows)

- `ffmpeg`/`ffprobe`/`python` 3.11 no PATH; `pip install faster-whisper opencv-python pillow numpy`.
- O `python` é o da Microsoft Store e **não enxerga a pasta da skill em `AppData\Roaming`**: copie `scripts/` e `assets/` para `<job>/_montagem/scripts` e `<job>/_montagem/assets` e rode as cópias.
- **Não use Remotion** (falha no seek de 1440x2560). Não use `/tmp` do Git Bash com o ffmpeg do Windows.
- Render longo: timeout alto (~590 s) ou background.
- **PowerShell:** passe listas entre aspas (`--shots "01,41"`), senão o shot 01 é pulado sem aviso. Valor negativo vai com `=` (`--ruido=-30dB`).

## Assets

Base: `C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\`

| Asset | Caminho |
|---|---|
| Efeitos sonoros | `Sons edição\` (`impact-cinematic-boom-352465.mp3`, `impacto cinema 2.mp3`, `impacto cinema 3.mp3`) |
| Trilhas | vêm do rascunho-modelo dele no CapCut (Passo 9) |
| Seta vermelha | `imagens edição\seta vermelha e  inclinada.jpg` |
| Fonte da legenda | `assets/Montserrat-Italic-VF.ttf` (render) e `assets/Montserrat-ExtraBoldItalic.ttf` (CapCut) |
| Prompt de títulos e tags | `assets/prompt_titulos_tags.txt` |
| Rascunhos do CapCut | `%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\` (o modelo é o mais recente que não começa com "Radar - " nem "_tmp") |

## Scripts (em `scripts/`)

| Script | Faz |
|---|---|
| `narracao.py` | corta as pausas (velocidade original), marca as emendas, transcreve palavra a palavra |
| `loop_final.py` | corta o fim da narração no começo da palavra que emenda com a abertura |
| `folha_contato.py` | folha de contato com tempo queimado |
| `grade.py` | quadros com grade de 10%: mede zoom/cx/cy e onde fica cada marca antes da EDL |
| `prep_shots.py` | audita a EDL e gera os shots 1440x2560 60fps + o corte; `keys`/`segue`, `recorte`, `borrar`, `destaque`, `flashforward` |
| `posfx.py` | transições do canal por shot (`fx`): `flash`, `flashback_in`, `flashback` |
| `legenda_karaoke.py` | faixa de legenda karaokê e `legenda_capcut.srt` com a grafia certa |
| `limpar_marcas.py` | clone de textura (`"tampar"`), só em fundo liso |
| `artes_print.py` | `card` (comentário) e `documento` (súmula com trecho realçado) |
| `revisao.py` | revisão a cada 0,1 s e folhas `bordas_XX.jpg` de cada virada |
| `render_final.py` | `--rascunho` para a revisão; sem a flag, o fechamento (prévia, checagem de áudio, `.srt`, guia da trilha, limpeza) |
| `guia_trilha.py` | `guia da trilha.txt` (chamado pelo `render_final.py`) |
| `capcut_projeto.py` | rascunho editável no CapCut a partir da EDL (Passo 9) |
| `compara_capcut.py`, `analisa_capcut.py`, `pares_quadros.py`, `compara_edicao.py`, `lado_a_lado.py`, `casar_fontes.py` | comparar a edição dele (`referencias/comparacao.md`) |
| `fechar_videos.py`, `lixeira.py` | fechar vídeos postados (`referencias/limpeza.md`) |
| `pasta_job.py` | trava de pasta |

Use os scripts: cada um carrega a correção de um erro que já aconteceu.

## Hub

Comandos e regras gerais: `referencias/hub.md`. Nesta skill:
- **Abertura (Passo 0):** id da linha `PAUTA DO HUB` do pedido ou de `<job>/_registro/pauta_hub.txt`; sem nenhum, `buscar` pelo protagonista. Rode `atualizar <id> --etapa montagem --pasta "<job>" --status trabalhando --nota "montagem começou"`.
- **Fim:** "Fechamento obrigatório: Hub" (última seção). A montagem nunca marca Pronto.

## Passo 0 — Insumos e conferências

Olhe a pasta do job inteira antes de perguntar: roteiro (`.txt`/`.docx`), `clipes/` com todas as subpastas (`apoio/`, `fotos/`, `_descartados/`, `_duplicados/`), `inventario.json` e a narração. Roteiro vazio: use o texto do chat e salve como `roteiro.txt`.

- **Narração:** o usuário gera no **Google AI Studio** (Gemini 2.5 Pro TTS, voz Puck). Não gere voz por conta própria; se faltar, peça.
- **Mais de uma narração na pasta:** transcreva todas, compare com o roteiro e use a que tem menos erro e nenhuma frase faltando. Diga qual e por quê.
- **Confira a narração contra o roteiro** (transcrição do Passo 1): liste cada palavra pulada ou trocada, com o tempo, **antes de montar**, para ele decidir se gera de novo. O AI Studio já pulou a frase de abertura e trocou "inédito" por "difícil".
- **Frase-ponte de loop:** o roteiro termina repetindo a abertura (ou em aberto, completando com a abertura). Se não tiver, sugira uma para ele colar no AI Studio.
- **Assinatura e opinião (desde 06/11/2026):** o roteiro fecha com uma frase de opinião e a assinatura do canal antes da frase-ponte. Elas são fala: não corte. A imagem delas é o protagonista (rosto/gesto), nunca torcida genérica.

## Passo 1 — Narração: cortar as pausas e medir

    python scripts/narracao.py "<job>/Narração.wav" "<job>/_montagem"

Não acelera. Cada pausa de 0,12 s ou mais (a −30 dB) vira uma respiração de 0,12 s (`--manter`); os silêncios das pontas saem. As emendas ficam em `pausas.json` e são os pontos de corte. Padrão `--ruido=-30dB --min-pausa=0.12`; com menos de uma emenda a cada 4 s, tente `--ruido=-28dB` ou `--min-pausa=0.10`. Confira que não sobrou silêncio ≥ 0,12 s.

**Duração (regra do usuário):** depois do corte de pausas e do loop, o vídeo **nunca fica abaixo de 60 s**. Abaixo disso, primeiro estique as respirações com a mesma narração (`--manter` até ~0,2 s; ganho = nº de emendas × diferença). Só se nem assim chegar a 60, pare antes da EDL e proponha uma frase (fato confirmado) para ele gerar de novo. Acima de 60 está aceito; passando de ~70 s, avise na entrega (no YouTube, 1:01–1:05 fica em 80–90% assistido; 1:14–1:21 cai para ~70%).

## Passo 1b — Loop no final

    python scripts/loop_final.py "<job>/_montagem"

Se a narração termina repetindo a abertura, corta no começo da palavra de emenda e a EDL usa a duração nova. Se termina em aberto (a abertura completa a frase), não há o que cortar e o script avisa. **O loop visual é obrigatório em todo vídeo** (Passo 3, regra 4), com ou sem frase-ponte.

## Passo 2 — Conhecer o material por trecho, não por clipe

1. Leia o `inventario.json`; parta das `janelas` de cada clipe.
2. Abra com `folha_contato.py` (passo 2–3 s) todo clipe sem janelas, inclusive os de `_descartados/` quando faltar material: o melhor trecho já esteve num clipe marcado como ruim.
3. Anote (clipe, entrada, saída, o que mostra): takes longos de arquibancada seguindo o lance; o protagonista identificável (rosto + número); o plano aberto do lance-chave; círculo/seta vermelha de destaque (estilo do canal, não sujeira); trechos com texto ou logo que um enquadramento tira.
4. React, compilado e legenda queimada descartam **o trecho**, não o clipe.
5. **Evento da noite anterior:** antes de montar, uma busca rápida no TikTok (2–3 termos) pelo momento do gancho: vídeos postados depois do garimpo já trouxeram o melhor gancho.
6. Junte folhas em mosaico e abra no máximo 2–3 imagens por mensagem (com mais, volta "[media removed: request limit]").

## Passo 3 — Regras de imagem

Classifique cada frase: **lance/ação**, **fato** (placar, retrospecto, título, declaração, data, número) ou **fala genérica**. Para cada uma, registre 2–3 candidatos e a escolha, com o porquê, na `nota` do shot.

**Gancho (0–3 s)**
1. **O gancho é o pico nº 1 do material** (Passo 3b), mostrado nos primeiros 0,5–1 s e cortado logo depois do contato, antes da consequência (`"flashforward": true`). Uma pessoa reconhecível fazendo algo: nunca a massa, nunca objeto parado, nunca a caminhada até o auge. Pico físico (golpe, empurrão, confusão) ganha da provocação. Entre duas entradas do mesmo take, a que mostra o pico mais cedo.
2. **Gancho literal à primeira frase:** a imagem de 0–2 s mostra o fato que a primeira frase diz. Fato com rosto ("fez essa cara quando…") = o rosto no instante do fato, com quem está ao lado.
3. **Movimento no gancho:** punch-in no contato (~1,0–1,2 → ~1,7) e/ou pan suave no sentido da ação. Nunca janela parada com ação acontecendo; nunca salto de lado no meio do shot. Sem `flash` no shot 1.
   - Filmagem de arquibancada do mesmo momento, na altura dos olhos e com o protagonista legível, ganha da câmera alta da TV. Protagonista pequeno e de longe na arquibancada: o replay fechado do mesmo instante.
   - Roteiro sobre um padrão (lesões, sequência de erros): o gancho é a imagem mais forte do padrão, não a mais recente.
   - Revelação visual (um número, um detalhe): abra no protagonista em movimento com a pista na tela, sem entregar a resposta.
   - Veredito na abertura ("foi cortado", "foi banido"): ícone do escudo riscado sobre a cabeça (`destaque` `icone`, `"riscar": true`, `tam` 0,15–0,18), também no shot de loop.

**Loop**
4. **Loop visual obrigatório:** o último shot é do mesmo clipe do primeiro e termina exatamente onde ele começa (tolerância de 1 quadro). Escolha para abrir um take com 2–3 s antes do ponto de entrada; o fim usa esses segundos. Loop por rosto ou ação, nunca por react/webcam nem com texto de fonte. O `prep_shots.py` barra se não emendar.

**Lance e ação**
5. **O lance do gancho volta inteiro, num take contínuo**, no momento dele na narração, do começo da jogada ao desfecho. Ângulos extras só depois, se sobrar narração. Picar o lance-chave em 4 cortes com círculo e replay foi recusado.
6. **Lance-chave legível:** plano que mostra o lance inteiro → círculo no protagonista (se existir) → close → 2º ângulo, em velocidade normal. "Plano aberto" não é plano em que a bola some: se ela e o protagonista ficam minúsculos, use o replay fechado seguindo a jogada em 2–4 ângulos. Take de torcida vale como prova do lance quando a jogada visivelmente bate com a narração (sequência, posição, placar no telão); plano genérico nunca é apresentado como o lance.
7. **Gol e pênalti narrados:** o shot começa antes do chute e termina na bola na rede. No payoff, quando o gancho já mostrou o lance, prefira outra fonte do mesmo lance (placar de TV na tela é prova, pode ficar).
8. **Assistência/gol do protagonista:** o lance com ele e a bola grandes; se só existir o lance com jogadores pequenos e parados, o close da comemoração dele. Nunca o lance ilegível.
9. **Ação inteira no quadro e até o pico:** `in` antes do início e saída ≥ 0,3 s depois do pico (contato, golpe, bola na rede). Zoom que corta o corpo de quem chuta é fechado demais. Se a frase é curta para a ação, estique para a frase seguinte (corte Tipo B), use 0,5–0,7x só na ação, ou mova o corte.
10. **Roteiro de incidente** (desmaio, lesão, briga): depois do contexto, o evento inteiro em ordem cronológica, cada frase com o momento seguinte do mesmo evento (jogada → contato → queda → no chão → reação → socorro → maca → substituição). Um clipe que cobre o evento todo vira a espinha; frase maior que o trecho, 0,6–0,75x no mesmo momento. Ferimento sempre desfocado (`borrar`).
11. **O detalhe que decide a polêmica** (a bola raspa ou não): um take só, em câmera lenta progressiva (ex.: 0,64x → 0,23x → 0,17x) até o contato, sem picar em lupa, círculo e seta.
12. **Prévia de suspense:** quando a revelação é visual, logo depois do gancho o replay que vai revelar, em câmera lenta (0,25–0,5x), com o círculo já no lugar, **cortado antes do detalhe** (1–1,5 s, `flashforward`). A revelação completa entra no momento dela.
13. **Lance-chave passado duas vezes** quando a narração fica nele por um bloco (~6–9 s): 1ª passada com seta/círculo, 2ª limpa ou mais fechada (`flashforward` na 2ª). A consequência na mesma frase segue no mesmo lance.
14. **"O mesmo lance" na frase:** pode repetir os mesmos quadros. Fora isso, nunca repita quadros (só o gancho e o replay duplo, ambos com `flashforward`).

**Fato e fala**
15. **Imagem literal de cada frase inteira:** a imagem diz a mesma coisa que a frase, de ponta a ponta; frase com duas ideias = duas imagens. A imagem nunca contradiz a frase. Prefira o literal mesmo em vídeo oficial (registre o risco de Content ID na nota).
16. **Fato narrado = imagem do fato, de qualquer data:** retrospecto, título, jogo anterior, declaração pedem o placar daquele jogo, a taça, o rival comemorando, a coletiva. Fato de outra data filmado da arquibancada vale mais, com o telão (placar e tempo) no quadro. Se o garimpo não trouxe, volte ao garimpo; nunca tape fato com torcida.
17. **Pessoa citada = a pessoa.** Fala sobre o protagonista ("lateral do Corinthians", "ele mesmo disse") = ele na tela. Instituição numa pergunta ou acusação = o rosto de quem a representa (Seleção → técnico; clube → técnico/presidente; arbitragem → o árbitro). Fato emocional do protagonista = o rosto dele naquele momento. Não mostre de rosto alguém que o roteiro não cita. Confira a identidade do rosto contra os quadros do lance; sem identidade confirmada, não entra.
18. **Falas genéricas** ("virou assunto", "quase ninguém percebeu"): o protagonista na tela (andando, reagindo). Torcida/estádio genérico só quando a frase fala literalmente da torcida ou do estádio.
19. **Ação descrita = a ação acontecendo**, não a consequência ("se machucou comemorando" = a comemoração, não a ambulância). Ação genérica ("voltou pra Barcelona") pode vir de outra data.
20. **Lugar nomeado = imagem do lugar** (de qualquer data, se o evento ainda não aconteceu). **Enumeração = um corte por item** (~0,5 s cada, na palavra). **Parte do corpo, gesto ou detalhe nomeado = punch-in nele** (corte seco para um quadro mais fechado do mesmo take, na palavra, `zoom` ~1,6–2,2). **Dado-resumo = infográfico de portal**, com punch-in no número; se ele limpou a arte num editor de IA, confira as letras pequenas.
21. **Pessoa nomeada entra na palavra:** o corte cai na palavra, mesmo antecipando a emenda em 0,2 s (Tipo B).
22. **Fala que cita documento ou post = o print real.** Súmula/comunicado: `artes_print.py documento --variantes` em tela cheia sobre o lance desfocado, com o trecho lido realçado em amarelo fora da faixa da legenda (48–60% da altura) e punch-in até o trecho. Story/post: o print com zoom lento. Post em outra língua lido pela narração: a tradução entre aspas, em Montserrat ExtraBold Italic branco com contorno, logo acima do original. Quando a súmula só narra um lance que existe em vídeo, mostre o lance.
23. **Comentários (desde 06/11/2026):** só entra comentário de pessoa relevante (jogador, técnico, clube, jornalista), ou quando a polêmica é o próprio comentário. Nesse caso: card real (`artes_print.py card`, `destaque` `icone`, `tam` ~0,86), nome do perfil desfocado se for anônimo, cards da reta final ficam até o último quadro, e o comentário que fecha entra sozinho e maior, com punch-in.
24. **Foto ou arte em tela cheia nunca parada:** zoom lento de ~1,0 para ~1,25 ou pan lento. Close de rosto = cabeça e ombros, com quem está ao lado; foto nítida do mesmo momento (photo mode do TikTok) com punch-in vale mais que vídeo fechado e mole.
25. **Expulsão/cartão:** o cartão levantado no quadro. **Objeto pequeno num plano aberto** (bola extra, objeto atirado): punch-in progressivo seguindo até ele ficar visível. **Relação no espaço** ("acertou a bola do jogo"): abra o quadro para caber os dois.

**Transições e trilha**
26. Corte seco entre shots. As únicas transições são as do `posfx.py`: `flash` só em virada, revelação e lance-chave (nunca no shot 1, em selfie, entrevista ou prévia que não seja o pico); `flashback_in`/`flashback` pela regra de P&B dos padrões fixos.
27. **Marque a revelação:** `"revelacao": true` no shot em que a história vira. O rascunho do CapCut põe a virada da trilha nele.

## Passo 3b — Plano de viralização (obrigatório antes da EDL)

Grave `_montagem/plano_viral.md` com:
1. **Mapa de impacto:** os 3–5 takes mais fortes do material (ação física, choque, multidão, contraste, rosto em emoção), com clipe, janela e o segundo exato do pico. O pico nº 1 abre o vídeo; os outros vão na revelação, no payoff e no último shot antes do loop. Nenhum pico fica fora sem justificativa.
2. **Tabela frase a frase:** frase inteira → o que ela afirma → a imagem literal → clipe e janela. Coluna vazia = volte ao garimpo (diga qual frase ficou sem imagem).
3. **Ações inteiras:** início e pico de cada ação, conferindo que o shot contém o pico.

Na entrega, diga em uma linha qual pico abriu o vídeo e onde ficaram os outros.

## Passo 4 — Ritmo

- ~22–30 planos por minuto (média ~2–2,5 s), com takes longos de 4–8 s e inserts de 0,5–1 s (reação, close, enumeração).
- **Cortes de conteúdo (Tipo A) caem nas emendas da narração** (±0,12 s). Troca de ângulo (Tipo B) é recurso para 2º ângulo ou palavra-chave, não cota.
- Menos cortes no trecho da prova: uma fonte só, em câmera lenta, vale mais que quatro shots curtos de fontes diferentes.

## Passo 5 — EDL, enquadramento e marcas

Escreva `edl.json` (formato no cabeçalho do `prep_shots.py`) e rode só a auditoria:

    python scripts/prep_shots.py "<job>/_montagem/edl.json" --saida "<job>/_montagem/render" --pausas "<job>/_montagem/pausas.json" --dur <duração> --so-checar

Ela confere limites, buracos, cortes fora de pausa, quadros repetidos, corte de cena e fade dentro de cada shot, planos/min e upscale. Corte de cena acusado: mude `in`/duração para ficar no trecho limpo. Alarme falso comprovado na folha a 30 fps: `"ignorar_bordas": true` **só nesse shot**. A auditoria não pega fusão (dissolve) de compacto: olhe a folha perto do fim de cada trecho de compacto. Depois rode sem `--so-checar`. **Tirar ou juntar um shot renumera todos:** renomeie os `shotNN.mp4` ou rode tudo de novo.

**Enquadramento:** tela cheia 9:16 sempre (faixa 16:9 com fundo desfocado foi recusada). A janela é a maior 9:16 possível (`zoom` 1,0); `cx`/`cy` posicionam; `keys` `[[t, cx], [t, cx, cy]]` com **t relativo ao início do shot** fazem a janela acompanhar o lance (o script converte keys absolutas e avisa); `tracking: "segue"` usa fluxo óptico (confira, ele se perde em amontoado); `"recorte"` tira a borda de repost antes do 9:16. Assunto no centro da janela, não encostado na borda. Escolha a fonte do mesmo momento em que o assunto ocupa mais pixels, não o arquivo maior; repost de baixa resolução com o momento certo vale mais que momento genérico em 1080.

| Tipo de plano | Zoom | Observação |
|---|---|---|
| Escala ou lugar (lotado, vazio, multidão, estádio, placa, cartaz) | 1,0 (máx. 1,3) | Fonte vertical do mesmo momento, ou pan lento num panorama. Nunca uma fatia com zoom |
| Lance coletivo | 1,0–1,4 | Zoom forte só em detalhe ou rosto |
| Jogador seguindo a bola, incidente | 1,2–1,6 | `keys` seguindo a ação |
| Punch-in em parte do corpo, gesto, rosto, dado lido | 1,6–2,2 | Corte seco ou progressivo, na palavra |
| Objeto pequeno num plano aberto | progressivo até o objeto ficar visível | Pode passar de 2,2x de upscale; avise na entrega |
| Shot que só fica limpo com zoom > 1,6 por causa de texto, logo ou tela dividida | — | Volte ao garimpo atrás da versão limpa do mesmo vídeo; só aproxime/tampe se não existir, e avise |

**Upscale:** alvo ≤ 2,2x (acima fica mole; a auditoria avisa a partir de 2,6x). Para tirar marca, acima de ~2,4x troque o trecho.

**Ferimento/sangue:** `"borrar": [[t, x, y, larg, alt], ...]` (fração do quadro final, animado), cobrindo a área toda, sem retângulo nem vermelho nas bordas.

**Seta ou círculo vermelho** no protagonista em quadro confuso: `"destaque": [{"tipo": "seta"|"circulo", "x", "y", "ang", "tam", "t0", "t1"}]`; segure o plano enquanto a narração descreve o que a seta mostra. Seta pode acompanhar o protagonista com keyframes. Confira a posição no shot renderizado.

**Marcas de terceiros (perfis, emissoras, portais) não podem aparecer em nenhum quadro.** O placar/relógio da transmissão pode ficar quando prova o lance. Em ordem:
0. **Meça antes da EDL** com `python scripts/grade.py <saida.jpg> "<clipe>|<seg>|<rótulo>" ...` em cada fonte, incluindo o rodapé, os primeiros 5 s (card de abertura de post, que cai no shot de loop) e os trechos que você vai reenquadrar. Assinaturas pequenas (@perfil, nomes de página) contam.
1. **Enquadrar sem a marca** (padrão): zoom leve + `cx`/`cy`. Logo atravessada no meio: enquadre acima dela com `keys` acompanhando.
2. **A ação vale mais que o quadro sem logo:** se só o enquadramento com a ação inteira deixa uma logo pequena, `"borrar"` retangular só sobre ela. Texto queimado sem fonte alternativa: idem. Confira cada caixa de `borrar` de perto no shot renderizado (já escapou 1% acima da logo).
3. **Trocar o trecho** quando o enquadramento que tira a marca corta o assunto.
4. `"tampar"` (clone) só em fundo liso (card branco, céu, gramado uniforme), nunca sobre torcida, rosto, camisa ou placa (vira "reflexo aparente"). Nunca `delogo`.
- Legenda queimada da fonte no meio da tela que não dá para tirar: avise o intervalo na entrega.

## Passo 6 — Legenda

    python scripts/legenda_karaoke.py --palavras "<job>/_montagem/palavras.json" --roteiro "<job>/roteiro.txt" --dur <duração> --saida "<job>/_montagem" --quadro <um quadro 1440x2560 do corte> --previa "<trecho de um bloco>"

- Karaokê: a palavra falada em amarelo (#FAFE05), as outras brancas; tempo do Whisper sobre a narração já cortada (nunca estime). Uma linha, 2–3 palavras; o bloco fecha em ponto, vírgula e dois-pontos. Montserrat ExtraBold Italic, ~3,1% da altura, contorno + sombra preta. **Centro a 54% da altura** (ele não mexeu na legenda do rascunho do CapCut em nenhuma das últimas rodadas).
- **Grafia certa é trabalho nosso:** corrija o `palavras.json` (guarde o original como `palavras_whisper.json`) — nomes estrangeiros, nome que vira duas palavras (junte num item), números. Grave o texto corrigido como `roteiro_legenda.txt` e passe todos os nomes por `--nomes`. Minúsculas, com nome próprio em maiúscula; números como no roteiro (o script converte algarismos 0–999 para extenso; placar e ano, à mão).
- Abra a `previa_legenda.png` e leia a lista de blocos.
- O `legenda_capcut.srt` sai junto (vai para a raiz do job como `legenda para o CapCut.srt`); serve se ele montar do zero no CapCut.

## Passo 7 — Rascunho, revisão e fechamento

**Ordem:** rascunho → revisão (Passo 8) → corrige → rascunho → revisão só dos shots mexidos → … → fechamento **uma vez**.

    python scripts/render_final.py --render "<job>/_montagem/render" --narracao "<job>/_montagem/narracao_final.wav" --legenda "<job>/_montagem" --saida "<job>" --nome <apelido> --rascunho

gera `_montagem/render/rascunho.mp4` (cor saturação 1,18 / contraste 1,12 + legenda + narração, encode rápido, ~2 min). Com a revisão limpa, o fechamento é o mesmo comando **sem** `--rascunho`:
- prévia 720p `_montagem/render/<apelido>-preview.mp4`;
- checagem áudio x narração: **FALA SUMIDA** bloqueia; "correlação baixa" é só aviso (o limitador achata a voz) — transcreva o rascunho com faster-whisper e compare com o roteiro antes de entregar;
- `legenda para o CapCut.srt` e `guia da trilha.txt` na raiz do job;
- limpeza: os cortes e o rascunho (regeneráveis) vão para a Lixeira; shots, clipes, EDL e prévia ficam.

Não gera MP4 final (o vídeo que vai ao ar sai do CapCut). `--mp4` gera os antigos com-legenda/sem-legenda em `Videos prontos/`, só se ele pedir. Correção depois da entrega: volte ao rascunho, revise os shots mexidos, rode o fechamento e regere o rascunho do CapCut.

## Passo 8 — Revisão antes de entregar

0. **Movimento (07/11/2026):** meça a diferença entre quadros do rascunho e liste os instantes parados:

       ffmpeg -i "<job>/_montagem/render/rascunho.mp4" -vf "fps=10,signalstats,metadata=print:key=lavfi.signalstats.YDIF" -f null - 2>&1 | grep -o "YDIF=[0-9.]*"

   YDIF abaixo de ~1 por mais de 0,5 s seguido = trecho parado (quadro congelado da fonte, gráfico, foto). Troque por vídeo do mesmo fato; se não existir, encurte para ≤ 1 s e diga na entrega. No Tarkowski (07/11) saíram parados: Lampard no banco, gráfico do VAR por 3 s, Ballard congelado 2 s, Moyes quase estático; ele reclamou que "ficou só imagem".
1. **Revisão a cada 0,1 s (regra do usuário), no rascunho, antes de qualquer entrega:**

       python scripts/revisao.py "<job>/_montagem/render/rascunho.mp4" "<job>/_montagem/revisao" --edl "<job>/_montagem/edl.json" [--shots "18,20"]

   Na 1ª passada, o vídeo inteiro; depois de correção, só os shots mexidos (e os vizinhos, se a duração mudou; renumerou, tudo de novo). Percorra todas as folhas, sem amostrar. Em cada quadro: **centro** (o assunto que a nota prometeu está no quadro?), **legenda** (diz o que está sendo falado e não cobre mão, bola ou rosto?), **topo, cantos e rodapé** (sobrou marca de terceiro, mancha de clone, logo do canal?), **viradas** (quadro preto, flash de outro lance?), **últimos quadros** (emendam no primeiro?).
2. **Bordas:** percorra todas as `bordas_XX.jpg` (cada virada a 30 fps). O passo de 0,1 s pula quadro solto de outra cena. Correção padrão: avançar a entrada ou recuar a saída 0,15–0,3 s. O clarão no 1º quadro de shot com `flash` é esperado.
3. **Checagem de viralização:** o 1º segundo mostra o pico nº 1? Cada ação aparece até o pico? Algum zoom escondeu a escala que a frase promete? Alguma imagem contradiz a frase ou cobre com torcida uma frase que nomeia pessoa, preço ou data?
4. **Às cegas:** dá para entender o lance-chave sem pausar? O final emenda no começo?

Qualquer defeito volta à EDL.

## Passo 9 — Rascunho editável no CapCut (sempre)

Ele refina e exporta do CapCut. Gere o rascunho **no fim de toda entrega, sem perguntar**:
1. Confira se o CapCut está aberto (`tasklist //FI "IMAGENAME eq CapCut.exe"`). Fechado: gere. Só o nosso rascunho aberto: `taskkill //F //IM CapCut.exe` e gere. **Projeto dele aberto: pergunte antes de fechar.**
2. `status <id> trabalhando --texto "Gerando rascunho do CapCut"` no Hub.
3. Rode, de dentro de `<job>/_montagem`, com `PYTHONIOENCODING=utf-8`:

       python scripts/capcut_projeto.py "<job>" --nome "Radar - <título>" [--modelo "<rascunho-modelo>"]

O rascunho parte do modelo dele (trilhas com a posição dele, impacto "Dramatic"; logos do modelo ficam de fora) e deixa **tudo nativo e editável**: cada shot é o clipe bruto com corte, velocidade, escala/posição e keyframes (no **tempo da fonte**); cor gravada nas cópias em `_montagem/capcut_clipes/`; flash em PNG (faixa FLASH); P&B pelo filtro do CapCut (faixa FLASHBACK); `borrar` como cópia com máscara Retângulo + Desfocar (faixa DESFOQUE); setas/círculos (SETAS); cards (CARDS/CARDS2/CARDS3); legenda karaokê com a fonte da entrega a 54%; narração; SFX do `sfx.json` ligado. Trilha principal a 0,12, 2ª trilha a 0,09 até ~1 s antes do fim, e a virada no shot `"revelacao"` (sem a marca, cai em 44,6 s e o script avisa).

Para conferir, abra no CapCut (computer-use: "CapCut", "capcut.exe" e "File Explorer"; a home abre no monitor VX-215X e o editor no 27G2G4) e veja 3–4 pontos (gancho, um flash, um card, o P&B). Diga que não assistiu o vídeo inteiro no CapCut. Detalhes e pegadinhas: `referencias/capcut.md`.

## Bloqueios: não entregue quando

- algum trecho parado (YDIF < ~1) passa de ~1 s, ou foi usado quadro/foto/gráfico parado onde existe vídeo do mesmo fato;
- a revisão a cada 0,1 s não foi percorrida no rascunho (inteira na 1ª passada; os shots mexidos em cada correção) ou achou defeito não corrigido;
- algum corte de conteúdo cai fora de pausa da narração;
- o último plano não emenda no primeiro;
- aparece marca de terceiro ou logo do canal em qualquer quadro, ou sobrou mancha de clone;
- a auditoria acusou corte de cena ou fade dentro de um shot;
- um plano genérico foi apresentado como prova de lance específico;
- o gancho não é o pico nº 1 do mapa, ou falta o `plano_viral.md`;
- uma ação foi cortada antes do pico;
- uma frase que nomeia pessoa, preço ou data foi coberta com torcida/estádio genérico, ou a imagem contradiz a frase;
- plano de escala/lugar com zoom > 1,3 ou upscale > 2,2x; assunto fora do quadro ou ilegível;
- ferimento sem desfoque, ou desfoque com retângulo/vermelho aparente;
- duração diverge da `narracao_final.wav` em mais de 0,2 s, falta áudio (FALA SUMIDA) ou há quadro preto nas viradas;
- vídeo final abaixo de 60 s;
- a frase cita documento ou post e a imagem não é o print real, ou o realce cai embaixo da legenda;
- clipe sem janelas no inventário não foi aberto (Passo 2);
- falta a prévia ou o rascunho do CapCut (salvo se o projeto dele estava aberto e ele pediu para não fechar).

## Entrega

- Mostre a prévia (`_montagem/render/<apelido>-preview.mp4`) com `SendUserFile`.
- Diga que o rascunho "Radar - <título>" está no CapCut.
- Resuma em poucas linhas: duração, planos/min, qual pico abriu e onde ficaram os outros, decisões que valem discussão, o que ficou mais fraco e por quê, nomes próprios da legenda para conferir, avisos (shot com logo desfocada, legenda queimada da fonte, upscale alto, duração acima de ~70 s). Não prometa desempenho.
- **Prompt de títulos e tags (sempre):** preencha `assets/prompt_titulos_tags.txt` — `{PROTAGONISTAS}`, `{JOGO}`, `{FATO}`, `{DURACAO}`, `{PAUTA}` (id do Hub), `{PASTA}` (pasta do job), `{FONTES}` (os @perfis/emissoras dos clipes usados na EDL, tirados do `inventario.json`, sem repetir) e `{ROTEIRO}` (texto limpo, sem rótulos, com a grafia certa) — grave em `<job>/prompt titulos e tags.txt` e mostre inteiro num bloco de código.
- Rode o "Fechamento obrigatório: Hub".

## Comparar a edição dele (só quando ele pedir)

Até 06/12/2026 vale a pausa de obra: não ofereça comparação. Quando ele pedir ("compara minha edição"), siga `referencias/comparacao.md`. Se virar regra, ela **substitui a regra antiga no lugar dela** neste arquivo, com a data; o caso vai para `referencias/historico.md`. Nada de histórico no SKILL.md.

## Espaço em disco

Clipes só saem quando ele pedir ("fecha os vídeos antigos"): `referencias/limpeza.md` (`fechar_videos.py`, vídeos com mais de 15 dias, Lixeira de 150 GB).

## Fechamento obrigatório: Hub (fim da entrega)

Depois de gravar o prompt de títulos e tags e gerar o rascunho do CapCut:

    python "C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\radardocampohub1.0\scripts\hub.py" --fonte montagem-de-video atualizar <id> --etapa montagem --pasta "<job>" --arquivo "Prévia=<job>\_montagem\render\<apelido>-preview.mp4" --arquivo "Rascunho no CapCut=Radar - <título>" --arquivo "Legenda para o CapCut=<job>\legenda para o CapCut.srt" --proximo-prompt-arquivo "<job>\prompt titulos e tags.txt" --status aguardando --status-texto "No CapCut · esperando títulos e tags" --nota "montagem entregue: <duração>s"

Se o rascunho do CapCut não foi gerado (projeto dele aberto), troque o `--status-texto` por "Esperando refinamento no CapCut" e tire o arquivo do rascunho.

A montagem **nunca marca Pronto**: quem passa para Pronto é a `titulos-e-tags`. Correção depois da entrega: rode a mesma linha de novo (arquivo de mesmo caminho é trocado).

Feche a resposta com: `Hub: <título> em Montagem, no CapCut esperando títulos e tags.` Se o `hub.py` falhar, diga o erro nessa linha e siga.
