---
name: garimpo-de-videos
description: "Usar quando o usuário fornece um roteiro de vídeo e pede para encontrar e baixar clipes-fonte em múltiplas redes (TikTok, Instagram, X, YouTube, Facebook, Kwai, Threads) para cada parte do roteiro — tanto os lances em si quanto apoio/contexto (torcida, estádio, banco, reação) — priorizando filmagem da torcida (vídeos longos de arquibancada, vlogs do jogo) em vez de transmissão oficial, para evitar Content ID. Entrega os arquivos baixados e um inventário com os TRECHOS aproveitáveis de cada clipe, pronto para a skill montagem-de-video."
---

# Garimpo de clipes — Radar do Campo

**Atualizada em 2026-10-31:** todo garimpo termina com o "Fechamento obrigatório: Hub" (fim do arquivo): clipes ligados, pasta e o prompt de montagem na pauta. **Antes, 2026-10-30:** a pauta do Hub acompanha o garimpo (seção "Hub", Passos 1, 8 e 9). **Antes, 2026-10-18:** prints do que o roteiro cita (comentário, súmula, story), começar pelos links da pesquisa, nada de clipe de canal concorrente, arquivos de trabalho fora da raiz.

Objetivo: dado um roteiro, entregar uma pasta cheia de material bruto baixado **e mapeado por trecho**, pronta para a `montagem-de-video`. Não é lista de links: é arquivo em disco + inventário.

## O que a montagem do usuário ensinou

Na montagem do Carrascal (Flamengo x Bragantino), o usuário montou o vídeo à mão com este mesmo material. **Mais da metade do vídeo dele saiu de um único clipe que o garimpo baixou e nunca abriu**: um "react" de 96s em que o cara aparece falando na câmera no começo e no fim, mas de 3s a 57s são 54 segundos limpos filmados da arquibancada, seguindo o protagonista. O garimpo tinha deixado o clipe em `_extras` como "não verificado", e a regra "rejeitar vídeo de reação" teria descartado o clipe inteiro de qualquer jeito.

Ele também aproveitou trechos que o garimpo tinha marcado como inúteis:
- o plano aberto de uma transmissão com **círculo vermelho** marcando o jogador (o círculo é estilo do canal, não sujeira);
- o que vem **depois** dos 4s de legenda queimada de um clipe da ESPN.

Daí saem as três regras centrais desta skill:
1. **Todo clipe baixado é aberto e mapeado.** Nada fica "não verificado".
2. **Avalia-se o trecho, não o clipe.** React, compilado, legenda queimada e marca d'água descartam o trecho ruim; o resto do clipe continua valendo.
3. **Filmagem longa de torcida é o material mais valioso**, e deve ser caçada de propósito.

## Modo padrão: garimpo enxuto (desde 08/10/2026)

Em 08/10/2026 (Bruno Duarte, Botafogo 1x2 Vasco) o usuário pediu "não exagerar nos tokens". O vídeo montado com esse material saiu "perfeito", e ele quer que o garimpo seja assim **todo dia**. O modo enxuto é o padrão. Só use o garimpo completo, com as 7 redes e o mapeamento de todo clipe, quando ele pedir ("garimpo completo", "todas as redes").

