---
name: titulos-e-tags
description: "Use quando o usuário fornece um roteiro pronto de vídeo de futebol (Radar do Campo) e pede opções de título, texto de capa e tags do YouTube, ou pede mais ideias de texto de capa / texto para combinar com a foto da capa."
---

# Títulos e Tags — Radar do Campo

**Versão 2026-11-06** (legenda do TikTok pensada para a busca, crédito das imagens, fim do "ninguém percebeu, mas…" como padrão; Hub resumido, comandos em `referencias/hub.md`). Histórico em `referencias/historico.md`. A cópia-mestre fica no HUB (`versao-nova-2026-09-22\titulos-e-tags\`).

Fluxo em duas etapas para transformar um roteiro pronto em título, texto de capa (thumbnail) e tags do YouTube. Não pule direto para a Etapa 2 sem passar pela Etapa 1.

## Hub

Comandos e regras gerais: `referencias/hub.md`. Nesta skill: na abertura, com a pauta conhecida e terminal neste PC, `status <id> trabalhando --texto "Gerando títulos e tags"` (a pauta continua em Montagem); com o título confirmado, `atualizar <id> --titulo`; no fim, o "Fechamento obrigatório: Hub", que é o único lugar que passa a pauta para Pronto. Se o `hub.py` falhar, diga em uma linha e siga.

## Etapa 1 — Títulos

**Hub, na abertura:** com a pauta conhecida e terminal neste PC, rode `status <id> trabalhando --texto "Gerando títulos e tags"` antes de gerar (a pauta continua em Montagem). Sem terminal, pule.

A partir do roteiro fornecido, gere:

**Opções de Títulos**, divididas em três categorias, com 2 opções cada (6 no total):
- Foco em Curiosidade
- Foco em Drama/Mistério
- Foco Direto/Viral

Regra importante: garanta que pelo menos uma das opções foque na notícia/confirmação principal do vídeo em si (o fato concreto), mesmo que o roteiro use um gancho de curiosidade ou mistério como abertura narrativa. Não deixe todas as opções dependerem só do ângulo de curiosidade do roteiro.

**A Melhor Escolha**: selecione o título com maior potencial de clique entre as 6 opções e explique em um parágrafo o porquê, citando o gatilho mental usado (curiosity gap, autoridade/factualidade, urgência, etc.).

Depois de apresentar isso, pare e espere o usuário confirmar qual título vai usar — ele pode escolher uma das opções sugeridas, pedir ajustes, ou trazer um título próprio. Não avance para a Etapa 2 sem essa confirmação.

**Hub:** com o título confirmado e a pauta conhecida, rode `atualizar <id> --titulo "<título confirmado>" --nota "título escolhido"`. O título da pauta igual ao do vídeo faz o Hub ligar a pauta ao vídeo quando ele for postado (etapa "no ar"). Sem `PAUTA DO HUB` no pedido e sem terminal, pule: esta skill também roda em chat sem acesso ao PC.

## Etapa 2 — Capa e Tags (só depois do título confirmado)

Com o título final em mãos:

**Texto para a Capa (Thumbnail)**: **8 a 10 opções** de texto curto (2 a 4 palavras), agrupadas por ângulo, cada grupo com 2–3. Elas são diferentes do título escolhido e devem complementar visualmente, trazendo um ângulo, reação ou detalhe que o título não entrega, nunca repetir a mesma informação do título. Em 18/out/2026 as 4 opções não bastaram, e ele pediu "mais ideias de texto na capa". Grupos que funcionaram no Bernal x Yamal:
- **Dúvida/polêmica:** "FOI TEATRO?", "CAIU OU FINGIU?", "QUEM EMPURROU PRIMEIRO?"
- **Injustiça/punição:** "E O YAMAL?", "ESCAPOU DO CLÁSSICO"
- **Ironia (dos comentários):** "MELHOR ATOR DE HOLLYWOOD", "VERMELHO PRO VINI?"
- **Detalhe do documento:** "NEM PRECISOU DE MÉDICO", "A SÚMULA ENTREGOU"
- **Reação:** "PERDEU A CABEÇA", "PEDIU DESCULPAS"

Feche com as 1–2 favoritas e o porquê, ligando com o título (o título conta a punição; a capa vira o foco para o Yamal).

**Ortografia letra por letra.** O texto da capa vai direto para a imagem. Em 18/out saiu "QUEM EMPUROU PRIMEIRO?" (o certo é EMPURROU). Antes de entregar, releia cada opção palavra por palavra, com atenção a rr/ss, acentos ("SÚMULA", "CLÁSSICO") e cedilha.

**Quando ele mandar a foto da capa** ("texto na capa para combinar com essa imagem", Andreas, 18/out/2026):
- Descreva em uma linha o que a foto mostra: gesto, expressão e objetos (a mão aberta do Andreas como quem pergunta "o que eu fiz?", o juiz com os dois cartões).
- Dê 4 textos que conversam com esse gesto ("EXPULSO POR ISSO?" com a mão aberta; "AMARELO + VERMELHO" com os dois cartões; "O QUE EU FIZ?" como fala dele), com a favorita.
- Diga onde pôr o texto sem cobrir rosto, cartão ou bola (o terço de baixo sobre a grama, ou o canto que está livre), e o destaque: letra branca com contorno preto e a palavra-chave em vermelho.

**Legenda do TikTok (busca):** a busca traz ~40% das views do canal no TikTok. Escreva 1–2 frases com as palavras que alguém digitaria para achar o vídeo: nome completo do protagonista, time, adversário ou competição e o fato em palavras simples ("Haaland reclama com Enzo Fernández em City x Brighton"), mais 3 a 5 hashtags (jogador, time, #futebol). Serve também para Instagram e Kwai.

**Crédito das imagens:** uma linha "Imagens: @perfil1, @perfil2, emissora" para o fim da descrição/legenda em todas as redes. As fontes vêm do prompt da montagem (`{FONTES}`) ou do `inventario.json` da pasta do vídeo (uploader dos clipes usados). Não dá direito de uso, mas mostra de onde veio o material.

**Tags para o YouTube**: gere imediatamente uma lista de tags otimizadas, com até 500 caracteres. Formato obrigatório: texto corrido separado por vírgulas, pronto para copiar e colar — nunca usar bullet points ou listas numeradas. Misture termos muito específicos do vídeo atual (nomes de jogadores, clubes, situação específica) com termos gerais do nicho (radar do campo, futebol, curiosidades de futebol, futebol europeu, bastidores do futebol, mercado da bola, etc.). Confira o limite de caracteres antes de entregar.

## Observações de estilo

- Nome do protagonista e o fato concreto vêm antes do mistério. "Todo mundo viu" e "ninguém percebeu" deixaram de ser padrão (06/11/2026): no máximo uma das 6 opções usa esse tipo de abertura.
- **Gancho de identidade brasileira:** se o protagonista estrangeiro passou por clube brasileiro, ou o caso envolve brasileiro, ponha isso no título. Em 18/out ele escolheu "Ex-Fluminense deu duas cabeçadas no Lamine Yamal e pode pegar 12 jogos": "Ex-Fluminense" faz quem acompanha o Brasileirão parar no vídeo. Junte com um dado concreto pouco visto ("duas cabeçadas", da súmula) e a consequência em aberto ("pode pegar 12 jogos").
- Nas duas escolhas de 18/out ele ficou com "A Melhor Escolha" sem ajuste (Andreas: "Andreas foi expulso por chutar uma bola… que não era a do jogo"). Continue recomendando um só, com o gatilho explicado.
- Se o usuário pedir para focar mais em algum ângulo específico (ex: a confirmação em vez do mistério), gere uma nova rodada de títulos com esse foco antes de seguir para a Etapa 2.

## Fechamento obrigatório: Hub (fim da Etapa 2)

Com a pauta conhecida e terminal neste PC, antes de encerrar a resposta da Etapa 2:

1. `ler <id>` para pegar a pasta e a etapa da pauta.
2. Grave `<pasta>\titulos e tags.txt` (sem pasta na pauta, na pasta temporária) com o título confirmado, os textos de capa favoritos, a legenda do TikTok, o crédito das imagens e as tags, do jeito que foram entregues.
3. Rode:

       python "C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\radardocampohub1.0\scripts\hub.py" --fonte titulos-e-tags atualizar <id> --etapa pronto --status aguardando --arquivo "Títulos e tags=<arquivo>" --nota "título, capa e tags prontos"

   Se a pauta já estiver em "ar", tire o `--etapa pronto` (o `--status aguardando` fica) (nunca volte uma pauta que já foi postada).
4. Feche a resposta com uma linha: `Hub: <título> em Pronto, com títulos e tags anexados.` Se o `hub.py` falhar, diga o erro nessa linha e siga (seção "Hub").

Sem terminal (chat sem acesso ao PC), diga em uma linha que o Hub não foi avisado.