1. **Reaproveite antes de buscar.** Se existe em `Shorts\` outra pasta do mesmo jogo, leia o `inventario.json` dela e copie o que serve. Depois liste, por parte do roteiro, só o que falta.
2. **Busque pouco e no alvo.** Comece pelo TikTok, no Chrome logado, com 4–6 buscas focadas: o lance-chave, o protagonista, cada gol ou lance citado e `<time> x <time> arquibancada <estádio>`. Junte os links com JS num `localStorage` depois de cada busca e rolagem. Vá para outra rede **só para a parte que ficou sem material** (coletiva na íntegra → YouTube; post que só existe no Instagram).
3. **Filtre antes de baixar.** Rode `yt-dlp --skip-download --print "%(uploader_id)s|%(id)s|%(duration)s|%(width)sx%(height)s|%(title).70s"` em lote e corte o óbvio antes do download: outro jogo ou idioma, slideshow de fotos, react sem trecho útil.
4. **Verifique em mosaico.** Gere a folha de cada clipe com miniaturas pequenas (largura 70–120, passo 2–3 s) e junte de 10 a 12 clipes numa imagem só, com o nome do arquivo em cada linha. Abra no máximo 2–3 imagens por mensagem; com mais que isso, voltam "[media removed: request limit]". A folha fina (`--passo 0.3–0.6`) fica só para o lance-chave.
5. **Mapeie as janelas do que cobre o roteiro.** Os clipes que cobrem uma parte do roteiro ganham janelas detalhadas no `inventario.json`. O compacto que só repete um ângulo já mapeado fica em `clipes/`, citado na entrega como "repete ângulo, sem janelas". Isso não é o "não verificado" do Carrascal: o clipe foi aberto no mosaico.
6. **Durante a montagem, busca extra pontual.** Se uma frase ficar sem imagem (em 08/10, o Colidio), faça uma busca rápida só para ela, em vez de um garimpo amplo antes.

Na rodada de 08/10 foram 5 buscas no TikTok e 46 clipes baixados. 24 foram mapeados, 9 descartados e 2 eram duplicados. Isso bastou para um vídeo aprovado sem mudanças. Continue entregando o placar das cotas do Passo 2, dizendo o que faltou.

## Hub: a pauta acompanha o trabalho (desde 30/out/2026)

Pedido do usuário em 30/out/2026: "todo o processo de escolher os roteiros, garimpagem e montagem do vídeo sincronizado certinho com as pautas e a esteira do Hub". Cada vídeo é uma **pauta** no Hub (radardocampo.online → Vídeos → Pautas), e a esteira anda: pauta → roteiro → garimpo → montagem → pronto → no ar. Esta skill avisa o Hub pelo script `hub.py`:

    python "C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\radardocampohub1.0\scripts\hub.py" --fonte garimpo-de-videos <comando>

- **Comandos:** `buscar [termo]`, `ler <id>`, `criar "<título>" [--etapa E] [--notas-arquivo F] [--roteiro-arquivo F] [--refs-json F] [--proximo-prompt-arquivo F]`, `etapa <id> <etapa> [--nota "..."]`, `atualizar <id> [--roteiro-arquivo F] [--notas-arquivo F] [--pasta P] [--arquivo "rótulo=caminho"] [--titulo T] [--proximo-prompt-arquivo F] [--etapa E] [--nota "..."]`, `prompt <id> <arquivo> [--etapa E]` (só o prompt do próximo passo), `clipe <id> <url> [--tipo clipe|referencia] [--trecho gancho|lance|torcida|reacao|contexto] [--inicio 0:12] [--fim 0:25] [--nota "..."]`, `clipes <id> <lista.json>`. Saída em JSON.
- **Achar o id da pauta:** procure a linha `PAUTA DO HUB: <id>` no pedido (o botão "Copiar prompt" do Hub e os prompts de chat novo das skills trazem essa linha). Sem ela, rode `buscar "<jogador ou time>"` e use a pauta que bater; se nenhuma bater, crie uma.
- **Passe o id adiante:** todo prompt para chat novo que esta skill gerar leva `PAUTA DO HUB: <id>` na primeira linha depois do pedido.
- **O prompt do próximo passo vai para a pauta (desde 31/out/2026).** O prompt de chat novo que esta skill entrega é gravado na pauta com `--proximo-prompt-arquivo <arquivo>` (ou `prompt <id> <arquivo>`). O Hub mostra o bloco "Prompt para o próximo passo" com botão de copiar, e ele cola num chat novo direto de lá.
- **O fluxo só termina com o "Fechamento obrigatório: Hub"** (última seção deste arquivo). Pedido de 31/out/2026: a esteira anda sozinha quando cada fluxo termina, sem depender de alguém lembrar de chamar o `hub.py`.
- **O Hub nunca trava o vídeo.** Se o `hub.py` der erro (sem internet, senha ausente, pauta excluída), diga em uma linha na resposta e siga o trabalho. Nunca peça para o usuário consertar o Hub no meio da rotina.
- Arquivo temporário para o `hub.py` (roteiro, lista JSON) segue a regra de pastas desta skill.

## Onde trabalhar (regra fixa do usuário)

Tudo o que esta skill grava fica **dentro da pasta do vídeo**: `C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\Videos prontos\Shorts\<nome do vídeo>\`. Se a pasta ainda não existir, crie-a com o título do vídeo. Clipes, fotos, folhas de contato (`frames/`), listas de download, logs, `.baixados.txt`, `inventario.json` e scripts auxiliares ficam todos nela.

- **Só leitura:** `logos\`, `Sons edição\`, `Musicas edição\`, `HUB Radar do Campo\`, a raiz de `Videos prontos\`, a própria pasta `Shorts\` e `Downloads\`. Nunca grave nem mova arquivo para elas.
- Arquivo temporário também vai para a pasta do vídeo, não para `/tmp`, scratchpad ou pasta geral.
- **Raiz do job limpa:** listas de links, logs de download, metadados (`tt_meta.txt`), scripts auxiliares e transcrições soltas vão em `<job>/_registro/`. Na raiz ficam só o roteiro, `inventario.json`, `.baixados.txt`, `clipes/` e `frames/`. No Andreas (18/out) foi assim; no Bernal, no mesmo dia, ficaram ~25 arquivos `log_dl*.txt`, `l_*.txt` e `tt_*.txt` soltos na raiz.
- `scripts/folha_contato.py` usa a trava `scripts/pasta_job.py` e aborta se a saída estiver fora de `Shorts\<vídeo>\`.

## Ambiente (máquina local Windows)

- `yt-dlp`: `C:\Users\bruno\AppData\Local\Microsoft\WinGet\Packages\yt-dlp.yt-dlp_Microsoft.Winget.Source_8wekyb3d8bbwe\yt-dlp.exe`. Se sumir: `winget install --id yt-dlp.yt-dlp`.
- `ffmpeg`/`ffprobe`/`python` 3.11 + `pip` no PATH.
- Navegador: para **busca no TikTok use o Claude in Chrome** (sessão logada). O browser embutido cai em CAPTCHA no TikTok, e CAPTCHA não se resolve. Carregue as ferramentas do Chrome com um único ToolSearch `select:`.
- `scripts/folha_contato.py` (nesta skill) gera folha de contato com o tempo queimado. No Windows o `drawtext` do ffmpeg precisa de `fontfile` explícito; o script já cuida disso.
- Não use `/tmp` no Git Bash para arquivos lidos ou escritos pelo ffmpeg/Python do Windows (os caminhos não batem). Use a pasta do job.

### Download e cookies

- **TikTok baixa sem cookies** (o yt-dlp resolve o desafio sozinho). Instagram também baixou sem cookies na maioria dos posts (11 de 14 no último job).
- Com o Chrome aberto, `--cookies-from-browser chrome` falha ("Could not copy Chrome cookie database"). Tente primeiro sem cookies; se falhar, tente `firefox`/`edge`; só então peça para fechar o Chrome.
- A URL de busca do Kwai (`/search/video?searchKey=`) está devolvendo "sem conexão"; use `https://www.kwai.com/discover/<termo>` (funcionou em out/2026).
- Post que não baixa (TikTok da ESPN com "IP bloqueado", X da DAZN Portugal com erro 403 no Bernal x Yamal): procure o mesmo vídeo repostado por outro perfil antes de marcar `[BAIXAR MANUALMENTE]`.

## Passo 1 — Pasta do job e roteiro

O usuário normalmente já deixou a pasta do vídeo com o roteiro em `.txt`/`.docx`. Liste a pasta e leia o roteiro do arquivo antes de pedir qualquer coisa. Se o arquivo existir mas estiver vazio (só os cabeçalhos), avise e use o roteiro do chat.

**Pedido que já traz contexto e links** (o prompt que a `garimpo-de-temas` gera no Passo 11b: contexto confirmado, "o que cada trecho precisa de imagem", "posts que já achei"): grave o roteiro em `ROTEIRO.txt` e **baixe primeiro os posts listados**. Eles já foram conferidos na pesquisa. Use a lista numerada de imagens como as partes do Passo 2, e as observações (canal concorrente, buscas úteis) como regra do job.

Estrutura:

    <pasta do job>/
      clipes/            <- tudo que tem pelo menos um trecho aproveitável
      clipes/apoio/      <- apoio/contexto
      clipes/fotos/      <- fotos nítidas do protagonista (Passo 3b)
      clipes/_descartados/   <- só o que não tem NENHUM trecho aproveitável
      clipes/_duplicados/
      inventario.json

Não existe mais `_extras` "não verificado": clipe baixado é clipe verificado.

**Hub, no começo do garimpo:** ache o id da pauta (seção "Hub"); sem pauta, crie com `criar "<título>" --etapa garimpo --roteiro-arquivo ROTEIRO.txt`. Grave o id em `<job>/_registro/pauta_hub.txt` (a montagem lê dali) e rode `atualizar <id> --etapa garimpo --pasta "<job>" --nota "garimpo começou"`. Rode também `ler <id>`: os **clipes salvos pela extensão do Chrome** (`kind: clipe`, com trecho e início/fim) contam como "posts que já achei": baixe primeiro e use as janelas marcadas como ponto de partida do mapeamento.

## Passo 2 — Quebrar o roteiro e definir as cotas

Quebre em partes (gancho, cada lance citado, fechamento). Para cada parte anote a alegação: quem, o quê, e se é lance específico, contexto ou **fato de outra data** (jogo anterior, retrospecto, título, final, declaração da semana, coletiva). Confirme os fatos do jogo (placar, minuto, autores dos gols, lance-chave) numa busca rápida antes de garimpar. Se o roteiro divergir dos fatos, avise o usuário.

**Cotas mínimas (critério de "terminei"):**

| Item | Mínimo |
|---|---|
| **Vídeo longo de torcida do jogo** (≥20s de arquibancada, de preferência seguindo o protagonista) | 2 clipes, se existirem |
| Trechos do protagonista identificável (rosto + nome/número no mesmo quadro) | 2 |
| Plano aberto do lance-chave (campo inteiro visível) | 1 |
| Trechos por parte com lance específico | 2 distintos |
| Trechos por parte de contexto | 1 |
| Apoio (Passo 3) | 8 |
| Ângulos diferentes do lance principal | 3 |
| **Fotos nítidas do protagonista** (Passo 3b) | 3 |
| **Fato de outra data citado no roteiro** (Passo 3c) | 1 trecho por fato |
| **Entrevista/coletiva citada** (Passo 3c), completa e transcrita | a íntegra, se existir |
| **Filmagem de torcida do fato de outra data** (Passo 3c), com placar no telão se houver. *Só se o roteiro citar fato de outra data* | 1 por fato, se existir |
| **Lugar citado** (estádio/cidade, qualquer data se o evento não aconteceu). *Só se o roteiro nomear um lugar* | 1 |
| **Infográfico do dado-resumo** (portal: 365Scores, ge, OneFootball). *Só se o roteiro trouxer um número/histórico* | 1 por dado, se existir |
| **Escudo PNG sem fundo**. *Só se o roteiro abrir com veredito ("foi cortado", "foi demitido")* | 1 |
| **Print do que o roteiro cita** (comentário, súmula/documento, story ou post). *Só se o roteiro citar* | 1 por citação |

As cinco últimas linhas são **condicionais**: se o roteiro não tem aquele elemento, a cota não existe e não entra no placar do Passo 8. Não busque escudo, lugar ou infográfico "por garantia".

Se uma cota não fechar, diga qual e por quê. Não entregue pela metade em silêncio.

## Passo 3 — Apoio

Busque, do mesmo jogo sempre que possível, pelo menos 8 destes: torcida cantando/mosaico/bandeirão; torcida reagindo ao gol; estádio por fora/chegada do ônibus; entrada dos times/hino; banco/técnico; **close do protagonista** (comemoração, concentração, andando em campo); placar/telão; aquecimento/bola parada; ângulo alternativo do lance.

Salve em `clipes/apoio/apoio_<categoria>_<rede>.mp4`. O apoio só precisa ser do jogo e do time certos e estar limpo no trecho que vai ser usado.

## Passo 3b — Fotos nítidas do protagonista

Quando o roteiro é sobre a história de um jogador, e não sobre um lance, o vídeo precisa de closes nítidos dele. Vídeo de celular raramente tem isso. No Faiq Bolkiah, o usuário foi buscar por conta própria uma foto de estúdio do jogador no Chonburi para "é capitão da seleção", porque o garimpo só tinha fotos pequenas, com logo, dentro de compilados.

- Busque **pelo menos 3 fotos** em que o rosto ocupe boa parte do quadro, com **1080px ou mais no lado menor**, de preferência uma por fase citada no roteiro (clube atual, seleção, clube antigo). Fontes, em ordem:
  1. perfis oficiais do clube e do jogador (Instagram/X/Facebook: foto de anúncio, dia de jogo)
  2. matérias de sites de notícia
  3. busca de imagens
- Rejeite foto com texto/arte do autor por cima, marca d'água grande ou pôster editado.
- **Confirme a identidade:** nome na legenda do post ou da matéria, ou número/camisa batendo. Família real, elenco e evento têm gente parecida. No Faiq, o rapaz de farda branca do banquete provavelmente era o príncipe Abdul Mateen, não o Faiq.
- Salve em `clipes/fotos/foto_<fase>_<fonte>.jpg` e registre no `inventario.json` com `tipo: "foto"`, a URL de onde veio e o sinal que confirma que é ele.

## Passo 3c — Fatos de outras datas e falas citadas

A montagem não pode cobrir fato com torcida genérica (regra do usuário, set/2026). No Atlético-GO, o roteiro dizia "o Dragão não ganhava do Goiás em 2026. Quatro clássicos, uma derrota, três empates. E ainda viu o rival ser campeão goiano". O garimpo só tinha trazido material do jogo do dia, a montagem tapou com torcida, e o usuário recusou ("sem contexto, mostra muita torcida"). Foi preciso voltar ao garimpo no meio da montagem. Por isso, para **cada fato de outra data** do roteiro:
- baixe o compacto daquele jogo ou evento (YouTube: `<time> x <time> <competição> <ano> melhores momentos`, `<time> campeão <competição> <ano>`, `final <competição> <ano>`) e marque a janela com **placar final na tela**, a comemoração do rival, a **taça** e a festa do título;
- confira a `upload_date` e o placar do vídeo contra o fato. O mesmo confronto se repete todo ano: a busca "England vs Spain Wembley vlog" trouxe vlogs de 2016 e 2018 misturados com os de 2026.
- **cace também a filmagem de torcida do fato antigo**, não só o compacto. No Raphinha (set/2026), a lesão contra a França em março: eu só achei transmissão e reposts ruins buscando "raphinha lesão frança amistoso". O usuário achou um vídeo da arquibancada, com o **telão mostrando o placar e o tempo**, buscando pelo **rival envolvido no lance**: "Mbappé lesiona Raphinha" (@contos0.5), e em inglês "how Raphinha got injured vs France" (@wolusfcb). Varie: `<craque rival> lesiona <protagonista>`, `<protagonista> injury vs <seleção> <mês>`, `<protagonista> machucado <estádio>`. Filtre pelo id do TikTok daquela época (os posts de março/2026 começavam em 7622…).

Para **lugar citado** ("fora do jogo contra a Índia, em Calcutá"; "o estádio onde…"): baixe 1–2 clipes do estádio ou da cidade, de **qualquer data**, se o evento ainda não aconteceu. O usuário usou um estádio de Calcutá lotado num evento de dezembro/2025 (@ihrapaaz). Busca: `<estádio> <cidade>`, `<cidade> football stadium`, `<cidade> torcida`.

Para **dado-resumo** do roteiro ("quarta lesão em um ano", "terceira vez com a Seleção", "X gols em Y jogos"): procure o **infográfico** que os portais postam no Instagram/X (365Scores, ge, OneFootball, SofaScore, Opta) e baixe a imagem na maior resolução. O usuário usou a arte "ALERTA LIGADO" do 365Scores, com o corpo e as lesões marcadas. Anote a marca do portal (a montagem enquadra sem ela) e se há texto miúdo: quando ele passa a arte num editor de IA para tirar a marca e ampliar, a IA deforma as letras pequenas ("COSA", "ZORA DO MONSO", "AMISTERO").

Para **veredito na abertura** ("foi cortado", "foi demitido"): baixe o **escudo do clube ou da seleção em PNG sem fundo** (Wikimedia Commons, ≥512px) para `clipes/fotos/escudo_<time>.png`. A montagem põe o escudo riscado com um X sobre a cabeça do protagonista (`destaque` `icone`), como o usuário fez com a CBF no Raphinha.

Para **texto citado no roteiro** (Bernal x Yamal, 18/out/2026), a montagem mostra o print real (`artes_print.py`):
- **Comentários** ("nos comentários chamaram ele de nova princesa…"): abra no Chrome o post onde eles estão (o roteiro ou o prompt dizem qual; no Bernal, o post da ESPN Deportes com 268 mil curtidas), ache cada comentário citado e salve um print da tela com o nome, o texto e as curtidas legíveis. Arquivo: `clipes/fotos/print_comentario_<palavra>_<rede>-<perfil>.jpg`.
- **Súmula, acta ou comunicado:** busque no X `acta <jogador>`, `súmula <jogador>`, `<árbitro> acta`. Jornalistas e perfis de arbitragem postam o print no mesmo dia; no Bernal veio do @alexferj_. Precisa estar legível na frase que o roteiro lê.
- **Story ou post de desculpas:** o story some em 24h, mas jornais (Marca, AS) e perfis no X repostam o print. Busque `<jogador> story disculpas` / `<jogador> pede desculpas story`.
- Registre no `inventario.json` com `tipo: "print"`, a URL e qual frase do roteiro ele prova.

Para **falas citadas** (coletiva, zona mista, "ele disse que…"):
- procure a **íntegra**, não só o recorte viral (no Atlético-GO: coletiva completa de 139s no @diariodegoias);
- **transcreva com faster-whisper** e anote no inventário o segundo exato de cada frase usada no roteiro. Foi assim que "doido varrido" (0–7s) e "corto o pescoço na hora certa" (70,5–75s) viraram fala confirmada e com tempo marcado, em vez de citação de matéria.

## Passo 4 — Critérios de seleção (por trecho)

- **Priorize a filmagem, não a conta.** Filmagem da torcida (celular, arquibancada, áudio ambiente) em vez de transmissão. Transmissão repostada por fã tem o mesmo risco de Content ID.
- **Vídeo longo de torcida vale ouro.** Vlog do jogo, "fui no Maracanã", "gravei o jogo todo", perfis que filmam a partida inteira da arquibancada: é disso que a montagem faz a base do vídeo, em takes de 4–8s. Compilado de *transmissão*, esse sim, serve de confirmação e 2º ângulo, não de base.
- **Descarte o trecho, não o clipe.** Registre como janela ruim: webcam de react, legenda do autor queimada no meio da ação, pôster/card editado, narração com legenda, quadro de IA. O resto do clipe entra no inventário.
- **Mesmo lance em versão limpa (regra de 29/out/2026, vídeo do Giay):** para cada trecho, procure o mesmo lance em mais de uma postagem (fonte original, repost sem texto, outra rede) e prefira a que não tem texto, logo, moldura ou tela dividida por cima. Clipe que só fica bem enquadrado com zoom forte para fugir da sujeira não é o escolhido se houver versão limpa. No Giay vários shots ficaram ruins e perderam qualidade porque entrou a primeira versão achada. Se não houver versão limpa, anote no inventário.
- **Texto queimado recortável:** se o texto ocupa uma faixa longe da ação (topo, rodapé, canto), anote `"recortavel": true` com a faixa. A montagem tira com zoom.
- **Círculo, seta ou destaque desenhado** sobre o jogador: mantenha e anote (`"anotacao": "circulo vermelho no protagonista"`). O canal usa esse recurso.
- **Overlay de transmissão** (placar, logo da emissora) não é legenda. O placar/tempo de jogo é prova de lance: anote onde ele aparece.
- **Resolução:** trecho abaixo de 720 de largura só entra se não houver alternativa para o mesmo momento; anote. Mas **momento único vence resolução**: no Raphinha, o usuário usou reposts 720x960 porque eram os únicos com ele andando no intervalo visto da arquibancada e com o close dele com o médico. Repost ruim com o momento certo fica no inventário, com a janela marcada.
- **Repost com legenda mentirosa:** o "raphinha injury today" de 29/set (@0.0.0.0.0.0.919) era a lesão da Copa (camisa 11, junho), não a da Austrália (camisa 10). Confirme o jogo pelo **uniforme e pelo número** (na Copa ele usou a 11 e, nos amistosos de setembro, a 10 com braçadeira), não pela legenda nem pela data do post.
- **Nunca use clipe de canal concorrente do mesmo formato** (@Onfirefut e parecidos: storytelling narrado de futebol). Não baixe vídeo deles nem como 2º ângulo: é o vídeo de outro canal do nicho, e o usuário pediu para não usar no Bernal x Yamal.
- **Vídeo gerado por IA:** desconfie de uniforme errado e closes de estúdio. O `tt_el.banquillo54` do Bernal x Yamal tinha a camisa do Barça errada e foi descartado. E confira de quem é o lance: o `tt_ffc.teixeira`, achado na busca "bernal", era sobre o Martinelli.
- Risco de Content ID: YouTube é o mais agressivo; Instagram/Facebook são rigorosos com transmissão e tranquilos com filmagem real; TikTok, X e Kwai são os mais tolerantes.

## Passo 5 — Buscar e baixar (baixe cedo, verifique depois)

Ordem: **TikTok → Instagram → Kwai → X → Facebook → YouTube Shorts → Threads**. Verificação definitiva é depois do download, com quadros reais; thumbnail engana.

Consultas: varie nome completo → sobrenome/apelido → hashtag do time → tipo de lance + time. **Sempre inclua buscas para filmagem longa de torcida:**
- `<time> x <time> arquibancada`, `<jogador> visto da arquibancada`, `<time> <estádio> gravei`, `fui no <estádio> <time>`, `<time> x <time> vlog`, `POV torcedor <time>`;
- abra o perfil de quem postou filmagem de arquibancada: costuma ter vários vídeos do mesmo jogo.
- **Jogo da Seleção: liste o perfil @canalwamo logo no começo** (filma da arquibancada, 1080x1920). Se `yt-dlp https://www.tiktok.com/@perfil` falhar com "Unable to extract secondary user ID" (Endrick, set/2026), pegue o `channel_id` de um vídeo do perfil (`yt-dlp --skip-download --print "%(channel_id)s" <url de um vídeo>`) e liste `tiktokuser:<channel_id>` com `--flat-playlist`.
- **Mesmo jogo, outro roteiro:** se já existe em `Shorts\` a pasta de outro vídeo do mesmo jogo, leia o `inventario.json` dela e copie (não mova) os clipes que servem, antes de buscar de novo. No Endrick, o job do Vini x Austrália já tinha a confusão, o gol do Bruno e todo o apoio do estádio.
- **Take de torcida do momento do gancho:** antes de encerrar, garanta um vídeo da arquibancada do lance que vai abrir o vídeo. No Endrick (set/2026) o usuário achou sozinho o bolo inteiro filmado da arquibancada num post intitulado "Endrick 1 vs 11 vini reaction" (@trent_1228): a legenda falava de reação, não da briga. Busque também por `<jogador> 1 vs 11`, `<jogador> vs <seleção> fight`, `<jogador> reaction`, `<time> brawl stands` e abra os posts de título genérico dos ids do dia.
- **Fato de outra data dito de passagem também conta** ("depois do título da Copa do Mundo", "campeão em julho"): traga a imagem do título (campeões no túnel, taça, festa), não só o jogo do dia. No Modric (set/2026) o usuário buscou sozinho a seleção da Espanha no túnel da Copa, em Los Angeles.
- **O protagonista do placar, de perto:** se o roteiro abre num placar ("a Espanha meteu 4 a 1"), traga o craque do jogo em gesto marcante filmado da arquibancada (Yamal sentado na bola, @football.360.1). Foi o gancho que o usuário escolheu.
- **Vlog de torcedor no YouTube** (`<time> x <time> <estádio> vlog`, `matchday vlog`) costuma ter o jogo inteiro filmado da arquibancada, com o lance-chave de trás do gol (Kane: o vlog "JK On Tour" tinha todos os gols e o pênalti). Baixe em 1080p e mapeie os letreiros do autor, que dizem minuto e autor de cada gol.

**Filtrar pela data:**
- **TikTok:** o número do vídeo cresce com o tempo. Anote o id de um post sabidamente do dia e descarte ids bem menores (no Kane, ids iniciados em 7481… eram do caso Julián Álvarez de 2025; os do jogo começavam em 7689…).
- **YouTube:** rode `yt-dlp --skip-download --print "%(upload_date)s|%(title)s"` antes de baixar.

**Coleta de links no TikTok:** um `javascript_tool` que junta os `a[href*="/video/"]` da página com a legenda do card e guarda num `localStorage`, rodado depois de cada busca+rolagem, junta 100+ links em poucos minutos sem abrir vídeo por vídeo. O Claude in Chrome às vezes cai no meio de um batch: comece o download do que já foi coletado em background enquanto reconecta.

URLs:
- TikTok: `https://www.tiktok.com/search/video?q=<query>` (no Chrome logado)
- Instagram: `https://www.instagram.com/explore/search/keyword/?q=<query>`
- X: `https://x.com/search?q=<query>%20filter%3Avideos&f=live`
- Facebook: `https://www.facebook.com/search/videos/?q=<query>`
- YouTube: `https://www.youtube.com/results?search_query=<query>` + filtro Shorts

Extraia os links com `read_page` (`filter: interactive`).

Download:

    yt-dlp -f "bv*+ba/b" -S "res,fps,vcodec:h264,ext:mp4:m4a" --merge-output-format mp4 --download-archive "<job>/.baixados.txt" -o "<job>/clipes/<nome>.%(ext)s" <url>

Se falhar: uma vez com outro navegador em `--cookies-from-browser`, uma vez com o repost do mesmo clipe em outra rede. Só então marque `[BAIXAR MANUALMENTE]`.

**Nome do arquivo com o id completo:** `tt_<perfil>_<id completo do vídeo>.mp4` (ex.: `tt_dobe699_7691017567284022549.mp4`), nunca só os 6 últimos dígitos. O usuário salva o que baixa como `<id>.mp4`. No Raphinha, ele baixou de novo o vídeo do @dobe699 que o garimpo já tinha, porque não reconheceu `tt_dobe699_022549.mp4` como o mesmo post.

## Passo 6 — Deduplicar

1. Agrupe por duração (±0,5s) + resolução (`ffprobe`).
2. Confirme com aHash do quadro do meio (Hamming ≤ 6 = mesmo vídeo).
3. Repost com corte, logo ou letterbox diferente o hash não pega; confira na folha de contato.

Mantenha a cópia de maior resolução e sem marca d'água; mova as outras para `_duplicados/` e registre qual ficou.

## Passo 7 — Verificar TODOS os clipes e mapear os trechos

Para **cada** clipe baixado, sem exceção:

0. **Grave o inventário a cada lote**, não só no fim. Depois de cada 8–10 clipes mapeados, atualize o `inventario.json` e mande ao usuário uma parcial de 3–5 linhas: o que já está mapeado por parte do roteiro. No Raphinha, o garimpo passou de 1h abrindo folhas e o usuário assumiu a montagem com os clipes baixados, mas sem nenhuma janela registrada.
   **Abra no máximo 4 folhas de contato por mensagem** (largura 160–200 e até ~48 quadros cada). Com 6–7 imagens de uma vez, várias voltaram "[media removed: request limit]" e tiveram que ser reabertas, o que dobrou o tempo. Se esse aviso aparecer, reabra de 2 em 2.
1. Folha de contato do clipe inteiro: `python scripts/folha_contato.py <clipe> <saida.jpg> --passo 2` (ou 1 em clipes curtos).
2. Divida o clipe em janelas: onde começa e termina cada trecho limpo, e o que atrapalha nos outros.
3. Nas janelas relevantes, refine com `--passo 0.3` para achar o momento exato do lance.
4. **Marque fusão e corte perto da borda da janela.** Compacto, edit e post de emissora costumam ter dissolve, corte de 1 quadro ou fade nas pontas de cada trecho; a montagem só descobre isso na revisão. Na folha fina (`--passo 0.3`), olhe os 0,5s de cada ponta da janela e, se houver, feche a janela antes (ex.: `"in": 42.75` em vez de 42.2 porque 42.2–42.7 é fusão) e anote em `"obs"`. No Endrick, 4 correções da revisão final vieram disso.
5. Para cada janela, anote: o que mostra, fonte (torcida/transmissão), status (`confirmado` só com sinal visível: nome/número, placar/tempo compatível ou ação inequívoca; senão `ambiente`), protagonista visível ou não.

Grave em `inventario.json`, um registro por clipe com as janelas (exemplo ilustrativo, no formato do react de 96s do job Carrascal):

    {"arquivo": "clipes/tt_vinizzera.mp4", "rede": "tiktok", "url": "https://...",
     "w": 1080, "h": 1920, "fps": 30, "dur": 96.7,
     "janelas": [
       {"in": 3.0, "out": 12.0, "fonte": "torcida", "status": "confirmado", "protagonista": true,
        "sinal": "mesma jogada que aparece na transmissao",
        "mostra": "jogada do 1o tempo vista da arquibancada, take continuo"},
       {"in": 15.0, "out": 25.0, "fonte": "torcida", "status": "confirmado", "protagonista": true,
        "mostra": "contra-ataque ate o chute no goleiro, um take so"},
       {"in": 42.0, "out": 57.0, "fonte": "torcida", "status": "ambiente", "protagonista": true,
        "mostra": "Carrascal 15 andando/posicionando em campo, filmado da arquibancada"}
     ],
     "descartar": [{"in": 0.0, "out": 3.0, "motivo": "webcam do react"},
                   {"in": 58.0, "out": 96.7, "motivo": "webcam do react"}],
     "recortavel": null, "anotacao": null, "crop_barras": null}

Esse arquivo é o que a `montagem-de-video` lê primeiro. Sem janelas, ela precisa refazer tudo.

## Passo 8 — Entregar

Organize por parte do roteiro. Em cada linha: **[BAIXADO]** ou **[BAIXAR MANUALMENTE]** · rede · torcida/transmissão · confirmado/ambiente · arquivo **e janela** (ex.: `tt_vinizzera.mp4 3–12s`) · o que mostra.

Destaque no topo os **vídeos longos de torcida** encontrados e quanto tempo limpo cada um tem: eles definem a montagem. Liste o apoio por categoria. Feche com o placar das cotas do Passo 2, dizendo o que faltou e por quê.

**Hub, na entrega:** ligue à pauta os clipes que cobrem o roteiro, um por trecho mapeado (até ~30), com `clipes <id> <job>/_registro/hub_clipes.json`. Cada item: `url` (a fonte original), `kind: "clipe"`, `role` (gancho, lance, torcida, reacao ou contexto, pela parte do roteiro), `start_s`/`end_s` da melhor janela, `title` (o que mostra) e `note` (nome do arquivo em `clipes/` e a parte do roteiro). O resto (pasta, nota e prompt de montagem) vai no "Fechamento obrigatório: Hub" (fim deste arquivo). A etapa continua garimpo; quem muda para montagem é a montagem.


## Passo 9 — Prompt para montar num chat novo (SEMPRE, no fim do garimpo)
Desde 21/out/2026: toda entrega de garimpo termina com um prompt num bloco de código, pronto para colar num chat novo (Claude ou Antigravity como plano B):
1. `Use a skill montagem-de-video para montar o Short deste roteiro do canal Radar do Campo.` e, logo abaixo, `PAUTA DO HUB: <id>`.
2. **PASTA DO JOB:** caminho completo da pasta com os clipes e o inventário.
3. **ROTEIRO (narração final)** e onde está/estará o áudio da narração (o usuário gera no AI Studio).
4. **CONTEXTO DO TEMA:** jogo, data, placar final, nomes completos, o lance minuto a minuto.
5. **MAPA TRECHO → CLIPE:** para cada frase, arquivo + janela (ex.: `tt_x.mp4 3–12s`) e o que mostra; marcar qual é o gancho (pico do material) e qual fecha o loop.
6. **O QUE FALTOU:** trechos sem imagem e a alternativa sugerida (foto, print, close).
7. **OBSERVAÇÕES:** marcas d'água a tampar, clipes de concorrentes a evitar, mínimo de 60s.

Grave esse mesmo texto em `<job>/_registro/prompt_montagem.txt`: ele vai para a pauta no fechamento, e o botão do Hub copia ele.

## Erros já cometidos (não repetir)

- Bernal x Yamal (18/out/2026):
  - Deixar ~25 arquivos de trabalho (logs, listas, metadados) soltos na raiz do job (use `_registro/`).
  - Não buscar no Instagram nem os perfis que o prompt pediu para procurar (ESPN México, @desde.lagrada.yt), só porque os 3 posts dados já tinham baixado. O que o pedido lista é cota.
  - A torcida do Betis no gol do Abde não apareceu: só a transmissão. Listar o perfil de quem filmou outros gols da arquibancada (@d77aguilar) cobriu os gols do Barça. Liste esse tipo de perfil logo no começo.

- Deixar 14 clipes em `_extras` "não verificados"; um deles era a base do vídeo que o usuário montou.
- Rejeitar o clipe inteiro por ter react, legenda queimada ou círculo de destaque.
- Tratar vídeo longo como suspeito por padrão; filmagem longa de torcida é o melhor material.
- Entregar só links porque o `yt-dlp` falhou, ou desistir no primeiro erro de download.
- Entregar só lance, sem apoio.
- Entregar o mesmo vídeo duas vezes vindo de redes diferentes.
- Confirmar lance por thumbnail em vez de quadros do arquivo baixado.
- Usar o browser embutido no TikTok (cai em CAPTCHA).
- Atlético-GO (set/2026): garimpar só o jogo do dia quando o roteiro citava retrospecto e título do rival. A montagem teve que parar e voltar ao garimpo (Passo 3c).
- Confiar em vídeo de busca sem conferir a data: o mesmo confronto aparece em vlogs de anos diferentes.
- Aceitar vídeo gerado por IA como bastidor real (Kane: "De la Fuente e Kane no vestiário", da conta theMattAI). Desconfie de cena de vestiário/bastidor que nenhum veículo mostrou.
- Modric e Endrick (comparados em 02/out/2026): o usuário baixou sozinho o gancho dos dois vídeos (o Yamal sentado na bola; o bolo do Endrick filmado da arquibancada), a imagem do título da Copa (túnel em Los Angeles) e o gol do Yamal na transmissão aberta até a rede.
- Raphinha cortado da Seleção (30/set/2026):
  - Buscar o fato antigo (lesão contra a França) só com "raphinha lesão frança": não achei a filmagem da arquibancada com o telão, que o usuário achou com "Mbappé lesiona Raphinha". Busque pelo rival envolvido no lance e em inglês (Passo 3c).
  - Não trazer imagem do lugar citado (Calcutá) nem o infográfico do dado-resumo (365Scores): o usuário foi buscar os dois (Passo 3c).
  - Passar de 1h abrindo folhas de 6–7 em 6–7 imagens ("request limit"), sem gravar inventário nenhum: o usuário montou sem as janelas (Passo 7, item 0).
  - Nomear com os 6 últimos dígitos do id: ele não reconheceu o arquivo e baixou de novo (Passo 5).

## Fechamento obrigatório: Hub (último passo de todo garimpo)

Na entrega, depois do prompt do Passo 9 e antes de encerrar a resposta:

1. Ligue os clipes: `clipes <id> <job>/_registro/hub_clipes.json` (Passo 8).
2. Confira que `<job>/_registro/prompt_montagem.txt` tem o prompt do Passo 9 exatamente como foi entregue, com a linha `PAUTA DO HUB`.
3. Rode:

       python "C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\radardocampohub1.0\scripts\hub.py" --fonte garimpo-de-videos atualizar <id> --etapa garimpo --pasta "<job>" --proximo-prompt-arquivo "<job>\_registro\prompt_montagem.txt" --nota "garimpo: N clipes mapeados; faltou: ..."

4. Feche a resposta com uma linha: `Hub: <título> em Garimpo, N clipes ligados, prompt de montagem salvo.` Se o `hub.py` falhar, diga o erro nessa linha e siga (seção "Hub").

Se ele pedir mais clipes depois, repita 1 a 3 (os links já ligados são pulados, e o prompt novo substitui o anterior).
