---
name: montagem-de-video
description: "Monta Shorts/Reels verticais de futebol do canal Radar do Campo a partir de roteiro + clipes garimpados + narração, no estilo das montagens feitas à mão pelo usuário: narração na velocidade original com as pausas entre trechos cortadas, filmagem da torcida em planos longos como base, protagonista sempre na tela, lance-chave em plano aberto antes do close, legenda karaokê (palavra falada em amarelo) no meio da tela. Use sempre que o usuário pedir para montar, editar, cortar ou finalizar o vídeo de um roteiro, mesmo que ele não diga 'montagem'. Use também quando ele pedir para comparar/estudar a edição que ele fez (compara minha edição, já postei, vê o que eu mudei) para aprimorar a skill, ou para abrir a montagem no CapCut (rascunho editável)."
---

# Montagem de vídeo — Radar do Campo

**Versão 2026-10-31b (a montagem nunca marca Pronto: na entrega a pauta fica em Montagem com os arquivos e o prompt de títulos e tags, o rascunho do CapCut só anexa, e quem passa para Pronto é a `titulos-e-tags`; pedido do usuário depois do Kaio Jorge, que foi Pronto → Montagem → Pronto). Antes: 2026-10-31 ("Fechamento obrigatório: Hub" no fim do arquivo: na entrega a pauta vai para Pronto com os arquivos e o prompt de títulos e tags; o rascunho do CapCut volta a pauta para Montagem; `{PASTA}` no prompt de títulos). Antes: 2026-10-30 (a pauta do Hub acompanha a montagem: seção "Hub", Passo 0 e Entrega; `{PAUTA}` no prompt de títulos). Antes: 2026-10-29 (regra: shot com enquadramento ruim por sujeira na tela volta ao garimpo atrás do mesmo vídeo limpo, em vez de zoom). Antes: 2026-10-28 (comparação do Bruno Guimarães x Fleetwood; Décima sétima rodada; `capcut_projeto.py` aceita 3 cards empilhados no mesmo shot, faixa CARDS3). Antes: 2026-10-27 (comparação em lote de CR7/Girotto, Toney, Neymar e a Lei Vini Jr, Piqué/Mbappé e Yamal na Bola de Ouro; Décima sexta rodada; o rascunho do CapCut agora leva os desfoques, as setas e a música até o fim, com a virada na revelação; `analisa_capcut.py` e `pares_quadros.py`). Antes: 2026-10-23b (prompt de títulos e tags para chat novo no fim de toda entrega). Antes: 2026-10-23 (comparação em lote de Carlos Miguel, Thiago Silva e Cetré; Décima quinta rodada). Antes: 2026-10-22 (correção no `capcut_projeto.py`: o fim de cada trecho da legenda é arredondado em microssegundos antes de subtrair o início, porque o arredondamento separado sobrepunha trechos e travava o rascunho no Thiago Silva). Antes: 2026-10-21b (entrega reduzida a 2 arquivos, com-legenda e sem-legenda, sem logo do canal; o rascunho do CapCut não herda as logos do modelo). Antes: 2026-10-21 (comparação em lote de Paquetá, Kannemann, Neymar x Soteldo, Neymar x Thiago Mendes e Vitinha, todos refinados no CapCut: gancho com punch-in e pan, janela no lado certo do assunto, fonte limpa do mesmo lance, prova segurada até o fim, trilha do modelo mais baixa, `compara_capcut.py`; Décima quarta rodada).** Anterior: 2026-10-18 (Andreas, Bernal e Leo Flores: rascunho do CapCut, item 22 e item 23). A versão é identificada pela DATA (não por v18/v19: o claude.ai conta os envios com outro número).

## PASSO ZERO OBRIGATÓRIO — usar sempre a versão mais nova

A cópia-mestre fica no HUB: `C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\Claude\skills claude\versao-nova-2026-09-22\montagem-de-video\`. Antes de qualquer outra coisa, leia a linha "Versão AAAA-MM-DD" do `SKILL.md` do HUB. **Se a data do HUB for mais nova que a desta cópia instalada, siga o SKILL.md do HUB inteiro (ignore este) e copie os `scripts/` e `assets/` do HUB** para `<job>/_montagem/`. Se forem iguais, use os scripts desta pasta. Diga ao usuário, em uma linha, qual data de versão está usando. Toda atualização da skill grava primeiro no HUB (com backup `_bak-AAAA-MM-DD-...`) e muda a data; assim o que foi decidido num dia vale no seguinte mesmo que o `.skill` não tenha sido reenviado.

Monta o vídeo vertical 9:16 a partir de três insumos: roteiro, clipes brutos (da skill `garimpo-de-videos`) e a narração já gravada. Buscar e baixar clipe é trabalho do garimpo; aqui é montagem.

## A referência que manda

`HUB Radar do Campo\Claude\videos exemplos\REFERENCIA MONTAGEM - Carrascal (feito a mao) TIKTOK.mp4`

O usuário montou esse vídeo à mão com o mesmo material que o garimpo baixou, enquanto uma versão automática era montada em paralelo. A comparação das duas deu origem a esta versão da skill. A automática estava tecnicamente correta, mas parecia outro canal. O que separa as duas, em ordem de impacto:

1. **Matéria-prima.** Mais da metade do vídeo dele saiu de um único clipe que a automática nunca abriu: um "react" de 96s cujo miolo (3–57s) eram 54 segundos limpos filmados da arquibancada, seguindo o protagonista. Ele também aproveitou *trechos* de clipes que a automática descartou inteiros (um círculo vermelho de destaque, o ângulo depois de uma legenda queimada).
2. **Torcida em planos longos.** Cerca de 23 planos por minuto, média ~2,6s, com takes de torcida de 5 a 8s cobrindo várias frases seguidas. A automática fez 41 planos por minuto, quase tudo de transmissão.
3. **Protagonista na tela.** Nas falas genéricas ele mostra o jogador andando em campo, não torcida nem estádio. Abre e fecha com o mesmo close do jogador.
4. **Narração enxuta.** Na referência ele acelerou a 1,2x (72,5s viraram 60,3s). Em set/2026 o usuário mudou a regra: **não acelerar**, só cortar as pausas entre os trechos (ver Passo 1).
5. **Lance-chave legível.** Plano aberto do lance inteiro, depois o close, em velocidade normal, depois um 2º ângulo. Nada de câmera lenta esticada.
6. **Legenda karaokê.** A palavra *falada* fica amarela e o amarelo anda palavra por palavra. Uma linha só, fonte menor, no meio da tela.

Segunda referência, **Faiq Bolkiah** (set/2026): `Videos prontos\Shorts\O jogador mais rico do mundo está desempregado\Videos prontos\O jogador mais rico do mundo tá desempregado. TIKTOK.mp4` (e `YOUTUBE`). O usuário remontou à mão partindo do corte automático. O que ele mudou e virou regra:
- **frase-ponte de loop** no fim (Passo 1b)
- **-10 LUFS** e trilha dele por baixo
- **marca do YouTube pequena no canto superior direito**
- **imagem literal** onde a fala nomeia um grupo ou uma coisa (Passo 3, item 7)
- "sem legenda" **sem marca**, porque ele edita a partir dele

Terceira referência, **Palermo e Paulo Diogo** (set/2026): `Videos prontos\Shorts\Jogadores que se machucaram comemorando gol\Videos prontos\Ele perdeu o dedo comemorando… e o juiz ainda deu amarelo TIKTOK.mp4`. O usuário partiu do corte automático e manteve o miolo (33–70s) igual. Isso aprovou a tela cheia com o zoom seguindo o lance e o desfoque do ferimento. O que ele mudou e virou regra:
- **gancho = prévia do lance-chave** (Passo 3, item 9), não o ferimento
- **imagem literal da ação da frase:** "se machucaram comemorando" pede a comemoração, não a ambulância (Passo 3, item 7)
- **gol no replay fechado seguindo a bola**, em vários ângulos, e não o plano aberto em que a bola some (Passo 4)
- **seta vermelha** apontando o protagonista no quadro confuso, com o plano segurado enquanto a narração descreve a lesão (Passo 5)
- **fonte onde o assunto ocupa mais pixels**, e não a mesma cena com zoom de 3,7x (Passo 5)

Quarta rodada, **Kane (Inglaterra x Espanha) e Atlético-GO** (27/set/2026). O que o usuário corrigiu e virou regra:
- **gancho no momento mais forte, já no primeiro segundo:** no Atlético-GO abri no goleiro comemorando no apito e só depois vinha o grito. Ele achou que "não prende". Refeito abrindo direto no goleiro gritando para o camarote (o payoff), e aprovou (Passo 3, item 9)
- **fala factual pede a imagem do fato:** "quatro clássicos, uma derrota, três empates… viu o rival ser campeão goiano" coberto com torcida do jogo = "sem contexto, mostra muita torcida". Trocado por placar dos jogos anteriores, rival comemorando na final, a taça e o rival campeão (Passo 3, item 10)
- **prévia de suspense:** no Kane, logo depois do rosto no gancho, ele pediu o replay com círculo no pé em câmera lenta **cortado antes do escorregão**, para segurar até a revelação (Passo 3, item 11)

Quinta rodada, **Ronaldo no banco e Arrascaeta x Estudiantes** (28/set/2026). Ele refinou no editor em cima do `completo-sem-legenda` (mesma duração, mesmo corte). Comparação quadro a quadro com `compara_edicao.py` e `lado_a_lado.py`:
- **lance-chave inteiro, num take só:** no Arrascaeta, eu abri com a queda como prévia e, na hora da narração ("escorregou sozinho, caiu com o braço esticado e o punho quebrou"), picotei em 4 cortes (círculo vermelho, replay, close caído). Ele trocou tudo pelo **mesmo clipe do gancho, contínuo**, do domínio até ele no chão (Passo 3, item 12)
- **assistência/gol = o lance; sem lance bom = o rosto dele:** "deu assistência do primeiro gol e fez o segundo" estava coberto com replays onde os jogadores ficam pequenos e parados. Ele trocou por closes dele sorrindo e gritando. Regra dele: mostre o lance se houver com qualidade; se não houver, close da reação/emoção; nunca o lance com jogador pequeno e parado (Passo 3, item 13)
- **emoção do protagonista nos fatos dele:** no Ronaldo, "sem entrar em campo" (Euro 2008) virou o close dele chorando, no lugar do plano aberto do jogo; o banco virou enquadramento fechado nele, sem o técnico na frente (Passo 3, item 7)
- **loop pelo rosto:** no Ronaldo ele abriu e fechou com o mesmo close do rosto rindo (Passo 3, item 4)
- **transições sim, SFX não:** manteve o flash/zoom e a grade de arquivo (`posfx.py`), tirou os nossos efeitos sonoros e pôs a trilha dele, a mesma nos dois, começando ~15 dB abaixo da voz e subindo em degraus (~35s e ~53s) até ~8–10 dB abaixo
- **legenda:** refez no CapCut (mesmo estilo, ~55% da altura). A automática dele errou "o punho quebrou" → "Pedro quebrou"; avise nomes e trechos arriscados na entrega (Passo 6)

Sexta rodada, **Vini ofereceu o pênalti ao Bruno (Austrália 2x4 Brasil)** (29/set/2026). Refinou em cima do `completo-sem-legenda` (mesma duração); manteve ~85% do corte: o trecho da Copa com `flashback`, a foto do Ancelotti, os closes do Vini, a entrevista e o loop. O que ele trocou:
- **o chute tem que estar no plano:** "empata… com o Raphinha, de pênalti" estava num ângulo cinematográfico da TNT atrás da trave que começava **depois** do chute (goleiro já no chão). Ele trocou pela transmissão aberta do compacto da ge (corrida → chute → bola na rede), com a logo da ge fora do quadro (Passo 3, item 14)
- **o lance do payoff não repete os quadros do gancho e termina na rede:** em "ele bateu rasteiro e fez o quarto" eu repeti o trecho do gancho, e a câmera saía da bola antes do gol (campo vazio no fim). Ele pôs outra transmissão, **com o placar 2T 34:29 AUS 2x3 BRA na tela**, seguindo até o goleiro caído e a bola na rede. Placar de transmissão é prova, não sujeira (Passo 3, item 14; Passo 5)
- **zoom de aproximação quando a ação está pequena:** no take da arquibancada da discussão na marca, no gol do Bruno visto de longe e no Vini derrubado, ele fechou mais o quadro (punch-in progressivo) até os jogadores ficarem legíveis. Não é o zoom excessivo do Palermo: é fechar na ação quando ela ocupa menos de ~1/4 da largura (Passo 5)
- **fato genérico sem pessoa aleatória:** "segundo amistoso entre os dois em quatro dias" estava no telão com o rosto do Otávio (goleiro que nada tem a ver com o roteiro). Ele trocou pela **roda da Seleção abraçada** no gramado. Não mostre de rosto alguém que o roteiro não cita (Passo 3, item 7)
- **gancho mais seco:** o close do Vini durou ~0,7s (eu fiz 1,1s) e o chute entrou direto, sem o `flash` no primeiro corte
- **áudio:** sem SFX; trilha começando ~17 dB abaixo da voz, subindo em degraus (~32s para ~-11 dB, ~46–54s para ~-8/-9 dB). Publicou a -11,1 LUFS (manteve o nosso nível)
- **legenda:** refez no CapCut a ~62% da altura. A automática errou "Noruega" → "doruega", "Ancelotti" → "ancelote", "Raphinha" → "Rañnha"; liste esses nomes na entrega (Passo 6)

Oitava rodada, **Argentina sem a camisa 10** (01/out/2026). Ele publicou **o nosso corte sem mudar nenhum quadro nem a legenda** (`compara_edicao.py`: zero trechos de imagem trocados), depois de pedir uma troca de gancho: a camisa ROMERO 13 pendurada no vestiário (objeto parado, bonito, mas não prende) virou **o Nico Paz pulando na comemoração, de costas com a 18** (a pista visual da revelação, em movimento). Só acrescentou a trilha, no padrão que o `guia_trilha.py` agora calcula: entra ~1s, ~17 dB abaixo da voz; abaixa ~4s antes da revelação; batida nos `flash`/`flashback_in`; sobe ~3s depois da revelação para ~11–12 dB; sai ~2s antes do fim (loop só com voz). -10,4 LUFS.

Nona rodada, **Modric aplaudido em Sevilha e a raça do Endrick** (comparados em 02/out/2026). Nos dois ele partiu do `completo-sem-legenda` (mesma duração) e manteve **~90% do corte**. Trocou só o **gancho e o shot de loop** (os dois), e no Modric mais dois trechos de fato. Para isso baixou clipes por conta própria (arquivos `<id>.mp4` em `clipes/`):
- **gancho = pessoa em ação, nunca torcida genérica, mesmo que a torcida seja o auge da história:** no Modric eu abri na arquibancada de pé aplaudindo (o clímax do roteiro), e ele trocou pelo **Yamal agachado sentado na bola** (o craque da goleada, num gesto que viralizou), filmado da arquibancada, cobrindo "a Espanha meteu 4 a 1 na Croácia". O loop fecha no mesmo take do Yamal. Gancho de fato coletivo ("a Espanha meteu 4 a 1") = o rosto/gesto de quem representa o fato (item 19), não a massa (Passo 3, item 9)
- **gancho em filmagem de torcida quando ela pega o mesmo momento:** no Endrick eu abri na câmera alta da TV com ele já no chão; ele trocou por um vídeo da arquibancada, na altura dos olhos, do **bolo inteiro acontecendo** (empurra-empurra → mão no rosto → queda), que o garimpo não tinha achado (@trent_1228, "Endrick 1 vs 11"). Mostra a ação e a escala da confusão, e foge do Content ID. O loop fecha no mesmo take (Passo 3, item 9)
- **"depois do título da Copa do Mundo" = imagem do título, de outra data:** eu cobri "primeiro jogo em casa depois do título" com os fogos da entrada; ele pôs **os campeões no túnel da Copa** (Rodri 16, Yamal 19, vídeo de julho/2026 em Los Angeles). Fato de outra data citado na frase vale mais que o ambiente do dia (item 10)
- **gol narrado na transmissão aberta até a rede:** "com dois minutos, Yamal já tinha marcado" estava num take da linha de fundo que acompanhava o Yamal correndo, sem a bola entrar. Ele trocou pela transmissão aberta (chute → goleiro → rede). Torcida só vale para o gol se mostrar a bola entrando (item 14)
- **trilha (a mesma nos dois, mesmo desenho):** entra em ~1s a ~18 dB abaixo da voz; queda curta em ~33–34s (-20/-23 dB); a partir de ~35s sobe para ~-12 dB; em ~53s sobe de novo para ~-9 dB; sai em ~62s (1–2s antes do fim). Três degraus (-18 → -12 → -9), não dois. Sem SFX. -10,7 LUFS.

Sétima rodada, **Raphinha cortado da Seleção** (30/set/2026). Dessa vez ele montou **do zero**, sem partir de entrega nossa: usou os clipes do garimpo (a maior parte do vídeo) e acrescentou o que faltava. `casar_fontes.py` + folhas a cada 0,5s mostraram:
- **gancho de uma história de padrão = a imagem mais forte do padrão, não o evento mais recente:** o roteiro abria com o corte depois da Austrália, mas ele abriu no Raphinha **agachado com a comissão na Copa** (a lesão mais grave), com um **ícone sobre a cabeça dele: o escudo da CBF riscado com um X vermelho** ("foi cortado da Seleção"). Fechou no mesmo take, com o mesmo ícone, emendando no loop (Passo 3, item 15)
- **parte do corpo nomeada = aproximar nela:** em "edema na parte de trás da coxa" ele fez um punch-in na parte de trás da coxa; no infográfico, um zoom nos marcadores da coxa (item 16)
- **lugar nomeado = imagem do lugar:** "fora do jogo contra a Índia" virou um estádio de Calcutá cheio, de outro evento (o jogo ainda não aconteceu) (item 17)
- **enumeração = um corte por item:** "março, junho, setembro" virou três cortes de ~0,5s, cada um numa lesão já mostrada (item 18)
- **instituição = o rosto de quem a representa:** "a Seleção tá sugando o Raphinha?" ficou 3s no close do Ancelotti (item 19)
- **dado-resumo = infográfico de portal:** "sempre na coxa… quarta lesão em um ano" virou uma arte do 365Scores ("ALERTA LIGADO", corpo com as lesões marcadas), com a marca do portal tirada e a imagem ampliada no editor de IA. A IA deformou as letras pequenas: "COSA DIREITA", "ZORA DO MONSO", "MÚRCULO", "AMISTERO" e um escudo inventado no lugar da Austrália (item 20)
- **fato de outra data em filmagem de torcida:** a lesão contra a França veio de um vídeo da arquibancada com **o telão mostrando o placar e o tempo** (prova do jogo) e **seta vermelha** quando ele cai. Ele **segurou o lance ~8,5s**, cobrindo "lesão na coxa de novo, cinco semanas parado e ficou fora das quartas da Champions…", passando o lance **duas vezes** (com seta, depois limpo). Não cortou para Barcelona x Atlético, que tínhamos baixado (itens 6 e 10)
- **ação genérica pode vir de outra data:** "ele voltou pra Barcelona" = ele saindo de boné e mochila pela zona mista da Copa. A fala não afirma que aquilo é o dia do corte (item 7)
- **"não dá pra falar que é corpo mole"** = o momento da lesão (a prova), não um rosto qualquer
- **ritmo ~26–31 cortes/min** (média ~2s), com os inserts de 0,5s do resumo e do gancho
- **reposts de baixa resolução com momento único entraram:** 720x960 dele andando no intervalo visto da arquibancada, 720x960 do close com o médico. Momento certo em 720 vale mais que momento genérico em 1080
- **legenda do CapCut a ~70% da altura**, com erros publicados: "Rafinha" (em vez de Raphinha) várias vezes e, em 54,4–55,3s, **"Rafinha teve uma lesão" no lugar de "a coxa dele tá pedindo socorro"**. Por isso agora entregamos o `.srt` com a grafia certa (Passo 6)
- **narração:** o AI Studio não falou "sábado, em Calcutá" e trocou "inédito" por "difícil" (Passo 0)
- **áudio:** -10,3 LUFS, sem SFX, trilha começando ~14 dB abaixo da voz e subindo até ~10 dB

Décima rodada, **"Lotou pro Messi… mas não pra Seleção" (Índia 0x4 Brasil, 03/out/2026)**. Ele não pediu para refazer, mas apontou quatro defeitos de montagem que viraram regra (Passo 3b, Passo 5 e Passo 8):
- **zoom demais matou o contexto:** planos que existiam para mostrar escala (Salt Lake lotado em 2011, o estádio no hino, a placa, o cartaz do jogo) foram recortados numa fatia de 9:16 com zoom 1,5–1,75 ou upscale de 3,5–5,3x. O espectador não via que o estádio estava cheio, nem que era um estádio. Plano de escala/lugar não leva zoom (Passo 5)
- **torcida genérica no lugar da frase:** "um torcedor resumiu: é um buraco no bolso" foi coberto com arquibancada vazia, quando o garimpo tinha o torcedor revoltado falando do preço do ingresso (CNN, 48–55s). "Bandeira do Brasil era difícil de achar" mostrou justamente o grupinho com bandeiras do Brasil (a imagem contradizia a frase). "Quem chamou atenção cantando o hino foi a própria imprensa brasileira" mostrou fotógrafos indianos numa coletiva. "Ingresso começava em 3.500 rúpias" e "dez meses depois" viraram estádio vazio genérico. Cada frase inteira precisa da imagem do que ela diz (Passo 3b)
- **corte antes do impacto:** o indiano com a camisa 10 da Argentina batendo a cadeira foi cortado em 22,07s, e a cadeira voa em 22,0–22,2s e ele bate de novo em 23,7–24,2s. O momento mais forte do vídeo inteiro saiu sem o golpe (Passo 3b, item 3)
- **gancho fraco:** abri no grupinho de brasileiros no setor vazio (plano parado, de longe). O gancho tinha que ser o take mais chocante do material: o torcedor arrancando e jogando a cadeira, ou o gramado invadido, cortado logo depois do golpe, e só então a narração do "detalhe" (Passo 3b, item 1)

Décima primeira rodada, **"Bruno Duarte apagou e ninguém viu" (Botafogo 1x2 Vasco, 08/out/2026)**. **Aprovado sem nenhuma mudança** ("ficou perfeito e muito bom"). Antes de montar, ele pediu três coisas, e o resultado virou o modelo para roteiro de um incidente (desmaio, lesão, briga):
- **Gancho = prévia do incidente:** o replay fechado da joelhada e da queda já no quadro 1, depois o 2º ângulo (arquibancada) dele de joelhos indo ao chão. Corta antes do socorro.
- **"Que os vídeos se completem":** depois do contexto, o incidente volta **inteiro e em ordem cronológica**, cada frase coberta pelo momento seguinte do mesmo evento: assistência → dividida ao vivo até o chão → replay da joelhada → ele se contorcendo → jogo parado com ele caído no canto → ele sozinho e imóvel → companheiro dando tapinhas (take contínuo) → médicos → maca → substituto entrando → maca saindo vista da arquibancada. Nada de imagem fora daquele trecho (Passo 3, item 21).
- **Jogador sempre bem enquadrado, sem zoom enorme:** zoom de 1,2–1,6 com `keys` seguindo a bola e o jogador. O mesmo zoom tirou as logos de TNT e Prime e o texto da CazéTV.
- **Espinha num clipe só:** um vídeo de transmissão de 50 s (xsports) cobria o incidente inteiro e foi a base, usado em ordem. Quando a frase era maior que o trecho, desacelerou 0,6–0,75x em vez de trocar de assunto.
- **Torcida 16%** e foi aprovado: o incidente só existia na transmissão (Passo 5, meta de torcida não se aplica).
- A revisão a cada 0,1s pegou o que faltava: logos de TNT/Prime, a dividida ao vivo mal enquadrada e a frase "o Colidio lança o David" coberta por outro lance. Foram 3 rodadas de rascunho, e só depois os 4 arquivos.
- A narração do AI Studio veio **sem a frase de abertura** do roteiro (o gancho do Tite). Avise antes de montar (Passo 0).

Décima segunda rodada, **comparação em lote de 17 vídeos (02/out a 17/out/2026)**, `compara_edicao.py` entre o `completo-sem-legenda` e o `TIKTOK.mp4` publicado:
- **8 de 17 saíram sem nenhuma troca de imagem, só a trilha** (Hojlund, Vitor Hugo, Luiz Araujo/Gabigol, CR7 suspenso, Pulgar, Vasco/Bombonera, Bruno Duarte e Cunha, o de 17/out). Padrão atual está certo: não mexa no que a rotina já faz.
- **Gancho literal à primeira frase (Messi, "Todo mundo viu o Messi se despedir"):** abri no Messi rindo com os companheiros (outro momento). Ele abriu no Messi emocionado no telão e nos drones com o 10, a própria homenagem. A imagem de 0–2s mostra o fato da primeira frase, não a pessoa em outro contexto (itens 9 e 10).
- **Sem flash branco no 1º quadro do gancho (Endrick x Roma, Drones):** ele tirou o `flash` do primeiro corte e abriu o quadro um pouco mais (mais da ação visível). Gancho seco, como no Vini. Não ponha `fx: flash` no shot 1.
- **Loop só por rosto ou ação, nunca por react/webcam (Drones):** o último shot era um streamer de webcam (react); ele fechou no close do Messi olhando para cima sorrindo, e o gancho recomeça nos drones. No Isaac Romero ele reajustou o shot final para o gesto do próprio gancho (mão levantada); no Tite encurtou 0,4s e fechou mais no árbitro com o cartão. Confira o último shot no `bordas_XX.jpg`: sem pessoa de webcam nem texto de fonte.
- **Plano de lugar legível (Isaac, 5,8–7,7s):** eu usei o gramado visto de cima, estreito, vertical, com poucas pessoas. Ele pôs o plano horizontal da cerimônia com os times alinhados. Plano de contexto mostra gente e cena, não só grama.
- **Flashback P&B só quando a fonte é antiga e curta (Rossi):** ele tirou a grade escura e preta e branca dos trechos de fato antigo e deixou colorido, e refinou tudo no Concat (65,17s). Com muito trecho de arquivo, o P&B cansa; use `flashback` só em 2 ou 3 shots.
- **Vini expulso:** ele reeditou a segunda metade para 60s, trocando a súmula em texto (36s) pelo árbitro mostrando o cartão em campo e fechando no Vini apontando para a torcida. Fato visual ganha da súmula em texto quando existe o lance.
- **Jorge Jesus (26–27,5s):** só reenquadrou o post do Instagram (mais alto). Calcutá (11,0–11,8s): troca de 0,8s, não identificada.

Décima terceira rodada, **Leo Flores, Andreas Pereira e Bernal x Yamal (17 e 18/out/2026)**. O Leo Flores saiu **sem nenhuma troca de imagem**, só com a trilha (-10,6 LUFS). O Andreas e o Bernal ele refinou **dentro do rascunho do CapCut que nós geramos** (Passo 9). Por isso a comparação foi pelo próprio projeto: o `draft_content.json` que geramos contra o que ele salvou. Ficaram a legenda (fonte, tamanho, altura) e a trilha do modelo dele sem mexer. O que ele mudou:
- **"O motivo da expulsão" = o cartão no quadro (Andreas, 3–8s):** eu enquadrei o árbitro da cintura para cima e o cartão vermelho levantado ficou fora do quadro. Ele desceu o quadro para mostrar o cartão e os jogadores reclamando. A logo da ge entrou no canto, e ele cobriu com um desfoque retangular (máscara no CapCut). A ação vale mais que um quadro sem logo (item 23; Passo 5, marcas).
- **Detalhe pequeno num plano aberto = punch-in progressivo até ele (Andreas, 22–25s):** em "uma bola veio da arquibancada e caiu no gramado", o plano alto da Prime mostrava o campo inteiro e a bola extra era um ponto. Ele fechou de 3,16 para 4,67 seguindo a bola, até ela ficar visível (item 23).
- **Relação no espaço = abrir o quadro (Andreas, 25–32s):** no lance em câmera lenta eu fiquei fechado (1,75) no Andreas. Depois do chute, ele abriu para 1,19, para caber as duas bolas, o Andreas e o atacante. O espectador precisa ver a bola extra acertando a bola do jogo (item 23).
- **Gancho com punch-in no contato (Bernal, 0–1s):** a cabeçada na câmera da TV passou de 1,22 para 1,72 no meio do shot, fechando no instante do contato.
- **Arte parada ganha movimento (Bernal, 9,4–11,8s):** na arte "DONE DEAL" do Betis ele pôs um zoom lento de 1,0 para 1,25. Foto ou arte em tela cheia não fica estática.
- **Pan seguindo a ação** na cabeçada em câmera lenta (23–26s) e no gol do Abde. Este ele teve que refazer, porque o keyframe que eu gravei não andava no CapCut (Passo 9, tempo dos keyframes).
- **Efeitos sonoros ligados nos dois:** ele ativou a faixa SFX (que eu deixava muda) e só baixou o 1º impacto do Andreas de 0,55 para 0,43. A trilha ACIDO do Bernal saiu ~1,4s antes do fim (loop só com voz).
- **Exportou um arquivo só, com a lupa e o logo do YouTube ocultos.** Publicou a -14,4 LUFS (Andreas) e -13,3 LUFS (Bernal), porque o CapCut não normaliza. Os nossos 4 arquivos continuam a -10 LUFS.

Décima quarta rodada, **Paquetá, Kannemann, Neymar x Soteldo, Neymar x Thiago Mendes e Vitinha (19 a 21/out/2026)**. Ele refinou os cinco **dentro do rascunho do CapCut**, e a comparação foi pelo projeto (`compara_capcut.py`). Em nenhum mexeu na legenda. O que se repetiu:
- **Gancho nunca parado:** nos cinco ele mexeu no shot 1. Punch-in (Vitinha 1,05→1,76; Thiago 2,4→2,84) e pan seguindo a ação (Paquetá -0,22→+0,22; Soteldo; Vitinha). No Kannemann foi o contrário: o nosso pan pulava de lado no meio do gancho (+0,28 → -0,55), e ele abriu para 1,23 e deixou a janela quase parada sobre a ação inteira. O shot de loop leva o mesmo quadro (item 23).
- **Gancho = a humilhação/o fato do título acontecendo (Thiago Mendes):** trocou o nosso gancho por um post da ESPN que ele baixou, **os jogadores do Boca comemorando na frente do Thiago Mendes**, fechando nos jogadores (o card do post fica fora do quadro). O título dele era "…após ser humilhado na eliminação". O loop fecha no mesmo clipe a 0,33x.
- **Post citado = o post (Thiago):** em "postou uma montagem feita com inteligência artificial em que rasgava o escudo do Boca", ele pôs **a própria montagem** (repost de perfil de torcida). Item 22 vale também para arte/IA citada.
- **Janela no lado ou na altura errada:** no Soteldo, quase todos os shots da ESPN tinham y 0,26 e ele desceu para ~0 / -0,27. No Kannemann, a coletiva do Renato e os melhores momentos estavam do lado errado (x -0,43 → 0,37). Confira na revisão se o assunto está no centro da janela, não só dentro dela.
- **Duas fontes do mesmo lance: a limpa (Soteldo):** trocou 3 shots do post da ESPN com cards de texto queimados ("…ado ilegal", "NEYMAR PARTIU PARA CIMA DO SOTELDO, MAS…") pelo outro post da ESPN do mesmo lance, sem texto.
- **Enquadramento ruim por sujeira = voltar ao garimpo, não aproximar (regra de 29/out/2026, Giay):** se um shot só fica bem enquadrado com zoom acima de ~1,6 ou com recorte grande para esconder texto, logo, moldura ou tela dividida, procure o MESMO vídeo/lance numa versão limpa (fonte original, outro repost, outra rede) e troque antes de entregar. Vale sempre. Só aproxime ou tampe se não existir versão limpa, e diga na entrega quais shots ficaram assim.
- **Texto queimado sem fonte alternativa = desfoque retangular (Paquetá):** cópia do clipe por cima, com máscara desfocada só sobre o texto. Mesma regra do Andreas (Passo 5, marcas, 1b).
- **Menos cortes no trecho da prova (Thiago, Kannemann):** quatro shots curtos de fontes diferentes viraram o post do Neymar com a camisa do Paredes (punch-in com pan) + uma reação em câmera lenta 0,62x por 6,3s. No Kannemann, tirou um insert de 0,7s de outra fonte no meio de um lance.
- **Prova segurada até o fim (Paquetá):** os cards de comentário (corintiano e palmeirense) entram empilhados e ficam até o último quadro, em vez de entrar e sair um por um.
- **Zoom menor em lance coletivo:** no Thiago ele abriu quase todos os shots do começo (1,5→1,25; 1,67→1,36; 1,93→1,55). Zoom forte só em detalhe ou rosto.
- **Flashback P&B mais longo** (Kannemann 58–68s, Vitinha 46–51s): ele esticou a faixa do filtro para cobrir o trecho de outra época inteiro.
- **Trilha do modelo mais baixa em todos:** de 0,34 para 0,15 / 0,16 / 0,09 / 0,07. O `capcut_projeto.py` agora grava 0,12 na trilha principal do modelo (Passo 9). Nos vídeos sem SFX, ele apagou a faixa SFX vazia.
- **Faltou no garimpo:** o post da ESPN da comemoração na frente do Thiago Mendes e o repost da montagem de IA. Ele baixou os dois.

Décima quinta rodada, **Carlos Miguel e a toalha, Thiago Silva 2008–2026 e Cetré e o pênalti repetido (22 e 23/out/2026)**, comparados pelo projeto do CapCut (`compara_capcut.py`). Legenda intacta nos três. O que ele mudou:
- **Punch-in no lance, de novo:** gancho do Thiago Silva de 1,0 para 2,23; shot 1 do Carlos Miguel com zoom 1,9→2,65 e pan; vários shots do Thiago com pan seguindo a ação onde a nossa janela era fixa. Shot parado com ação acontecendo continua sendo o ajuste nº 1.
- **Gancho pelo pico em câmera lenta (Cetré):** trocou o rosto de 0,6s por um close dos pés a 0,81x com pan, e repetiu esse mesmo take no meio (35,4s e 49,2s) e no loop. O lance-chave volta como refrão visual.
- **Trecho da prova inteiro numa fonte só, em câmera lenta (Carlos Miguel 38,5–44,8s):** dois shots de fontes diferentes viraram um take da getv a 0,5x por 6,3s.
- **Desfoque retangular de texto/logo em série (Cetré):** 9 cópias do clipe da Conmebol por cima, na mesma posição, para mascarar o texto queimado.
- **Flashback P&B:** no Thiago Silva ele apagou o filtro (61s de arquivo em P&B cansava); no Cetré trocou o filtro por outro. Trecho longo de arquivo fica colorido.
- **Trilha ainda mais baixa** (0,08–0,11) e faixa SFX vazia apagada.

Décima sexta rodada, **CR7 e o gol do Girotto, Toney e o vídeo de IA, Neymar e a Lei Vini Jr, Piqué e a manita, Yamal de cara fechada (24 a 27/out/2026)**. Os cinco foram refinados no rascunho do CapCut e comparados corte a corte com `analisa_capcut.py` (a frase narrada e a nota de cada shot ao lado do que ele mudou) e `pares_quadros.py` (nosso x dele no mesmo instante). Legenda intacta nos cinco. O Hinestroza não foi mexido nem exportado. O que ele mudou:
- **Metade dos "reenquadramentos" eram desfoques nossos que não chegavam ao CapCut.** No CR7, os shots 1, 8, 9, 23, 36 e 38 (os que tinham `borrar` na logo da Thmanyah) ganharam zoom 1,2–1,25 deslocado para tirar a logo. No CR7 e no Piqué ele refez à mão 9 desfoques (cópia do clipe + máscara Retângulo + efeito Desfocar). O `capcut_projeto.py` agora leva cada `borrar` assim (faixa DESFOQUE) e as setas/círculos (faixa SETAS) (Passo 9).
- **Marca que escapou do nosso desfoque:** no CR7 a caixa do `borrar` ficou logo acima do "FIFA+", e a logo apareceu nos 5 shots da Copa 2022. No Neymar, o "g" da ge no canto superior direito sobrou em 4 shots do vídeo da ge (ele fechou de 1,20 para 1,22–1,24 e deslocou).
- **Gancho = o pico físico, não a provocação (Neymar):** abri no Neymar de costas, falando com a mão na boca. Ele abriu na confusão (Neymar partindo para cima e sendo segurado, com pan) e fechou o loop no mesmo take a 0,71x. A mão na boca desceu para o shot 2, a 0,63x, em "o nome da regra que tirou ele de campo": a regra pune cobrir a boca, então a imagem é o gesto (item 7). O nosso shot 2 era um reserva de colete amarelo, com o Neymar fora do quadro.
- **Gancho começa perto do pico (Piqué):** a mesma arrancada do Mbappé, mas entrando 2,2s depois (o chute aparece logo), sem pan. O loop acompanhou.
- **Gancho literal com contexto (Yamal):** o nosso era um close extremo do rosto (da testa ao queixo, parado). Ele baixou um vídeo postado no dia seguinte (@kart_x, 960x720) com o Yamal sentado no momento do anúncio e gente se levantando ao lado, com pan a 0,81x, e fechou o loop nele. Também trocou os outros closes extremos ("dessa cena", "ficou em terceiro", "cara fechada") por fotos nítidas (photo mode do TikTok) que mostram cabeça, ombros e quem está do lado, com punch-in lento.
- **O ponto da prova numa câmera lenta progressiva (CR7):** "na câmera lenta começou a dúvida… a cabeça de um zagueiro brasileiro, o Andrei Girotto" (21,8–28,4s) tinha 4 cortes (lupa, círculo, seta, Girotto). Ele pôs o replay da TV do mesmo instante, contínuo, desacelerando 0,64x → 0,23x → 0,17x até o contato da bola com as cabeças. É a regra do Carlos Miguel (prova numa fonte só, em câmera lenta) levada ao extremo: quanto mais perto do detalhe, mais lento.
- **"O mesmo lance" = os mesmos quadros (CR7):** em "não dá pra ver se o Cristiano toca" e em "a Opta olhou o mesmo lance" ele usou o mesmo trecho do vídeo por trás do gol, com pan seguindo o CR7. Quando a frase diz "o mesmo lance", repetir de propósito é a imagem literal.
- **Punch-in no dado lido (CR7, Toney):** na página da Liga, zoom de 2,27 para 3,03 até "Ronaldo 49'"; na súmula, de 1,5 para 2,0 na linha do gol; no post do relatório médico, de 1,0 para 1,41 subindo até o texto da lesão.
- **Detalhe nomeado = punch-in nele (Neymar):** "colocou a mão na frente da boca" e "cobriu a boca" passaram de 1,0 para 1,62–1,67 no Neymar.
- **Ação inteira no quadro:** a falta do Félix com zoom 1,89 cortava o corpo dele, e ele abriu para 1,58. "Ele ainda fez outro" ganhou pan do CR7 até a bola entrar. "O Toney abriu o placar" passou a começar 0,7s antes, no cabeceio, com pan até a rede (item 14).
- **Pessoa nomeada entra na palavra (Yamal):** em "enquanto o Mbappé…", ele puxou o corte do Mbappé na plateia 0,2s para trás, para a imagem cair na própria palavra, e não na pausa seguinte.
- **Texto estrangeiro lido = tradução na tela (Toney):** nos posts do Al-Khaleej com legenda em árabe, ele escreveu a tradução que a narração lê, entre aspas, em Montserrat itálico branco, logo acima da legenda árabe ("Parabéns, era só brincadeira"; "perdemos pro Al-Ahli e vamos ter que aguentar a zoeira por uma semana.").
- **Seta seguindo o protagonista na multidão (Yamal):** em "deu um abraço rápido no Kane", seta vermelha (`imagens edição\seta vermelha e  inclinada.jpg`) com keyframes acompanhando o Yamal por 1,6s.
- **Flash só onde há virada:** tirou o flash do "ele admitiu" (selfie do Neymar) e o da prévia do Yamal caído no clássico. Essa prévia ele trocou pelo salão da cerimônia em "ainda pior pra ele": a imagem de lesão sugeria um fato que não aconteceu.
- **Flashback P&B no trecho de outra época inteiro, e só nele:** no CR7 o filtro parava antes do último shot da Copa 2022 (faltou `flashback` no shot 30), e ele esticou até 64,7s. No Piqué encurtou para só a foto antiga da manita e deixou colorido o telão do Camp Nou de 2010.
- **Música (os cinco):** a 2ª trilha do modelo acabava em ~66s, e ele esticou até ~1s antes do fim em todos. Levou a virada (fim da 1ª trilha + impacto "Dramatic" + entrada da 2ª) para a revelação quando o padrão caía longe dela: no CR7, "gol contra do Girotto" (36,6s); no Piqué, "o jogador que o Piqué tinha escolhido" (45,9s). Subiu o Dramatic de 0,12 para 0,24–0,43 e baixou a 2ª trilha para 0,08–0,10. O `capcut_projeto.py` faz isso agora, se a EDL marcar `"revelacao": true` (Passo 3b).

Décima sétima rodada, **Bruno Guimarães perde pênalti pro Fleetwood (28/out/2026)**, refinado no rascunho do CapCut (`analisa_capcut.py`). Legenda intacta. ~75% do corte ficou igual. O que ele mudou:
- **Gancho com o protagonista grande no contato:** eu abri no take da arquibancada atrás do gol (Bruno pequeno, de longe). Ele pôs por cima, nos mesmos 1,6s, o replay da TV por trás do Bruno, com punch-in de 1,25 para 1,58 e pan até o pé na bola. Arquibancada vale no gancho só se o protagonista for legível; senão, o replay fechado do mesmo instante.
- **Pan seguindo o rosto nos closes** (Bruno cabisbaixo, Arteta, Bruno sorrindo): a janela anda até o rosto ficar centrado, em vez de ficar fixa com ele na borda.
- **Defesa do goleiro:** a nossa janela corria para o lado depois da defesa; ele parou o pan no goleiro e na bola (o desfecho fica no quadro até o fim do shot).
- **Nome de quem comentou desfocado:** nos cards de comentário (Passo 3, item 22) ele desfocou o nome/usuário de cada comentarista (máscara retangular). Comentário anônimo entra sem o nome legível.
- **O comentário-clímax sozinho e grande:** os dois primeiros cards ficam empilhados; no último ("mas é teimoso", o mais curtido) ele tirou os outros e deixou só esse card, ampliado (1,0 → 1,31 com punch-in), sobre o replay do Bruno correndo para a bola. Refina a regra do Paquetá: a prova fica até o fim, mas a frase que fecha o vídeo tem o card dela isolado.
- **Narração:** tirou ~0,8s perto do fim, para a frase final chegar mais seca. Trilha e virada no `"revelacao"` ficaram como geramos.
- **Bug:** o `capcut_projeto.py` travava com 3 cards no mesmo shot (o 3º caía na CARDS2 em cima do 2º). Corrigido com a faixa CARDS3.

Loudness final e altura da legenda ele ajusta sempre no CapCut: no Palermo/Diogo publicou a -7 LUFS com a legenda a ~61%; no Raphinha, -10,3 LUFS com a legenda a ~70%. Os valores do Passo 6 e do Passo 7 são só o ponto de partida.

Em caso de dúvida sobre estilo, extraia quadros dessa referência (`scripts/folha_contato.py`) e compare. Ela vale mais que qualquer número escrito aqui.

## Onde trabalhar (regra fixa do usuário)

Tudo o que esta skill grava fica **dentro da pasta do vídeo**: `C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\Videos prontos\Shorts\<nome do vídeo>\`. Isso vale para `_montagem/`, `render/`, prévias, folhas de contato, EDL, JSONs, scripts auxiliares e os 2 vídeos da pasta `Videos prontos/` do próprio job.

- **Só leitura:** `logos\`, `Sons edição\`, `Musicas edição\`, `HUB Radar do Campo\` (inclusive `videos exemplos\` e `remotion-radar\`), a raiz de `Videos prontos\`, a própria pasta `Shorts\` e `Downloads\`. Nunca grave nem mova arquivo para elas.
- Narração ou material que chegou em `Downloads\`: **copie** para a pasta do vídeo e trabalhe na cópia.
- Arquivo temporário também vai para a pasta do vídeo (`_montagem/`), não para `/tmp`, scratchpad ou pasta geral.
- Os scripts têm uma trava (`scripts/pasta_job.py`) e abortam se a saída estiver fora de `Shorts\<vídeo>\`. Não contorne a trava.

## Ambiente (máquina local Windows)

- `ffmpeg`/`ffprobe`/`python` 3.11/`pip` no PATH. Dependências: `pip install faster-whisper opencv-python pillow numpy`.
- **Não use Remotion.** O compositor dele não consegue seekar vídeo 1440x2560 nesta máquina (falha com "No frame found at position"). O pipeline em `scripts/` é ffmpeg + PIL, e foi testado ponta a ponta.
- Não use `/tmp` no Git Bash para arquivos que o ffmpeg vai ler ou escrever: o ffmpeg do Windows enxerga outro caminho. Use a pasta do job (`_montagem/`).
- Render passa de 5 min: rode com timeout alto (~590s) ou em background.
- **Confira a versão antes de começar:** compare esta pasta da skill com a cópia do HUB (`diff -rq`). Se o HUB estiver mais novo (no Endrick a skill instalada ainda não tinha a v16), use os scripts e as regras do HUB e avise o usuário para reenviar o `.skill` pelo claude.ai.
- O `python` desta máquina é o da Microsoft Store e **não enxerga a pasta da skill** em `AppData\Roaming` ("No such file"). Antes de começar, copie `scripts/` e `assets/` da skill para `<job>/_montagem/scripts` e `<job>/_montagem/assets`, e rode as cópias. A trava de pasta continua valendo.

## Assets

Base: `C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\`

| Asset | Caminho |
|---|---|
| Marca d'água do canal | **não usa mais** (21/out/2026); `logos\` fica só como arquivo |
| Efeitos sonoros | `Sons edição\` (impactos: `impact-cinematic-boom-352465.mp3`, `impacto cinema 2.mp3`, `impacto cinema 3.mp3`) |
| Trilhas | `Musicas edição\` (normalmente o próprio usuário coloca a trilha) |
| Referências publicadas | `HUB Radar do Campo\Claude\videos exemplos\` |
| Fonte da legenda | `assets/Montserrat-Italic-VF.ttf` (nesta skill) |
| Prompt de títulos e tags | `assets/prompt_titulos_tags.txt` (modelo preenchido no fim de toda entrega) |
| Fonte da legenda no CapCut | `assets/Montserrat-ExtraBoldItalic.ttf` (instância fixa wght 800 do VF, usada pelo `capcut_projeto.py`) |
| Rascunhos do CapCut | `%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\` (o modelo dele é o mais recente que não começa com "Radar - ") |

## Scripts desta skill (em `scripts/`)

| Script | Faz |
|---|---|
| `narracao.py` | corta as pausas entre os trechos (velocidade original), marca os pontos de corte, transcreve palavra a palavra |
| `loop_final.py` | corta o fim da narração no começo da palavra que emenda com a abertura (loop) |
| `folha_contato.py` | folha de contato com tempo queimado, para achar trechos e pontos de entrada |
| `grade.py` | quadros lado a lado com grade de 10%: mede zoom/cx/cy/recorte e onde fica cada marca d'água antes da EDL |
| `prep_shots.py` | audita a EDL e gera os shots 1440x2560 60fps + o corte contínuo (completo e limpo); zoom que acompanha o lance (`keys`/`segue`), `recorte` de borda, `borrar` (ferimento), `destaque` (seta/círculo vermelho, ou `icone` PNG riscado com X), `flashforward` (gancho e replay do lance-chave) |
| `legenda_karaoke.py` | gera a faixa de legenda karaokê no padrão do canal e o `legenda_capcut.srt` (grafia certa, para ele importar no CapCut) |
| `limpar_marcas.py` | apaga marca d'água de terceiros clonando textura vizinha (chamado pelo `prep_shots.py` via `"tampar"`) |
| `revisao.py` | revisão obrigatória antes da entrega: um quadro a cada 0,1s, em folhas com tempo e número do shot, e as folhas `bordas_XX.jpg` com cada virada de shot a 30fps |
| `pasta_job.py` | trava usada pelos outros scripts: aborta qualquer gravação fora de `Videos prontos\Shorts\<vídeo>\` |
| `render_final.py` | junta corte + cor + marca + legenda + narração + SFX, normaliza o áudio e gera a prévia |
| `casar_fontes.py` | descobre de que clipe veio cada trecho de uma montagem feita pelo usuário |
| `guia_trilha.py` | grava `guia da trilha.txt` na raiz do job (chamado pelo `render_final.py`): onde a música entra, cai, sobe, bate e sai, no padrão das edições dele |
| `posfx.py` | transições do canal, marcadas por shot na EDL (`"fx"`): `flash` (clarão + soco de zoom), `flashback_in` (clarão + zoom + grade de arquivo P&B), `flashback` (só a grade). Roda depois do `prep_shots.py` e refaz os cortes; pode rodar de novo depois de rerenderizar shots |
| `compara_edicao.py` | compara a nossa entrega com a versão que o usuário refinou no editor: trechos de imagem trocados (por região da tela) e janelas de áudio diferentes |
| `lado_a_lado.py` | folha com o nosso vídeo em cima e o dele embaixo, no mesmo tempo, para ver o que ele trocou |
| `capcut_projeto.py` | gera o rascunho editável no CapCut a partir da EDL, em cima do rascunho-modelo dele (Passo 9) |
| `compara_capcut.py` | compara o `draft_content.json` que geramos com o que ele salvou no CapCut: shots trocados, zoom, posição, keyframes, faixas e volumes (diferença de ±0,01s em início/duração é arredondamento do CapCut). Para regerar o original: `capcut_projeto.py "<job>" --nome "Radar - <título>" --modelo "<modelo>" --raiz "<job>/_montagem/cmp/capcut_orig"`, **rodando de dentro de `<job>/_montagem`** (os cards da EDL são caminhos relativos a ela) e com `PYTHONIOENCODING=utf-8` |
| `analisa_capcut.py` | comparação minuciosa do rascunho gerado x o salvo por ele, corte a corte, com a frase narrada, a nota do shot, máscaras, efeitos, animações, textos novos e faixas por cima (`<job>/_montagem/cmp/analise.txt`) |
| `pares_quadros.py` | mosaico nosso x dele (exportado) nos tempos dados, 4 pares por linha, com rótulo |
| `artes_print.py` | `card`: recorta um comentário do print e faz o card com sombra; `documento`: súmula/comunicado em tela cheia com o trecho lido realçado em amarelo sobre o lance desfocado (Passo 3, item 22) |

Use os scripts. Cada um carrega a correção de um erro que já aconteceu (estão no fim da skill); reescrever do zero traz os erros de volta.

## Hub: a pauta acompanha o trabalho (desde 30/out/2026)

Pedido do usuário em 30/out/2026: "todo o processo de escolher os roteiros, garimpagem e montagem do vídeo sincronizado certinho com as pautas e a esteira do Hub". Cada vídeo é uma **pauta** no Hub (radardocampo.online → Vídeos → Pautas), e a esteira anda: pauta → roteiro → garimpo → montagem → pronto → no ar. Esta skill só leva a pauta até Montagem; Pronto é da `titulos-e-tags`. Esta skill avisa o Hub pelo script `hub.py`:

    python "C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\radardocampohub1.0\scripts\hub.py" --fonte montagem-de-video <comando>

- **Comandos:** `buscar [termo]`, `ler <id>`, `criar "<título>" [--etapa E] [--notas-arquivo F] [--roteiro-arquivo F] [--refs-json F] [--proximo-prompt-arquivo F]`, `etapa <id> <etapa> [--nota "..."]`, `atualizar <id> [--roteiro-arquivo F] [--notas-arquivo F] [--pasta P] [--arquivo "rótulo=caminho"] [--titulo T] [--proximo-prompt-arquivo F] [--etapa E] [--nota "..."]`, `prompt <id> <arquivo> [--etapa E]` (só o prompt do próximo passo), `clipe <id> <url> [--tipo clipe|referencia] [--trecho gancho|lance|torcida|reacao|contexto] [--inicio 0:12] [--fim 0:25] [--nota "..."]`, `clipes <id> <lista.json>`. Saída em JSON.
- **Achar o id da pauta:** procure a linha `PAUTA DO HUB: <id>` no pedido (o botão "Copiar prompt" do Hub e os prompts de chat novo das skills trazem essa linha). Sem ela, rode `buscar "<jogador ou time>"` e use a pauta que bater; se nenhuma bater, crie uma.
- **Passe o id adiante:** todo prompt para chat novo que esta skill gerar leva `PAUTA DO HUB: <id>` na primeira linha depois do pedido.
- **O prompt do próximo passo vai para a pauta (desde 31/out/2026).** O prompt de chat novo que esta skill entrega é gravado na pauta com `--proximo-prompt-arquivo <arquivo>` (ou `prompt <id> <arquivo>`). O Hub mostra o bloco "Prompt para o próximo passo" com botão de copiar, e ele cola num chat novo direto de lá.
- **O fluxo só termina com o "Fechamento obrigatório: Hub"** (última seção deste arquivo). Pedido de 31/out/2026: a esteira anda sozinha quando cada fluxo termina, sem depender de alguém lembrar de chamar o `hub.py`.
- **O Hub nunca trava o vídeo.** Se o `hub.py` der erro (sem internet, senha ausente, pauta excluída), diga em uma linha na resposta e siga o trabalho. Nunca peça para o usuário consertar o Hub no meio da rotina.
- Arquivo temporário para o `hub.py` (roteiro, lista JSON) segue a regra de pastas desta skill.

## Passo 0 — Insumos e perguntas

**Hub:** o id da pauta vem da linha `PAUTA DO HUB` do pedido ou de `<job>/_registro/pauta_hub.txt` (o garimpo grava). Sem nenhum dos dois, `buscar` pelo protagonista. Ao começar: `atualizar <id> --etapa montagem --pasta "<job>" --nota "montagem começou"`.

Olhe a pasta do job inteira antes de perguntar qualquer coisa: roteiro (`.txt`/`.docx`), `clipes/` com **todas** as subpastas (`apoio/`, `_extras/`, `_rejeitados/`, `_duplicados/`), `inventario.json` e a narração. Se o roteiro estiver vazio, avise e use o texto que o usuário mandou no chat, salvando-o como `roteiro.txt` para a legenda.

A narração é gerada pelo **próprio usuário no Google AI Studio** (Gemini 2.5 Pro TTS, voz Puck). Pela API esse modelo não tem cota no plano dele, então não gere narração por conta própria. Se o job não tiver narração, peça.

**Frase-ponte de loop:** antes de ele gerar a narração, confira se o roteiro termina com uma frase que repete a abertura (ex.: abertura "O jogador mais rico do mundo tá desempregado." → fim "…Minuto em campo, não. É por esse motivo que o jogador mais rico do mundo tá desempregado."). Se não terminar, **sugira a frase-ponte** para ele colar no AI Studio. Ela liga o fim ao começo, e o `loop_final.py` corta a narração no começo da repetição.

**Confira a narração contra o roteiro** (transcrição do Passo 1): se um trecho do roteiro não foi falado, avise antes de montar. A narração do Faiq pulou a abertura "Todo mundo tá falando que…" e ninguém percebeu. A do Raphinha não falou "sábado, em Calcutá" e trocou "inédito" por "difícil"; o vídeo saiu assim. Liste cada diferença (palavra pulada ou trocada) com o tempo, para ele decidir se gera o trecho de novo.

**Mais de uma narração na pasta:** às vezes ele gera duas ou mais (no Bernal, a das 16h16 e a das 16h17). Transcreva todas, compare com o roteiro e use a que tem menos erro de pronúncia e nenhuma frase faltando. A das 16h16 dizia "Amal", "procedor" e "pescorso". Diga na entrega qual usou e por quê.

**Entrega = 2 arquivos, sem logo do canal (pedido do usuário em 21/out/2026).** Ele sempre abre no CapCut, refina e exporta a versão final de lá, e deixou de usar a logo. Acabaram o `video pronto para o TIKTOK`, o `video pronto para o YOUTUBE`, o `com-legenda-sem-marca` e o 5º arquivo com SFX. O `render_final.py` gera só:
- **`<apelido>-com-legenda.mp4`:** o completo (cor + legenda karaokê + narração).
- **`<apelido>-sem-legenda.mp4`:** **base de edição**, o corte em 9:16 cheio com cor e narração, sem legenda.

Nenhum dos dois leva lupa, "Radar Do Campo" nem outra marca do canal, e o rascunho do CapCut (Passo 9) também não traz as faixas de logo do modelo.

**Transições (padrão desde 28/set/2026):** marque `"fx"` na EDL e rode `posfx.py`. `flash` nos momentos-chave (gancho, revelação, lance-chave, virada de bloco), `flashback_in` no primeiro shot de um trecho de outra época e `flashback` nos seguintes desse trecho. As transições entram nas 2 entregas. Ele pediu no Ronaldo e no Arrascaeta e manteve nos dois.

Pergunte só sobre **SFX**: quer efeitos nos impactos? Se quiser, monte o `sfx.json` e ele entra **só na faixa SFX do rascunho do CapCut** (Passo 9); as 2 entregas saem sem SFX (não passe `--sfx` no `render_final.py`). O `render_final.py` grava `guia da trilha.txt` na raiz do job (entrada, queda, revelação, degrau, batidas e saída, no padrão dele); avise na entrega. A trilha é o usuário quem coloca no CapCut (no Faiq ficou ~14 dB abaixo da voz; no Ronaldo e no Arrascaeta começou ~15 dB abaixo e subiu em degraus até ~8–10 dB); não adicione música sem ele pedir.

## Passo 1 — Narração: cortar as pausas e medir

    python scripts/narracao.py "<job>/Narração.wav" "<job>/_montagem"

A narração **não é acelerada**. O script corta os silêncios entre os trechos: cada pausa de 0,12s ou mais (a -30 dB) vira uma respiração de **0,12s** (`--manter`), e o silêncio do começo e do fim sai quase todo. Pausas curtas dentro da frase ficam como estão. Isso vem antes de qualquer outra coisa, porque as emendas, os tempos das palavras e a duração da EDL dependem dessa linha do tempo nova. As emendas ficam em `pausas.json` e são os pontos de corte da montagem.

Só mude a velocidade (`--vel`) ou a respiração (`--manter`) se o usuário pedir. O padrão é `--ruido=-30dB --min-pausa=0.12` (o antigo -35 dB/0,15s achou só 2 pausas nas narrações do Kane e do Atlético-GO; o novo achou 22 e 38). Se ainda sair poucas emendas (menos de uma a cada 4s), tente `--ruido=-28dB` ou `--min-pausa=0.10`. **Valor negativo vai com `=`**: `--ruido -30dB` quebra o argparse. O script imprime quanto silêncio saiu. Confira que nenhum silêncio de 0,12s ou mais sobrou na `narracao_final.wav`.

**Mínimo de 60s (regra do usuário, out/2026).** O vídeo final, depois do corte de pausas e do `loop_final.py`, **nunca fica abaixo de 60s**. Acima disso tudo bem (73s foi aceito no Endrick x Roma). Se ficar abaixo, **primeiro estique as respirações com a mesma narração**: rode de novo com `--manter` maior, até ~0,2s. O ganho é o número de emendas vezes a diferença. No Andreas (18/out) eu parei e pedi narração nova para 59,2s, e ele respondeu "ajuste os cortes para que fique em 60 segundos com essa mesmo". Com `--manter 0.17` nas 25 emendas, deu 60,19s, sem acelerar nem cortar fala. Só se nem com ~0,2s chegar a 60 pare antes da EDL e proponha uma frase a acrescentar (só fato confirmado) para ele gerar de novo.

## Passo 1b — Loop no final

    python scripts/loop_final.py "<job>/_montagem"

Se a narração terminar repetindo a abertura, o script corta no começo da palavra de emenda: na abertura "o jogador…", corta em "…que o J|". A palavra cortada sai da legenda, e a EDL usa a duração nova. Se não houver repetição, ele não mexe em nada. Ele também reconhece a **ponte de continuação** (Endrick, set/2026): a narração termina em aberto ("…esse vai continuar sendo só o dia em que…") e a abertura completa a frase ("O Endrick levou a mão na cara"). Nesse caso não há o que cortar, e o script avisa que a ponte existe. Os dois tipos valem como frase-ponte; só sugira uma ao usuário quando o fim não repete nem fica em aberto. **Mesmo assim a imagem tem que fazer loop** (Passo 3, item 4): o loop visual é obrigatório em todo vídeo, com ou sem frase-ponte no roteiro.

## Passo 2 — Conhecer o material por trecho, não por clipe

O que decide a qualidade da montagem é achar os bons trechos. Um clipe não é "bom" ou "ruim"; ele tem janelas usáveis.

1. Leia o `inventario.json`. Se ele trouxer `janelas` por clipe, parta delas.
2. **Abra todo clipe que não tiver janelas registradas**, inclusive os de `_extras` e `_rejeitados`, com `folha_contato.py` (passo de 2–3s no clipe inteiro). O melhor material do job Carrascal estava em `_extras`, marcado como "não verificado".
3. Em cada clipe, procure e anote (clipe, entrada, saída, o que mostra):
   - **takes longos de torcida** (arquibancada, celular) que acompanham o lance ou o protagonista. São a base do vídeo.
   - **o protagonista identificável**: rosto e nome/número no mesmo quadro (comemorações costumam ter isso), e planos dele andando ou se posicionando em campo.
   - **o plano aberto do lance-chave**, com o campo inteiro visível, e qualquer **círculo ou seta de destaque** marcando o protagonista. Isso é estilo do canal (aparece em vídeos publicados), não é sujeira.
   - **trechos com texto, logo ou webcam queimados**: dá pra aproveitar se o texto estiver numa faixa longe da ação e um zoom tirar ele do quadro.
4. React, compilado e vídeo com legenda queimada descartam **o trecho** ruim, não o clipe.
5. **Evento da noite anterior:** antes de montar, faça uma busca rápida (TikTok, 2–3 termos) pelo momento do gancho, o rosto do protagonista na hora do fato. No Yamal (27/out/2026), o vídeo dele sentado no instante do anúncio foi postado de manhã (@kart_x), depois do garimpo, e o usuário baixou por conta própria para trocar o gancho.

## Passo 3 — Montar a espinha pela torcida e pelo protagonista

Quebre a narração em trechos pelas pausas e marque o que cada um precisa mostrar. **Antes de pensar em torcida, classifique cada trecho:** é o lance/ação, é fala genérica, ou é **fato** (placar, retrospecto, título, declaração, data)? Fato pede a imagem daquele fato (item 10); torcida nunca cobre fato. Depois escolha as imagens nesta ordem de preferência. O motivo: o canal vende "a gente estava lá olhando esse jogador". Filmagem de torcida passa isso e ainda foge do Content ID; transmissão picada parece compilado de TV.

1. **Take de torcida que cobre o trecho.** Se o mesmo take cobre vários trechos seguidos, **segure o plano** e só corte quando o conteúdo mudar. Na referência, "contra-ataque puxado → sai cara a cara → finaliza em cima do adversário → gol feito, perdido" é um único take de 7,5s.
2. **Transmissão** só onde a torcida não pegou bem (close do lance-chave, gol do adversário) e como 2º ângulo do lance-chave.
3. **Falas genéricas** ("virou assunto nas redes", "na verdade já tinha acontecido", "quase ninguém percebeu"): **o protagonista na tela** (andando, se posicionando, reagindo), não torcida genérica. Torcida e estádio só quando a fala é literalmente sobre eles.
4. **Loop visual obrigatório (regra do usuário, set/2026), mesmo quando o roteiro não tem frase-ponte.** O último plano termina exatamente onde o primeiro começa: **mesmo clipe**, e a saída do último shot (`in + duração`) igual ao `in` do primeiro, com tolerância de 1 quadro. Quando o vídeo repete no TikTok/Shorts, a imagem continua sem pulo, como se fosse um take só. Na prática:
   - Escolha para abrir um take do protagonista que tenha uns 2–3s **antes** do ponto de entrada. O fim do vídeo usa esses segundos anteriores, e a abertura começa no quadro seguinte.
   - Se o take de abertura não tiver frames antes, inverta: feche com o take e abra no quadro seguinte ao fim dele.
   - O `prep_shots.py` barra a EDL se o último shot não emendar no primeiro.
   O começo continua fisgando ("esse é o cara"), e o final emenda no começo.
   - Se houver um **close bom do rosto do protagonista** (reação forte: riso, grito, choro), ele é ótimo para o loop: no Ronaldo, o usuário abriu e fechou o vídeo no mesmo close dele rindo (~0,5s no começo, ~1s no fim).
5. **Confirmação:** um take de torcida vale como prova do lance quando a jogada visivelmente bate com a narração (sequência, posição, cor do goleiro, placar), mesmo sem o número legível. Plano genérico nunca é apresentado como o lance. Rosto de jogador que você não consegue identificar não entra como se fosse o protagonista.
6. **Sem repetir frames.** Um clipe pode voltar (a abertura que se repete no fim é outro trecho do mesmo clipe), mas nunca os mesmos quadros. Duas exceções, ambas com `"flashforward": true` na EDL:
   - o gancho (item 9), que pode ser a prévia do clímax que reaparece depois;
   - **o lance-chave passado duas vezes seguidas, como replay**, quando a narração fica nele por um bloco inteiro (~6–9s): a 1ª passada com a seta ou o círculo (`destaque`), a 2ª limpa ou mais fechada. No Raphinha, a lesão contra a França cobriu "lesão na coxa de novo… cinco semanas parado… fora das quartas da Champions" assim, e ficou melhor do que cortar para outro jogo.
7. **Imagem literal quando a fala nomeia um grupo ou uma coisa.** No Faiq, o usuário trocou duas escolhas minhas:
   - "não jogou um único minuto pelo **time principal**": entrou **o próprio time campeão erguendo a taça**, no lugar do estádio vazio
   - "**dinheiro** pra comprar o clube inteiro": entrou **o palácio**, no lugar da torcida

   Prefira o literal mesmo quando é vídeo oficial de clube. Registre o risco de Content ID na nota, mas não troque por algo genérico só por isso.

   Quando a fala é **sobre o lance**, mostre **o vídeo do lance**, não o post ou print de outro perfil com texto em cima. No Matheuzinho, usei o post da GE TV ("1000 de aura pro Matheuzinho") em "vira print na hora", e o usuário pediu "apenas o vídeo do lance ao invés dessa print". Use só a faixa do vídeo, enquadrando sem o card.

   Quando a fala descreve uma **ação** ("se machucaram justamente comemorando", "corre pra festejar"), mostre a ação acontecendo, não a consequência. No Palermo/Diogo, eu cobri "esses dois jogadores se machucaram justamente comemorando" com o Palermo na ambulância. O usuário trocou pelo Palermo pulando para a torcida e pelo amontoado.

   Fala que descreve o protagonista ("lateral do Corinthians", "primeira convocação", "ele mesmo disse") pede **ele** na tela: foto, entrevista, close. Elenco genérico de agasalho ou aquecimento aleatório pareceu "fora de contexto" para o usuário. E "o herói do último lance" pede o close do herói, não jogadores pequenos vistos de longe.

   Fato **emocional** do protagonista (eliminação, ficar no banco, "sem entrar em campo", lesão) pede **o rosto dele naquele momento**, não o plano aberto do jogo. No Ronaldo, "sem entrar em campo" (Euro 2008) estava coberto com o árbitro num plano aberto; o usuário trocou pelo close dele chorando. O banco, com o técnico na frente, virou enquadramento fechado nele.
8. **Identidade:** confira que o rosto é mesmo do protagonista antes de usar close como se fosse ele. Clipe de família real ou de evento tem parentes parecidos. No Faiq, o rapaz de farda branca do banquete provavelmente é o príncipe Abdul Mateen. No Palermo/Diogo, a foto "Paulo Diogo" da Wikimedia era de outra pessoa (cabelo curto). O Diogo do Servette tem cabelo comprido. Confira a foto contra os quadros do lance. **Sem identidade confirmada, a foto não entra.** Em foto de grupo (elenco abatido na eliminação), só use se ele estiver visível e reconhecível (cabelo, tatuagem, número) e enquadre nele.
9. **Gancho (0–3s) = prévia do momento mais forte do roteiro, o LANCE em si** (a comemoração no alambrado, o muro caindo), cortado antes do desfecho. Ele repete no meio do vídeo quando a narração chega lá (`"flashforward": true`). Quando o usuário pede "mostre a parte que ele perde o dedo", ele quer o lance no alambrado, não a mão ferida: o ferimento só aparece no momento dele na narração, e **sempre desfocado** (`"borrar"`, Passo 5) para não ter restrição. No Palermo/Diogo, abri na mão desfocada, e ele trocou pelo Diogo subindo e pendurado na grade em plano aberto. O loop fecha com o Diogo correndo para o alambrado, e o vídeo recomeça com ele pendurado.

   **O gancho tem uma pessoa reconhecível fazendo algo, nunca a massa.** Torcida de pé aplaudindo, mesmo sendo o clímax do roteiro, foi trocada (Modric, 02/out/2026) pelo Yamal agachado sentado na bola. Quando a frase de abertura é um fato coletivo ("a Espanha meteu 4 a 1"), abra no rosto ou no gesto de quem representa o fato. **Se existe filmagem de arquibancada do mesmo momento do gancho, prefira-a à câmera da TV** (Endrick: o bolo inteiro visto da arquibancada, na altura dos olhos, no lugar da câmera alta com ele já no chão). Antes de fechar o gancho, procure no garimpo (e peça busca extra, se faltar) um take de torcida desse momento.

   **Roteiro sobre um padrão** (lesões repetidas, sequência de erros, maldição): o gancho é **a imagem mais forte do padrão**, não o evento mais recente. No Raphinha, o roteiro abria no corte depois da Austrália, e o usuário abriu na lesão da Copa (ele agachado com a comissão), que é a mais grave, com o ícone de "cortado" sobre a cabeça dele (item 15).

   **Gancho = ação, nunca objeto parado.** Quando o roteiro abre num fato genérico ("a Argentina meteu 4 a 0") e a revelação é um detalhe visual (o número nas costas), abra no **protagonista da revelação em movimento com a pista na tela**, sem entregar a resposta: no camisa 10, o Nico Paz pulando de costas com a 18 (o espectador vê um número, a revelação explica que não era o 10). A camisa pendurada no vestiário, que eu tinha escolhido, foi recusada. Marque `"revelacao": true` no shot da revelação (o `guia_trilha.py` usa).

   **O gancho é o auge em si, não o que vem antes dele.** No Atlético-GO o auge era o goleiro gritando "é pra você, falastrão!" para o camarote. Eu abri no apito final (ele correndo e ajoelhando) e só depois o grito, e o usuário achou que não prendia. O certo foi abrir no grito já no quadro 1 e usar o apito no fim, emendando no loop. Se a história é uma reação (grito, briga, gesto), o gancho é a reação acontecendo, não a caminhada até ela.
10. **Fato narrado = imagem do fato, de qualquer data.** Retrospecto ("não ganhava do rival em 2026", "quatro clássicos, uma derrota, três empates"), título ("viu o rival ser campeão"), jogo anterior e declaração ("o presidente foi a público cobrar o elenco") pedem **o próprio fato**: placar final daquele jogo na tela, o rival comemorando, a taça, o rival campeão na festa, a coletiva em que ele falou. No Atlético-GO eu cobri esse trecho com a torcida do Goiás na Serrinha, e o usuário disse "colocados meio sem contexto e mostra muita torcida". Esse material é de **outras datas**: se o garimpo não trouxe, volte ao garimpo antes de montar (compactos de jogos anteriores, final do estadual, coletiva completa) em vez de tapar com torcida. A meta de % de torcida do Passo 5 **não** vale para esses trechos.

    Dois refinamentos (Raphinha, set/2026):
    - Fato de outra data **filmado da arquibancada** vale mais que a transmissão, e o **telão do estádio com o placar e o tempo** é a prova de que é aquele jogo: deixe o telão no quadro.
    - A **consequência** que vem na mesma frase do fato ("cinco semanas parado e ficou fora das quartas da Champions") pode seguir no lance do fato (item 6, replay), em vez de cortar para um terceiro jogo. O usuário não usou o Barcelona x Atlético que tínhamos baixado. Troque de imagem quando a consequência vira assunto próprio, numa frase só dela.
11. **Prévia de suspense.** Quando a revelação é um detalhe visual (o pé de apoio tocando a bola, a mão no lance), mostre logo depois do gancho **o replay que vai revelar, cortado imediatamente antes do detalhe**, em câmera lenta (0,25–0,5x) e com o círculo/seta já apontando o lugar. É um `flashforward` curto (1–1,5s); a revelação completa entra só no momento dela na narração. No Kane: rosto dele em "só apareceu no replay", depois o replay da ESPN com círculo na bola a 0,27x, parando antes do pé escorregar. Confira a posição do círculo no shot renderizado: no primeiro render ele ficou ao lado da bola.
12. **O lance do gancho volta inteiro, num take contínuo.** Quando o gancho é a prévia do lance-chave (`flashforward`), no momento dele na narração o lance reaparece **no mesmo clipe, sem cortes**, do começo da jogada até o desfecho, em velocidade normal, cobrindo a frase toda. No Arrascaeta, "escorregou sozinho, caiu com o braço esticado e o punho esquerdo quebrou" estava picotado em 4 cortes (círculo vermelho em câmera lenta, replay fechado, close caído); o usuário trocou pelo take contínuo do gancho (domínio → escorregão → queda → ele no chão), ~4s, e só então um close. Ângulos extras (círculo, replay) só depois do take inteiro, se sobrar narração.
13. **Assistência e gol: o lance, com qualidade; se não houver, o rosto dele.** Frase sobre o que o protagonista fez ("deu a assistência", "fez o gol", "marcou o segundo") pede **o lance em si** com qualidade: ele e a bola grandes e legíveis, a jogada acontecendo. Se só existir o lance com os jogadores pequenos e parados, ou borrado, use **o close da reação/emoção dele** naquele momento (comemorando, gritando, sorrindo). **Nunca** o lance com jogador pequeno e parado. No Arrascaeta, "deu assistência do primeiro gol e fez o segundo" estava num compacto 1080p horizontal com os jogadores minúsculos; o usuário trocou por closes dele sorrindo e gritando na comemoração (regra dele, 29/set/2026).
14. **Gol e pênalti narrados: o plano contém o chute e termina na bola na rede.** Um ângulo bonito (câmera de trás da trave, cinematográfica) que começa depois do chute não serve: o espectador tem que ver o contato com a bola. Confira o primeiro e o último quadro do shot: o 1º antes do chute, o último com a bola entrando ou já na rede (ou o goleiro caído com a bola visível no gol). Se a transmissão escolhida sai da bola antes do gol, use `keys` para acompanhar ou troque de fonte. No payoff, quando o gancho já mostrou o lance, prefira **outra fonte do mesmo lance** (outra emissora, com o placar de TV na tela) em vez de repetir os mesmos quadros. No Vini x Austrália, o usuário trocou o pênalti do Raphinha (TNT, goleiro já no chão) pela transmissão aberta da ge e o quarto gol (repetição do gancho, câmera saindo da bola) pela transmissão com o placar 2x3, até a bola na rede.
15. **Ícone simbólico sobre o protagonista** quando a frase de abertura é um veredito ("foi cortado", "foi demitido", "foi banido"). No Raphinha, o usuário pôs o **escudo da CBF riscado com um X vermelho** sobre a cabeça dele no gancho e repetiu no shot de loop. Use `destaque` com `"tipo": "icone"`, `"arquivo"` (PNG sem fundo do escudo do clube ou da seleção, pedido ao garimpo) e `"riscar": true`, com `x`/`y` logo acima da cabeça e `tam` ~0,15–0,18. Deixe o ícone em quadro enquanto a frase do veredito durar (~1–1,5s) e confira no shot renderizado que ele não cobre o rosto.
16. **Parte do corpo nomeada = aproximar nela.** "Edema na parte de trás da coxa" → punch-in na parte de trás da coxa dele; "sempre na coxa" no infográfico → zoom nos marcadores da coxa. Vale para joelho, tornozelo, mão ("o punho quebrou"). O punch-in dele é um **corte seco para um quadro mais fechado do mesmo take**: o shot seguinte continua o mesmo clipe, sem pular tempo (`in` = saída do anterior), com `zoom` ~1,8–2,2 e `cx`/`cy` na parte do corpo (corte Tipo B, na palavra). Aproxime no tempo da palavra, não antes. Confira o upscale (≤2,2x) e, se passar, use uma fonte mais fechada do mesmo momento.
17. **Lugar nomeado = imagem do lugar.** "Fora do jogo contra a Índia, em Calcutá": se o jogo ainda não aconteceu, mostre o estádio ou a cidade, de qualquer data (no Raphinha, um estádio de Calcutá lotado num evento de 2025). A fala não afirma que aquilo é o jogo, então a data da imagem não importa.
18. **Enumeração = um corte por item, no tempo de cada palavra.** "Março, junho, setembro" → três cortes de ~0,5s, cada um na imagem de um item já mostrado no vídeo (a lesão de cada mês). Serve para listas de jogos, títulos e datas: é um resumo visual que amarra o que veio antes. Os cortes caem nas palavras, mesmo fora de pausa (Tipo B).
19. **Instituição na pergunta ou na acusação = o rosto de quem a representa.** "A Seleção tá sugando o Raphinha?" → close do Ancelotti por ~3s. Clube → técnico ou presidente; CBF → presidente; arbitragem → o árbitro do lance. Nunca escudo parado ou estádio vazio.
20. **Dado-resumo ou estatística = infográfico de portal**, quando o garimpo trouxer um (365Scores, ge, OneFootball): "sempre na coxa… quarta lesão em um ano" → arte "ALERTA LIGADO" com o corpo e as lesões marcadas, em tela cheia (foto entra como clipe: `prep_shots.py` trata imagem igual a vídeo) e, na palavra do dado, corte seco para a mesma arte com zoom no dado (item 16). A marca do portal sai por enquadramento (Passo 5). Se o usuário limpar ou ampliar a arte num editor de IA, **confira as letras pequenas**: no Raphinha a IA reescreveu "COXA" como "COSA", "Zona do Mundo" como "ZORA DO MONSO", "Amistoso" como "AMISTERO", e inventou um escudo no lugar do da Austrália. Prefira enquadrar a parte sem texto miúdo ou avise o usuário. Isto é diferente da regra do Matheuzinho (item 7): lá o print de post **substituía o vídeo do lance**. Infográfico é bem-vindo quando ilustra um **número ou histórico**, que não tem vídeo.
21. **Roteiro de incidente (desmaio, lesão, briga, socorro): o evento inteiro em ordem cronológica** (Bruno Duarte, 08/out/2026, aprovado sem mudanças). O gancho é a prévia do pico (item 9). Quando a narração chega no incidente, cada frase pega **o momento seguinte do mesmo evento**: início da jogada → contato → queda → no chão → reação dos outros → socorro → maca → substituição, até o desfecho. Não volte no tempo nem corte para imagem de outro assunto no meio. O usuário chama isso de "os vídeos se completarem".
    - Se um clipe cobre o evento todo (repost de transmissão de 40–60 s), use-o como espinha e intercale só o 2º ângulo (replay, arquibancada) do mesmo instante.
    - Frase maior que o trecho: estique com 0,6–0,75x no mesmo momento, não pule para outro.
    - Jogador ou bola sempre dentro do quadro, com zoom moderado (1,2–1,6) e `keys` seguindo a ação.
22. **Fala que cita comentário, documento ou post = o print real** (Bernal x Yamal, 18/out/2026). Isto é diferente do Matheuzinho (item 7), em que o print de post tomava o lugar do vídeo do lance. Aqui o assunto da frase é o próprio texto:
    - **"Nos comentários, chamaram ele de nova princesa…"**: o card com o comentário de verdade (nome, texto, curtidas) por cima do lance, entrando na palavra. Use `artes_print.py card` sobre o print que o garimpo trouxe e ponha na EDL como `destaque` `icone`, com `tam` ~0,86, um card por comentário citado. Pode empilhar dois (y 0,6 e 0,3) quando as frases vêm seguidas.
    - **"O árbitro escreveu na súmula…"**: a súmula de verdade em tela cheia, sobre um quadro do lance desfocado, com **o trecho que a narração lê realçado em amarelo**. Use `artes_print.py documento --variantes`: a versão limpa entra quando a frase começa, e a realçada no trecho da revelação. **O realce não pode cair na faixa da legenda** (48–60% da altura): no Bernal precisei subir o texto marcado, porque ele ficava embaixo da karaokê.
    - **"Pediu desculpas num story"**: o print do story (repost de jornal no X serve), com zoom lento.
    - **Comentário de anônimo: desfoque o nome do perfil** (`borrar` só sobre o nome no card). Com 3 comentários, o último (o mais forte) entra sozinho e maior, com punch-in, e os anteriores saem (Bruno x Fleetwood).
    - **Post ou legenda em outra língua que a narração lê** (Toney, 27/out/2026): a tradução em português, entre aspas, em Montserrat ExtraBold Italic branco com contorno preto, logo acima do texto original, enquanto a frase dura. Faça um PNG transparente com o texto e ponha como `destaque` `icone` (vai para a entrega e para a faixa CARDS do CapCut).
    - **Documento ou post lido:** além do realce, **punch-in até o trecho lido** (CR7: página da Liga de 2,27 para 3,03 em "Ronaldo 49'"; súmula de 1,5 para 2,0; Toney: post do relatório médico de 1,0 para 1,41 subindo até a lesão).
    - Isto refina a regra do Vini (rodada 12, "fato visual ganha da súmula em texto"): quando a súmula só narra um lance que existe em vídeo, mostre o lance. Quando a revelação **é o que está escrito** ("não precisou de atendimento médico e pôde continuar"), o documento é a imagem literal. Logo depois, volte à prova visual (o Yamal de pé).
23. **O que ele ajusta no CapCut em cima do nosso corte** (Andreas e Bernal, 18/out/2026). Faça já na EDL:
    - **Expulsão, cartão, "o motivo da expulsão"**: o cartão levantado tem que estar no quadro. Enquadre o árbitro com o braço e o cartão, não da cintura para cima. Se a logo da emissora entrar, a ação ganha (Passo 5, marcas).
    - **Objeto ou detalhe pequeno num plano aberto** (a bola extra caindo no gramado, a bola do jogo, o objeto atirado): **punch-in progressivo** com `keys` e `zoom` crescendo até o objeto ficar visível. No Andreas foi de 3,16 para 4,67 em ~2,5s, seguindo a bola. Aqui o plano aberto é o lance, não um plano de escala.
    - **Frase sobre relação no espaço** ("ela acertou a bola do jogo", "ele chutou a segunda bola"): o quadro tem que caber os dois elementos. No meio do lance em câmera lenta ele abriu de 1,75 para 1,19 depois do chute, para a bola extra e a bola do jogo aparecerem juntas.
    - **Gancho com punch-in no contato:** além da prévia cortada no impacto (item 9), feche o quadro no instante do contato (1,22 → 1,72 no Bernal), com `keys` seguindo os dois jogadores.
    - **Foto ou arte em tela cheia nunca parada:** zoom lento de ~1,0 para ~1,25 em 0,6–1s (arte "DONE DEAL" no Bernal), ou pan lento.
    - **Câmera lenta com pan seguindo a ação** (a cabeçada a 0,56x no Bernal), não janela fixa.
    - **Shot 1 e shot de loop com movimento** (rodada 14, os 5 vídeos): punch-in de ~1,0–1,2 para ~1,7 e/ou `keys` com pan seguindo a ação. Pan suave e no sentido da ação, nunca um salto de lado no meio do shot (Kannemann).
    - **Assunto no centro da janela:** confira a altura (`cy`) e o lado (`cx`) em cada shot. A pessoa que fala ou o lance no meio do quadro, não encostados na borda.
    - **Duas fontes do mesmo momento:** escolha a que não tem card nem texto queimado (Soteldo). Se só existe a com texto, `borrar` retangular só sobre o texto (Paquetá).
    - **Cards e prints da reta final ficam até o último quadro**, empilhados, em vez de entrar e sair (Paquetá).
    - **Gancho (rodada 16):** o pico físico (confusão, golpe, empurrão) ganha da provocação que veio antes (Neymar). Entre duas entradas do mesmo take, a que mostra o pico mais cedo (Piqué: +2,2s). Fato com rosto ("fez essa cara quando o Kane ganhou") = o rosto no instante do fato, com quem está ao lado, não um close de outro momento (Yamal).
    - **Close de rosto = cabeça e ombros, com quem está do lado.** Rosto da testa ao queixo, parado, foi trocado 3 vezes no Yamal. Foto nítida do mesmo momento (photo mode do TikTok, 1140–1284 px) com punch-in lento vale mais que vídeo fechado e mole.
    - **Gesto nomeado na frase** ("mão na frente da boca", "cobriu a boca"): punch-in de ~1,6–1,7 nele (Neymar).
    - **Pessoa nomeada:** o corte para ela cai na palavra, mesmo antecipando a emenda em 0,2s (Tipo B; Mbappé no Yamal).
    - **"O mesmo lance" na frase:** pode repetir os mesmos quadros do lance já mostrado (CR7).
    - **O detalhe que decide a polêmica** (a bola raspa ou não na cabeça): um take só, em câmera lenta progressiva (0,64x → 0,23x → 0,17x) até o contato, sem picar em círculo, seta e lupa (CR7).
    - **Ação inteira:** zoom que corta o corpo de quem chuta/cobra a falta é fechado demais (Félix 1,89 → 1,58). Gol narrado: pan até a rede (CR7, Toney).
    - **Flash** só em virada, revelação e lance-chave; nunca em selfie, entrevista ou prévia que não seja o pico.
    - **Flashback:** `fx` em todos os shots do trecho de outra época, até o último (no CR7 faltou o shot 30); foto antiga em P&B, vídeo de arquivo com placar/telão pode ficar colorido (Piqué).

Registre, por trecho, 2 ou 3 candidatos e a escolha, com o porquê. Isso vira a `nota` do shot. Se não houver alternativa, diga isso.

## Passo 3b — Plano de viralização (obrigatório antes da EDL, out/2026)

O usuário quer **todo vídeo pensado para viralizar**: gancho que prende, partes importantes inteiras e estrutura com picos. Antes de escrever a EDL, grave `_montagem/plano_viral.md` com estas três partes e confira cada item contra ele:

1. **Mapa de impacto do material.** Percorra o inventário e liste os 3–5 takes mais fortes de todo o garimpo (ação física, choque, multidão, contraste, rosto em emoção), com clipe, janela e **o segundo exato do pico** (contato, golpe, bola na rede, queda, grito). No Calcutá eram: o torcedor com a 10 da Argentina batendo a cadeira (pico 22,0–22,2s e 23,7–24,2s), o gramado do Salt Lake invadido visto do alto (Olé), o Messi cercado e sumindo no bolo de seguranças, a arquibancada vazia no apito inicial.
   - **O gancho é o pico nº 1 do mapa**, mesmo que pertença ao meio da história. Use `flashforward`, com o pico nos primeiros 0,5–1,0s, e corte logo depois do golpe, antes da consequência. Plano parado, de longe ou "bonito" não é gancho (no Calcutá abri num setor vazio com um grupinho, e não prendia).
   - Os outros picos vão nos pontos de virada: revelação ("e aqui vem o detalhe"), payoff e o último shot antes do loop. Nenhum pico do mapa pode ficar fora do vídeo sem justificativa escrita.
2. **Tabela frase a frase.** Uma linha por frase **inteira** da narração (não por pausa): o que a frase afirma → a imagem literal que prova ou mostra exatamente aquilo → clipe e janela. Regras:
   - A imagem tem que **dizer a mesma coisa que a frase**, de ponta a ponta. Se a frase tem duas ideias ("o estádio encheu de novo, mas o Messi ficou só 20 minutos"), são duas imagens, cada uma no tempo da sua metade.
   - **Pessoa citada = a pessoa.** "Um torcedor resumiu: é um buraco no bolso" pede o torcedor falando (havia um, na CNN, reclamando do ingresso), nunca arquibancada.
   - **Preço, data, número** pedem a prova (ingresso, cartaz, telão, matéria com o número, card de portal), não estádio genérico.
   - **A imagem nunca contradiz a frase.** "Bandeira do Brasil era difícil de achar" com um grupo agitando bandeiras do Brasil diz o contrário. Mostre o setor vazio sem as bandeiras, ou um plano aberto em que elas mal aparecem.
   - **Torcida/estádio genérico só é aceito quando a frase fala literalmente da torcida ou do estádio naquele momento.** Se a coluna "imagem literal" ficaria vazia, volte ao garimpo antes de montar (e diga ao usuário qual frase ficou sem imagem), em vez de tapar com torcida.
3. **Ações inteiras.** Para cada ação que entra no vídeo (golpe, chute, cadeira jogada, queda, invasão, gol), anote início e **pico**, e confira que o shot **contém o pico**: `in` antes do início da ação e saída pelo menos 0,3s **depois** do pico. Se a frase é curta demais para a ação inteira, estique o shot para dentro da frase seguinte (corte Tipo B), use 0,5–0,7x só na ação, ou mova o corte da frase. Cortar 0,1s antes do impacto joga fora o melhor momento.

Na entrega, diga em uma linha qual pico abriu o vídeo e onde ficaram os outros.

**Marque a revelação (27/out/2026):** `"revelacao": true` no shot em que a história vira, o fato que muda tudo ("gol contra do Girotto", "o jogador que o Piqué tinha escolhido levou amarelo"). Nenhuma das 5 EDLs de 24–27/10 tinha a marca, e ele moveu a música à mão. O `capcut_projeto.py` põe a virada da trilha nesse shot.

## Passo 4 — Ritmo

- Alvo: **~22–30 planos por minuto de vídeo final**, plano médio ~2–2,5s, com takes longos de 4–8s e inserts rápidos de 0,5–1s (reação, close, resumo de lista). A referência Carrascal tinha ~23; a montagem que ele fez do zero no Raphinha (set/2026) ficou em ~26–31, com o lance-chave segurado por ~8,5s e os inserts curtos concentrados no gancho e na enumeração.
- **Cortes de conteúdo (Tipo A) caem nas emendas** da narração (as pausas cortadas, tolerância ±0,12s). É o que evita o corte no meio da fala. `prep_shots.py` confere isso.
- **Troca de ângulo (Tipo B) é recurso, não cota.** Use quando não houver take contínuo ou para dar um 2º ângulo de um momento importante. Picar um take bom em vários ângulos deixa o vídeo com cara de compilado.
- **Lance-chave**, nesta ordem: plano aberto mostrando o lance inteiro (quem sai de onde, para onde vai) → círculo marcando o protagonista, se existir → close do momento → 2º ângulo. **Velocidade normal** por padrão. Câmera lenta só quando o lance é curto demais para a frase, e mesmo assim sem esticar o mesmo lance por muitos segundos.
- **"Plano aberto" não é plano em que a bola some.** Se na transmissão aberta a bola e o protagonista ficam minúsculos, ou um jogador em primeiro plano toma o meio do quadro, use o **replay fechado** que acompanha a bola e corte entre 2–4 ângulos seguindo a jogada: condução → chute → bola entrando (atrás da rede) → corrida para comemorar. No Palermo/Diogo, fiz o gol do Palermo num plano aberto fixo, com o camisa 7 do Levante no centro. O usuário trocou pelo replay do camisa 8 driblando o goleiro, com a bola na rede vista de trás.
- Sem cross-fade nem transição de pacote. Entre shots, corte seco; as únicas transições são as do canal via `posfx.py` (`flash`, `flashback_in`, `flashback`), nos momentos-chave e nas viradas de época (Passo 0).

## Passo 5 — EDL, enquadramento e qualidade

Escreva `edl.json` (formato no cabeçalho de `prep_shots.py`) e rode primeiro só a auditoria:

    python scripts/prep_shots.py "<job>/_montagem/edl.json" --saida "<job>/_montagem/render" --pausas "<job>/_montagem/pausas.json" --dur <duração da narração> --so-checar

Ela confere limites dos clipes, buracos, cortes fora de pausa e frames repetidos, e imprime planos/min, % de torcida e % de protagonista na tela, comparando com a referência. Se a torcida estiver abaixo de ~50% ou o plano médio abaixo de ~1,8s, reveja a seleção antes de renderizar, **mas não troque imagem de fato (Passo 3, item 10) nem lance/reação que só a transmissão pegou por torcida só para bater a meta**: no Atlético-GO, a versão aprovada tinha 45% de torcida; no Endrick, 25%, porque a trombada, o empurrão e os closes da confusão só existiam na TV. Depois rode sem `--so-checar`.

A auditoria também procura **corte de cena e fade dentro do trecho de cada shot**. Compilado, react e post de emissora têm cortes próprios e fade para preto nas pontas. Se o shot atravessa um desses pontos, aparece 1 quadro de outra cena "piscando" na tela ou um quadro escuro na virada. No Matheuzinho, o hino cortava para outra cena em 3,18s e o shot ia até 3,20s: o usuário viu a piscada logo no começo do vídeo. Quando a auditoria acusar, mude `in`/duração para ficar dentro do trecho limpo e redistribua o tempo com o shot vizinho (corte Tipo B, se cair fora de pausa). Só use `--sem-bordas` para depurar. Se um shot acusa corte em qualquer `in` que você tente (no camisa 10, a fila acusava sempre `in`+0,03s) e a folha a 30fps não mostra corte nenhum, é alarme falso: marque `"ignorar_bordas": true` **só nesse shot**, nunca desligue a checagem do vídeo inteiro.

**A auditoria não pega fusão (dissolve) da fonte**: a troca é gradual, sem salto de cena nem quadro escuro. No Atlético-GO, o placar 1x1 de um compacto fundia para outra cena em ~605s e só apareceu na revisão (Passo 8), como um "fantasma" de outro jogador sobreposto nos últimos quadros do shot. Em compactos e melhores momentos de emissora, olhe a folha de contato perto do fim de cada trecho escolhido. Testei um detector automático (quadro do meio ≈ média dos vizinhos) e ele não separou dissolve de pan de câmera; por isso a checagem é visual.

**`--shots` no PowerShell:** `--shots 01,41` vira um array e chegava ao script como "1 41" (o shot 01 era pulado sem aviso no camisa 10). Os scripts agora aceitam vírgula, espaço ou ponto e vírgula, mas passe entre aspas: `--shots "01,41"`.

**Tirar ou juntar um shot renumera todos**, e o `prep_shots.py` grava por número: depois de apagar o shot N, renomeie os `shotNN.mp4` de `completo/` e `limpo/` (N+1 vira N…) antes de rerenderizar só os alterados, ou rode tudo de novo.

Enquadramento, por shot:
- A janela é a maior 9:16 possível no clipe (`zoom` 1,0). O script corta antes de escalar (lanczos + nitidez), porque cortar depois de escalar borra.
- `zoom` > 1 para fechar no assunto ou tirar texto/logo queimado. `cx`/`cy` posicionam a janela. Quando um placar ou detalhe no canto é a prova do lance, trave a janela para ele ficar em quadro. No Carrascal, o bloqueio precisou de `cx` 0,351 para não cortar o placar "1º 02:42".
- **Tela cheia 9:16 sempre.** O usuário rejeitou a faixa 16:9 com fundo desfocado ("não gostei da forma com desfoque"). Também rejeitou o zoom excessivo que tira o contexto. O certo é o zoom só até a cena ficar legível, **com a janela andando para acompanhar a bola ou o lance**:
  - `"keys": [[t, cx], [t, cx, cy], ...]`: keyframes da posição da janela, com **t relativo ao início do shot** (0 = primeiro quadro do shot). No Endrick escrevi em tempo do vídeo final (40,18, 41,2…) e a janela ficou parada até pular no fim, com o gol fora do quadro. O `prep_shots.py` agora detecta keys absolutas, converte e avisa. É o mais confiável. Quando a fonte tem círculo/seta marcando o jogador, dá para rastrear a cor vermelha quadro a quadro e virar keys. Foi o que fiz no passe do Diogo, e o círculo ficou no quadro o lance todo.
  - `tracking: "segue"`: fluxo óptico, descontando o pan da câmera. Confira o resultado, porque ele se perde em amontoado. `"mov"` é o antigo (linear).
- `"recorte": [x, y, larg, alt]` (fração do fonte) tira a borda do repost (título, legenda do autor, marca no rodapé) **antes** do 9:16. Serve para vídeo de TikTok com a transmissão numa faixa no meio.
- **Resolução efetiva do assunto:** escolha a fonte do mesmo momento onde o assunto ocupa mais pixels, não o arquivo maior. Um TikTok 1080 com a transmissão numa faixa de 30% da altura tem menos pixels no lance que um 576 com o lance de tela cheia. A auditoria avisa quando o upscale passa de 2,6x. No Palermo/Diogo, usei o muro caindo de uma faixa pequena com zoom de 3,7x e ficou um borrão amarelo. O usuário usou outro ângulo, mais aberto e nítido.
- Upscale acima de 2,2x fica mole. Prefira outro trecho para o mesmo momento; se não houver, avise o usuário.
- **Plano de escala, lugar ou multidão não leva zoom (Calcutá, out/2026).** Quando o shot existe para mostrar **quanto** (estádio lotado ou vazio, multidão, invasão do gramado) ou **onde** (estádio, placa, cartaz, cidade), o contexto é o assunto: `zoom` 1,0 e upscale ≤ 2,2x. Recortar uma fatia de 9:16 de um panorama 16:9 (Salt Lake de 2011 com `cx` 0,22 e upscale 5,3x; hino com zoom 1,6) mata a informação: ninguém vê que estava cheio. Em ordem de preferência:
  1. uma fonte **vertical ou de celular** do mesmo momento ou do mesmo lugar;
  2. com uma fonte horizontal, `keys` fazendo um **pan lento** de um lado ao outro do panorama no tempo da frase, para revelar a escala;
  3. sem nada disso, outro plano.
  Zoom > 1,3 só serve para fechar numa **pessoa ou ação** pequena no quadro (punch-in, Passo 3 item 16), nunca num plano de contexto.
- **Ferimento/sangue:** `"borrar": [[t, x, y, larg, alt], ...]`, em fração do quadro final e animado no tempo, desfoca a área com borda suave e sem retângulo aparente. Cubra a área toda (a borda esmaece para fora) e confira de perto: sobra de vermelho nas bordas conta como defeito.
- **Seta ou círculo vermelho no protagonista** quando o quadro é confuso (amontoado, grade, vários jogadores iguais): `"destaque": [{"tipo": "seta"|"circulo", "x", "y", "ang", "tam", "t0", "t1"}]`, em fração do quadro final. `x`/`y` é a ponta da seta (ou o centro do círculo), e `ang` diz de onde a seta vem (135 = do canto superior esquerdo). No Palermo/Diogo, o usuário acrescentou à mão uma seta vermelha apontando o Palermo embaixo da grade caída. Ele **segurou esse plano** durante "o muro desaba em cima da perna dele… perna esquerda fraturada", em vez de cortar para o rosto. Enquanto a narração descreve a lesão, fique no plano que mostra a lesão acontecendo.

**Marcas d'água de terceiros (regra do usuário, set/2026):** no vídeo final só pode aparecer a marca do canal. Marca de perfil (WAMO, @fulano) e logo de emissora (ge, sportv, ESPN, TNT, Paramount+, 10) têm que ser escondidos. **O placar/relógio da transmissão pode ficar** quando prova o lance: no Vini x Austrália o usuário escolheu justamente o take com "2T 34:29 AUS 2x3 BRA" na tela para o pênalti decisivo. O usuário não quer borrão: o `delogo` deixa uma mancha que "ainda polui". Em ordem de preferência:
  0. **Meça antes de escrever a EDL**, com `python scripts/grade.py <saida.jpg> "<clipe>|<seg>|<rótulo>" ...` em cada fonte usada, **incluindo o rodapé e os primeiros 5s do clipe**. No Atlético-GO escaparam do enquadramento: um pedaço do logo da ITV no canto, "www.diariodegoias.com.br" no rodapé, a assinatura "@futebolgoiano1minuto" na borda de baixo e o card do post da ESPN (placar + texto) nos primeiros 4s do clipe. O último caso é típico do **shot de loop**, que volta alguns segundos antes da entrada do primeiro e cai no card de abertura do post: escolha a entrada do gancho de modo que o trecho do loop fique depois do card. **Assinaturas pequenas de perfil também contam**: no Arrascaeta escaparam "@BRAYANNCRF" (rodapé da faixa do vídeo), "SportyNet" (topo) e "FUTSTATUS" (canto superior direito), cada uma com poucos pixels, e só foram vistas na revisão com recorte ampliado. Em repost de TikTok com a transmissão numa faixa, meça onde a faixa termina e use `"recorte"` cortando **dentro** dela (acima da assinatura), não na borda preta. **Cards de texto do perfil no meio do lance** também contam: no Andreas, o "MDS olha essa expulsão" sobre a jogada, a logo da Band nos planos da comemoração e, no Bernal, a logo da CazéTV no topo dos shots 24 e 28 só apareceram na revisão. Meça também os trechos que você vai **reenquadrar** (a logo entra quando a janela desce).
  - **Logo atravessada no meio do quadro** (TyC Sports na altura da cintura dos jogadores): enquadre **acima** dela (zoom ~1,9 e `cy` ~0,26 no camisa 10) e acompanhe o jogador com `keys` `[t, cx, cy]` quando ele subir ou descer no quadro; se o enquadramento acima corta o assunto, troque de fonte.
  1. **Enquadrar sem a marca (padrão):** zoom leve + `cy`/`cx` que deixem a marca fora (ex.: WAMO no topo sai com zoom ~1,22 e `cy` ~0,59; ge no canto direito sai com zoom ~1,3 e `cx` ~0,385). Fica invisível de verdade. Meça onde a marca está (grade de 10%) e calcule a janela: altura = 1/zoom, largura = 0,5625×altura/proporção do fonte.
  1b. **A ação vale mais que o quadro sem logo** (Andreas, 18/out/2026): quando o único enquadramento com a ação inteira (o cartão vermelho levantado) deixa uma logo pequena no canto, ele enquadra a ação e cobre a logo com um **desfoque retangular pequeno** (máscara no CapCut). Faça o mesmo com `"borrar"` só sobre a logo, nunca com clone, e avise na entrega. Não corte a ação para fugir da logo.
  1c. **Confira cada caixa de `borrar` no shot renderizado, de perto** (CR7, 27/out/2026): a do "FIFA+" ficou 1% acima da logo, e ela saiu nos 5 shots da Copa 2022. Nos vídeos da ge, olhe o canto superior direito: o "g" sobrou em 4 shots do Neymar.
  2. **Trocar o trecho** quando o enquadramento que tira a marca também corta o assunto (rosto pela metade, lance fora do quadro) ou passa de ~2,4x de upscale. No Matheuzinho, o zoom 2,0 na zona mista da WAMO cortou o rosto e o usuário apontou "enquadramento ruim": troquei pela entrevista da ge, que sai limpa com zoom 1,72.
  3. **`"tampar"` só em fundo liso**, como logo sobre card branco ou céu, com `"de": "cor"`. Formato na raiz da EDL: `{"CLIPE": [[x, y, larg, alt] | {"box": [...], "de": "esq|dir|baixo|cima|cor"}, ...]}` em fração do quadro-fonte. O `limpar_marcas.py` também clona textura vizinha (`esq|dir|baixo|cima`), mas **o usuário vê a clonagem como "reflexo muito aparente"** sobre torcida, rosto, camisa e placa (Matheuzinho, set/2026). Clone só num pedaço minúsculo de gramado uniforme, e confira de perto.
  - **Legenda queimada da própria fonte** (as amarelas do post da ESPN com a fala do goleiro, no meio da tela) fica em cima da nossa karaokê. Se não dá para enquadrar sem ela sem cortar o protagonista, mantenha e **avise o usuário na entrega** com o intervalo exato, para ele baixar a nossa legenda no CapCut nesse trecho.
  - Um shot pode ter seu próprio `"tampar"` (sobrepõe o do clipe; `[]` = nada).
  - Depois de renderizar, **recorte de perto cada área tampada** e confira: o clone às vezes copia meio jogador, uma letra ou um rosto vizinho. Nesses casos, troque a direção (`de`) ou use o enquadramento. Para medir as caixas, extraia um quadro de cada clipe usado com grade de 10% e anote onde fica cada marca. Muitas marcas se movem ou mudam de tamanho: confira o shot renderizado, não só o fonte. Na varredura do Passo 8, procure marca de terceiro em todos os quadros; qualquer uma que sobrar bloqueia a entrega.

## Passo 6 — Legenda

    python scripts/legenda_karaoke.py --palavras "<job>/_montagem/palavras.json" --roteiro "<job>/roteiro.txt" --dur <duração> --saida "<job>/_montagem" --quadro <um quadro 1440x2560 do corte> --previa "<trecho de um bloco>"

Padrão medido na referência (o script já aplica):
- **Karaokê:** a palavra que está sendo falada fica amarela (#FAFE05), as outras brancas. O tempo vem do Whisper sobre a narração já com as pausas cortadas. Nunca estime o tempo.
- **Uma linha**, 2–3 palavras. O bloco fecha em ponto, vírgula e dois-pontos.
- Montserrat ExtraBold Italic, ~3,1% da altura (~80px), contorno preto + sombra preta difusa.
- **Centro a ~54% da altura.** Os vídeos publicados mais antigos usavam ~70–74%; a referência atual usa o meio da tela. O usuário ajusta a altura final no CapCut (~55% no Ronaldo, ~61–62% no Palermo/Diogo e no Vini, ~70% no Raphinha), então não gaste revisão com isso.
- **Grafia certa dos nomes é trabalho nosso**, porque a legenda automática do CapCut erra. Na versão dele do Palermo/Diogo saiu "servete contra shopping house", "Vila real" e "Guiness". Corrija o `palavras.json` do Whisper (nomes de clubes, números por extenso, palavras que o Whisper pulou) antes de gerar a faixa. Guarde o original como `palavras_whisper.json` e grave o texto corrigido também como `roteiro_legenda.txt` para o `--roteiro`. O Whisper erra com frequência nome estrangeiro e nome que vira duas palavras: em set/2026 saiu "e a Mal" (Yamal), "Greer" (Guéhi), "Oyer Zarbao" (Oyarzabal), "Julien" (Julián), "Atlético Goiano" (Atlético-GO), "tira o livre" (tiro livre), "travição" (travessão). Quando um nome vira várias palavras, junte num só item com o `ini` da primeira e o `fim` da última. Confira também o 1º nome de cada frase, porque o script não sobe para maiúscula nome que só aparece no início de frase: passe todos por `--nomes`. Ao entregar, liste os nomes próprios da legenda para ele conferir se refizer no CapCut. Ele refez a legenda no CapCut no Ronaldo e no Arrascaeta, e a automática errou "o punho quebrou" → "Pedro quebrou": avise também frases curtas que a transcrição automática costuma trocar por nome.
- **Números por extenso:** o `legenda_karaoke.py` converte sozinho o algarismo que sobrou (0–999) para extenso ("dois a 2" → "dois a dois", "20" → "vinte"). Número acima disso ou com sentido especial (placar "4x2", ano "2026") corrija à mão.
- **Minúsculas**, com nome próprio em maiúscula. Grafia e números **como no roteiro** ("doze", "zero a zero"), não como o Whisper escreveu ("12", "Carrascau").

Abra a `previa_legenda.png` e leia a lista de blocos que o script imprime. Se um nome próprio sair minúsculo, passe `--nomes "Fulano,Ciclano"`.

**SRT para o CapCut (desde 30/set/2026).** O usuário refaz a legenda no CapCut em todo vídeo, e a automática dele erra. No Raphinha saiu publicado "Rafinha" em vez de Raphinha, várias vezes, e em 54,4–55,3s "Rafinha teve uma lesão" no lugar de "a coxa dele tá pedindo socorro". O `legenda_karaoke.py` agora grava `legenda_capcut.srt`, com os mesmos blocos, tempos e grafia da nossa faixa, e o `render_final.py` copia para `<job>/legenda para o CapCut.srt` (raiz do job, fora de `Videos prontos/`). Na entrega, diga para ele **importar esse arquivo no CapCut** (no editor do computador, importar legendas) e aplicar o estilo dele, em vez de gerar a automática. Se ele montar do zero em cima da narração crua, sem o nosso corte, os tempos não batem: nesse caso gere o SRT a partir da `narracao_final.wav` (pausas cortadas), que é a linha do tempo que ele também usa.

## Passo 7 — Render, áudio e marca d'água

**Ordem (regra de 29/set/2026, para a montagem não passar de ~1h):** rascunho → revisão (Passo 8) → corrige → rascunho → revisão só dos shots alterados → … → **as 2 entregas uma vez só, no fim**. No Vini x Austrália a montagem levou ~2h porque cada correção refazia os 4 arquivos (~20 min cada, 3 vezes). O rascunho sai em ~2 min.

    python scripts/render_final.py --render "<job>/_montagem/render" --narracao "<job>/_montagem/narracao_final.wav" --legenda "<job>/_montagem" --saida "<job>" --nome <apelido> --rascunho

gera `_montagem/render/rascunho.mp4`: a mesma composição do com-legenda final (cor + legenda + narração), com encode rápido e fora de `Videos prontos/`. Com a revisão limpa, rode o mesmo comando **sem** `--rascunho` (e com `--sfx sfx.json`, se houver) para gerar as entregas:

    python scripts/render_final.py --render "<job>/_montagem/render" --narracao "<job>/_montagem/narracao_final.wav" --legenda "<job>/_montagem" --saida "<job>" --nome <apelido> [--sfx sfx.json]

- **Cor:** saturação 1,18, contraste 1,12.
- **Sem marca d'água do canal** (21/out/2026): nenhuma das 2 entregas leva lupa ou "Radar Do Campo". Não existe mais `_checagem_marca.png`.
- **Áudio x narração:** o script compara cada entrega com a `narracao_final.wav` segundo a segundo. **FALA SUMIDA** (a narração tem voz e a entrega quase não tem) bloqueia a entrega. **Correlação baixa** é só aviso: o limitador de volume achata os picos da voz e derruba a correlação sem faltar nada (Kane, set/2026: 4 janelas "divergentes" e a transcrição da entrega bateu 100% com a narração). Se aparecer só o aviso, transcreva a entrega com faster-whisper e compare com o roteiro antes de entregar.
- **SFX:** 2–4 no vídeo todo, nos impactos (gancho, revelação, lance-chave). O script monta uma cama única em numpy. Nos dois vídeos refinados no CapCut (Andreas e Bernal, 18/out) ele **ligou** a faixa de efeitos que eu deixava muda, então no rascunho do CapCut ela vem ligada (Passo 9). As 2 entregas saem sem SFX; os efeitos ficam só na faixa do CapCut.
- **Loudness:** o áudio final é normalizado a **-10 LUFS** (medido no Faiq). As montagens automáticas anteriores saíram com -18,9 e -13,4, baixas demais. O nível final e a trilha (~13–14 dB abaixo da voz) ficam por conta do usuário no CapCut: no Palermo/Diogo ele publicou a -7,1 LUFS. Não mude o alvo por conta própria. O que ele exporta do rascunho do CapCut sai mais baixo, porque o CapCut não normaliza: -14,4 no Andreas e -13,3 no Bernal. O Andreas (-11,3) e o Bernal (-10,5) também saíram um pouco abaixo do alvo no nosso render: confira o valor que o `render_final.py` imprime e avise se passar de 1 dB.
- **Exportação:** 1440x2560, 60fps, H.264 ~20 Mbps, AAC 192k. As 2 entregas vão para `<job>/Videos prontos/` e nada mais entra nessa pasta. São 2 encodes de 1440x2560 (preset medium, ~6–8 min no total): rode em background e **só uma vez**, depois da revisão limpa do rascunho. Se o usuário pedir correção depois da entrega, volte ao rascunho, revise só os shots mexidos e gere as 2 de novo no fim. A prévia 720p e a checagem da marca ficam em `_montagem/render/`.

## Passo 8 — Revisão antes de entregar

1. **Revisão obrigatória a cada 0,1s (regra do usuário, set/2026) antes de QUALQUER entrega**, inclusive reentregas depois de correção. Ela é feita no **rascunho** (Passo 7), não nos arquivos finais:

       python scripts/revisao.py "<job>/_montagem/render/rascunho.mp4" "<job>/_montagem/revisao" --edl "<job>/_montagem/edl.json"

   Na primeira passada, o vídeo inteiro. **Depois de uma correção**, gere o rascunho de novo e revise só os shots que você mexeu (com 0,5s de margem para pegar as emendas):

       python scripts/revisao.py "<job>/_montagem/render/rascunho.mp4" "<job>/_montagem/revisao" --edl "<job>/_montagem/edl.json" --shots 18,20

   Mudou a duração de um shot? Os vizinhos mudam de posição: inclua-os em `--shots`. Tirou ou juntou shot (renumeração)? Revise o vídeo inteiro de novo.

   São 10 quadros por segundo (~660 num vídeo de 66s), em folhas de 60 quadros (6s cada), com o tempo e o número do shot em cada miniatura. A borda vermelha marca o primeiro quadro de cada shot. **Abra e percorra todas as folhas**, sem amostrar. Em cada quadro confira cada área da tela:
   - **Centro:** o assunto que a nota prometeu está na tela e dentro do quadro?
   - **Legenda:** diz o que está sendo falado e não cobre o lance (mãos, bola, rosto)?
   - **Topo e cantos:** sobrou marca de terceiro (WAMO, ge, sportv, placar de TV), mancha do clone, letra ou rosto duplicado?
   - **Rodapé:** nenhuma marca do canal (desde 21/out/2026 não vai logo)?
   - **Viradas:** quadro preto, flash de outro lance ou transição queimada da fonte?
   - **Últimos quadros:** emendam no primeiro (loop)?

   Anote cada defeito com tempo e shot, corrija a EDL, rerenderize os shots (`prep_shots.py --shots`, `posfx.py`), gere o rascunho e **revise de novo** os shots mexidos até sair limpo. Só então gere as 2 entregas e entregue. Depois do render final, confira a `_checagem_marca.png` e a checagem de áudio; a revisão quadro a quadro não precisa ser repetida, porque a imagem é a mesma do rascunho.
2. **Bordas de cada shot:** com `--edl`, o `revisao.py` também gera `bordas_XX.jpg`, com cada virada de shot a 30fps (0,2s antes e depois), uma linha por corte. **Percorra todas.** O passo de 0,1s pula quadro solto, e a auditoria do `prep_shots.py` não separa esses casos de ruído (testei um limiar mais sensível nas bordas: o quadro de outro vídeo deu score 0,09, igual ao 2º quadro de qualquer shot). No Endrick, só as bordas mostraram 1 quadro de outro vídeo com o microfone "BTB Sports" no início da zona mista, uma fusão da fonte com imagem fantasma, 1 quadro de outra cena no fim de um shot e um quadro escurecido no começo de outro. A correção padrão é avançar a entrada (ou recuar a saída) 0,15–0,3s. O clarão branco no 1º quadro de shot com `fx: flash` é esperado, não é defeito.
3. **Compare com a referência:** ponha 4–6 quadros da sua montagem ao lado de quadros equivalentes da referência (mesma posição na narração). Legenda na mesma altura e tamanho? Mesma proporção de torcida? Protagonista na tela nas falas genéricas?
4. **Revisão às cegas:** assista como espectador. Deu para entender o lance-chave sem pausar? O final parece final e emenda no começo?

Qualquer defeito: corrija a EDL, rode de novo e revise de novo.

**Checagem de viralização (Passo 3b) no rascunho, antes das 2 entregas:**
- O 1º segundo mostra o pico nº 1 do mapa de impacto?
- Cada ação do vídeo aparece até o pico, inclusive o golpe ou contato? Olhe o último quadro de cada shot de ação na folha `bordas_XX.jpg`.
- Algum shot com zoom ou upscale escondeu a escala que a frase promete ("lotou", "vazio", "85 mil")?
- Alguma imagem contradiz a frase dela, ou cobre com torcida uma frase que nomeia pessoa, preço ou data?

Qualquer "sim" volta à EDL.

## Passo 9 — Rascunho editável no CapCut (desde 18/out/2026)

O usuário quer ajustar sozinho o que fizemos, sem pedir outra rodada. Em 18/out ele pediu: "ao invés de abrir a timeline no Concat, consegue fazer o mesmo só que no CapCut?". O CapCut substitui o Concat (`concat_projeto.py`, que fica só se ele pedir o Concat). **No fim de toda entrega, ofereça em uma linha abrir o rascunho no CapCut**, e gere quando ele aceitar (ou quando ele pedir, como no Bernal: "abre tudo certinho no CapCut como fizemos na última"). Não gere sem perguntar, porque gerar exige fechar o CapCut dele.

    python _montagem/scripts/capcut_projeto.py "<job>" --nome "Radar - <título>" [--modelo "<rascunho-modelo>"] [--sfx-mudo]

Rascunho gerado, rode a parte "Rascunho do CapCut" do "Fechamento obrigatório: Hub" (fim deste arquivo).

O que ele aprovou, depois de recusar a 1ª versão ("não consigo mexer no que você fez como zoom, enquadramento e efeitos, até mesmo a legenda está diferente, e já quero que a música do meu rascunho anterior esteja igual"):
- **Parte do rascunho-modelo dele:** é o mais recente que não começa com "Radar - " nem com "_tmp", hoje o "0417-cópia… (15)". A pasta é copiada inteira, então vêm junto as duas trilhas com a posição dele, o efeito "Dramatic", tudo cortado (as faixas de logo do modelo, lupa e YouTube, ficam de fora desde 21/out/2026) na duração do vídeo. **Volume da trilha principal: 0,12** (rodada 14: o modelo vem com 0,34, e ele baixou para 0,07–0,16 nos cinco vídeos). A segunda trilha vai a 0,09 e até ~1s antes do fim (o modelo parava em ~66s), e o impacto "Dramatic" a 0,3. Com `"revelacao": true` num shot, a virada inteira (fim da 1ª trilha, Dramatic, entrada da 2ª) vai para ele. Sem a marca, fica em 44,6s e o script avisa (rodada 16).
- **Tudo nativo e editável, nada renderizado por cima.** A 1ª versão tinha uma faixa CORTE com o vídeo entregue em cima dos brutos, e ele não conseguia mexer. Agora cada shot é o clipe bruto, com corte e velocidade, escala e posição em Vídeo › Transformar e o movimento em keyframes.
- **Cor da entrega gravada nas cópias dos clipes** (`_montagem/capcut_clipes/`, eq 1,18/1,12). Keyframe de Ajuste (saturação/contraste) aparece no painel, mas não renderiza.
- **Flash:** PNG branco com keyframe de opacidade, na faixa FLASH, mais o soco de escala no shot. **Flashback:** filtro P&B do CapCut (褪色黑白, biblioteca Pro; ele é Pro) numa faixa própria.
- **Cards e fotos:** foto ou PNG da EDL vira clipe de 12s, e os destaques `icone` (cards de comentário) vão nas faixas CARDS/CARDS2, editáveis.
- **Desfoque e setas (desde 27/out/2026):** cada `borrar` da EDL vira, na faixa DESFOQUE, uma cópia do shot (mesmo corte, zoom e pan) com máscara Retângulo e efeito Desfocar (0,6, borda 0,25), como ele faz à mão. A caixa é convertida para a fonte e anda junto com o pan. Setas e círculos (`destaque` seta/circulo) vão como PNG do quadro inteiro na faixa SETAS. Antes nada disso ia para o rascunho, e ele refazia à mão ou fechava o zoom para esconder a marca (CR7, Piqué). Conferido no CapCut em 27/10: o desfoque, a seta e o P&B aparecem na prévia.
- **Legenda:** karaokê com um trecho por palavra, a palavra falada em amarelo #FAFE05 e a mesma fonte da entrega (`assets/Montserrat-ExtraBoldItalic.ttf`, passada como caminho no estilo). Tamanho 10 e centro a 54%. Ele não mexeu na legenda em nenhum dos dois.
- **SFX ligado** (ele ligou a faixa nos dois; `--sfx-mudo` deixa muda). Narração na faixa NARRACAO.
- **Tempo dos keyframes = tempo da fonte.** O CapCut grava o `time_offset` no tempo do clipe (o mesmo do `source_timerange`), não relativo ao início do segmento. A 1ª versão gravava relativo: em clipe com entrada > 0, o pan e o soco ficavam parados, e no Bernal ele teve que refazer o pan do gol do Abde. O script converte (`in + t × velocidade`).

Pegadinhas:
- **Gere com o CapCut FECHADO.** Com ele aberto, o `root_meta_info.json` é reescrito, o rascunho some da lista ou abre a versão velha, e ao fechar o CapCut grava por cima. Se só o nosso rascunho estiver aberto, `taskkill //F //IM CapCut.exe`. Se o projeto dele estiver aberto, **pergunte antes**.
- Para conferir: o computer-use precisa de "CapCut", "capcut.exe" e "File Explorer" (barra de tarefas). A home abre no monitor VX-215X e o editor no 27G2G4. Confira 3–4 pontos na prévia (gancho, um flash, um card, o flashback) e diga que não assistiu o vídeo inteiro no CapCut.
- Ele exporta do CapCut um arquivo só, com o título como nome, em `Videos prontos/`. Para comparar depois ("Aprendizado diário"), compare o `draft_content.json` do "Radar - <título>" com o que o script gera de novo numa raiz temporária dentro do job (`--raiz "<job>/_montagem/cmp/capcut_orig"`, com uma cópia só do `draft_content.json` e do `draft_meta_info.json` do modelo e do `root_meta_info.json`). Isso mostra cada zoom, keyframe, faixa e volume que ele mudou, o que o vídeo sozinho não mostra. Depois rode `analisa_capcut.py "<job>" "Radar - <título>"` (corte a corte, com a frase narrada e a nota do shot, máscaras, efeitos, textos e sobreposições) e `pares_quadros.py` nos tempos que ele apontar (nosso x dele lado a lado). Antes de transformar um zoom dele em regra, veja se o shot tinha `borrar`: até 26/10 o desfoque não ia para o rascunho, e o zoom era só para esconder a marca.

## Bloqueios: não entregue quando

- a revisão a cada 0,1s (`revisao.py`) não foi percorrida no rascunho do corte que vai ser entregue (inteira na 1ª passada; os shots alterados em cada correção), ou achou defeito não corrigido;
- aparece logo do canal em alguma entrega, ou a legenda não está no padrão do Passo 6 (Modo Completo);
- algum corte de conteúdo cai fora de pausa da narração;
- o último plano não emenda no primeiro (loop visual: mesmo clipe, saída do último = entrada do primeiro);
- aparece marca d'água de outro perfil ou emissora (WAMO, ge, sportv, Paramount+…) em qualquer quadro, ou sobrou mancha/reflexo de clonagem;
- a auditoria acusou corte de cena ou fade dentro de algum shot (quadro de outra cena piscando, quadro escuro na virada);
- um plano genérico foi apresentado como prova de lance específico;
- o gancho não é o pico nº 1 do mapa de impacto (Passo 3b), ou falta o `plano_viral.md`;
- uma ação (golpe, chute, cadeira, queda) foi cortada antes do pico;
- uma frase que nomeia pessoa, preço ou data foi coberta com torcida/estádio genérico, ou a imagem contradiz a frase;
- um plano de escala/lugar (lotado, vazio, multidão, placa, cartaz) tem zoom > 1,3 ou upscale > 2,2x;
- algum shot com zoom deixa o assunto sair do quadro, ou o lance fica ilegível (bola/protagonista minúsculos, borrão de upscale);
- aparece ferimento/sangue sem desfoque, ou o desfoque deixa retângulo ou vermelho aparente;
- a duração diverge da `narracao_final.wav` em mais de 0,2s, falta áudio ou há quadro preto nas viradas;
- o vídeo final ficou abaixo de 60s (estique as respirações antes, Passo 1);
- a frase cita um comentário ou um documento e a imagem não é o print real dele (Passo 3, item 22), ou o realce do documento cai embaixo da legenda;
- clipes baixados não foram abertos (o Passo 2 não foi feito em `_extras`/`_rejeitados`);
- falta o `com-legenda` ou o `sem-legenda` em `Videos prontos/`, ou algum dos dois falhou na checagem de áudio x narração.

## Entrega

Os 2 arquivos em `<job>/Videos prontos/`: `<apelido>-com-legenda.mp4` e `<apelido>-sem-legenda.mp4`, sem logo. Na raiz do job, `legenda para o CapCut.srt` e `guia da trilha.txt`: diga em uma linha para ele importar esse arquivo no CapCut em vez da legenda automática. Mostre a prévia (`_montagem/render/<apelido>-preview.mp4`) com `SendUserFile`. Resuma em poucas linhas: planos/min, % de torcida, % de protagonista, as decisões que valem discussão e o que ficou mais fraco e por quê. Não prometa desempenho. Termine oferecendo abrir o rascunho editável no CapCut (Passo 9).

**Hub, na entrega:** siga o "Fechamento obrigatório: Hub" (fim deste arquivo), depois de gravar o prompt de títulos e tags abaixo.

**Prompt de títulos e tags para chat novo (pedido do usuário em 23/out/2026).** Ele roda títulos/capa/tags num chat novo. Em toda entrega, sem perguntar, preencha `assets/prompt_titulos_tags.txt` (troque `{PROTAGONISTAS}`, `{JOGO}`, `{FATO}`, `{DURACAO}`, `{PAUTA}` (o id da pauta do Hub), `{PASTA}` (a pasta do job) e `{ROTEIRO}` pelo roteiro limpo, sem os rótulos Gancho/Contexto/Payoff e com a grafia certa dos nomes), grave em `<job>/prompt titulos e tags.txt` e mostre o prompt inteiro num bloco de código na resposta, pronto para copiar. O prompt é autossuficiente (traz as regras da skill `titulos-e-tags`): funciona em qualquer chat, mesmo sem a skill. Se a skill `titulos-e-tags` mudar, atualize este modelo junto.

**Limpeza automática da entrega (05/10/2026).** No fim do render final, e nunca no `--rascunho`, o `render_final.py` manda para a Lixeira só o que se refaz sozinho: `corte_completo.mp4`, `corte_limpo.mp4` e `rascunho.mp4` (~1,7 GB). Shots, clipes, EDL e prévia ficam, então correção e remontagem continuam iguais. Se ele pedir correção depois da entrega, siga o fluxo de sempre: o `prep_shots`/`posfx` emendam o corte de novo, e o `render_final` refaz o `corte_completo` pela `lista_completo.txt` se ele não existir. Não comente a limpeza na entrega, a não ser que ela falhe.

Se o usuário mandar a montagem que ele fez à mão com o mesmo material, rode `casar_fontes.py` nela para ver de onde saiu cada trecho, compare com a sua e proponha mudanças nesta skill. Com ~100 clipes e compactos longos do YouTube, ele leva ~40 min: rode em background e, enquanto isso, faça as folhas do vídeo dele a cada 0,5s (`folha_contato.py --passo 0.5`), transcreva a narração e o vídeo final (faster-whisper) e meça LUFS e trilha. Match com score abaixo de ~0,7 não é confiável quando há ícone, seta ou zoom por cima: confirme olhando o quadro. Os clipes que ele baixou por conta própria (arquivos com o id do TikTok como nome) mostram o que faltou no garimpo: consulte a origem com `yt-dlp --print "%(uploader)s|%(upload_date)s|%(description)s"` e leve a lição para a skill `garimpo-de-videos`.

**Aprendizado diário (pedido do usuário, out/2026):** quando ele disser algo como "compara minha edição de hoje" (ou a rotina do dia achar um vídeo editado por ele ainda não comparado), compare, mostre o que ele mudou e **atualize esta skill no HUB no mesmo dia**: backup `_bak-AAAA-MM-DD-<vídeo>`, regra nova no lugar certo (Passo 3/5/7, "Erros já cometidos"), nova data na linha de versão, `.skill` reempacotado. Grave `<job>/_montagem/cmp/comparado.txt` quando terminar, para a rotina não oferecer de novo.

Se ele refinou a nossa entrega no editor (mesma duração; costuma ficar em `Videos prontos/` como `<título> TIKTOK.mp4`), compare com a base que ele usou (normalmente o `sem-legenda`; antes de 21/10 era o `completo-sem-legenda`):

    python scripts/compara_edicao.py "<nosso>.mp4" "<dele>.mp4" "<job>/_montagem/cmp"
    python scripts/lado_a_lado.py "<nosso>.mp4" "<dele>.mp4" "<job>/_montagem/lado.jpg" <t0> <t1> 0.3

O primeiro lista os trechos de imagem trocados (por região da tela) e as janelas de áudio diferentes; o segundo mostra os dois lado a lado. Resíduo de áudio constante e baixo em todo o vídeo é a trilha dele; picos isolados são SFX. Traduza cada troca numa regra e proponha a mudança nesta skill.

Se ele refinou **no rascunho do CapCut** que geramos (Passo 9), o `compara_edicao.py` acusa diferença em quase tudo, porque os brutos e o filtro P&B do CapCut não batem pixel a pixel com o nosso render. Nesse caso compare **o projeto**, como explicado no Passo 9: cada zoom, keyframe, faixa ligada ou oculta e volume que ele mudou aparece ali. Use o `lado_a_lado.py` só nos trechos que o projeto apontar.

## Espaço em disco: fechar os vídeos postados

Em 05/10/2026 o disco C: chegou a 22 GB livres. Cada vídeo ocupava ~5 GB: ~2,3 GB de `clipes`, ~3 GB de `_montagem/render` e só ~1 GB de finais. O usuário pediu um **registro final** (o "end-point") de cada vídeo postado. Mas os clipes **não podem sair na entrega**, porque ele pode pedir correção ou remontagem depois. Por isso:

- **Na entrega** saem só os cortes regeneráveis (ver Entrega). O vídeo fica com ~3 GB.
- **Quando ele pedir** ("fecha os vídeos antigos", "limpa os vídeos já postados"), rode o `fechar_videos.py` sobre os vídeos com mais de 15 dias:

      python scripts/fechar_videos.py                 # mostra o que faria, sem mexer em nada
      python scripts/fechar_videos.py --executar      # [--dias 15] [--so "<pasta>"] [--limite-gb 140]

  O script cria `<job>/_registro/` (receita da montagem, inventário, links das fontes, notas, transcrições e `lista_clipes.txt`), manda `clipes`, `_montagem`, `frames` e `transcricoes` para a Lixeira e refaz `Shorts/Registro dos vídeos postados.csv`. Esse CSV é o único arquivo que a skill grava fora de uma pasta de vídeo, com autorização dele. O vídeo fecha com ~1 GB. Para remontar um vídeo fechado, os links estão no `_registro`, mas alguma fonte pode ter saído do ar.
- **Antes de rodar,** peça para ele esvaziar a Lixeira. Ela tem 150 GB; passando disso, o Windows apaga para sempre o que estiver lá dentro. O script para sozinho em `--limite-gb`.
- **Nunca apague de vez:** tudo vai para a Lixeira (`scripts/lixeira.py`), e quem esvazia é ele. Se a "Proteção contra ransomware" do Defender estiver ligada e a pasta for protegida, o arquivo não sai e o script avisa. Não desligue a proteção: avise o usuário.

## Erros já cometidos (não repetir)

- Bruno x Fleetwood (28/out/2026): gancho na arquibancada com o Bruno pequeno; nomes dos comentaristas legíveis nos cards; os 3 cards empilhados no clímax em vez do último sozinho; closes com a janela fixa e o rosto na borda.
- CR7, Toney, Neymar, Piqué e Yamal (24–27/out/2026):
  - Rascunho do CapCut sem os desfoques e as setas da EDL: ele refez à mão ou fechou o zoom para esconder a marca. Corrigido no `capcut_projeto.py`.
  - Caixa do `borrar` acima do "FIFA+" (logo à mostra em 5 shots) e o "g" da ge no canto em 4 shots do Neymar.
  - "O nome da regra que tirou ele de campo" coberto com um reserva de colete, com o Neymar fora do quadro.
  - Closes extremos do rosto do Yamal, sem contexto; falta do Félix cortada pelo zoom; prévia de lesão do Yamal sugerindo um fato que não houve.
  - P&B parando antes do último shot da Copa 2022; 2ª trilha acabando 10–14s antes do fim; nenhuma EDL com `"revelacao": true`.
- Thiago Silva (22/out/2026): o `capcut_projeto.py` travou com "SegmentOverlap" na legenda, porque palavras divididas à mão (anos por extenso) tinham tempos que, arredondados separadamente, se sobrepunham em 1 µs. Corrigido no script.

- Andreas Pereira e Bernal x Yamal (18/out/2026):
  - Parar a montagem e pedir narração nova porque deu 59,2s, quando dava para chegar a 60 com a mesma, esticando as respirações (Passo 1).
  - 1ª versão do rascunho do CapCut com o corte renderizado por cima dos brutos: zoom, enquadramento e efeitos ficaram impossíveis de mexer, a legenda saiu com outra fonte e a música do modelo dele não veio (Passo 9).
  - Keyframes gravados relativos ao segmento: no CapCut o pan e o soco ficaram parados em todo clipe com entrada > 0 (Passo 9).
  - Cartão vermelho fora do quadro em "o motivo da expulsão", bola extra invisível no plano aberto e quadro fechado demais para a bola extra acertar a bola do jogo. Ele corrigiu os três no CapCut (item 23).
  - Card "MDS olha essa expulsão", logo da Band e logo da CazéTV só vistos na revisão (Passo 5, item 0).

- Bruno Duarte (08/out/2026, aprovado sem mudanças). Erros pegos na própria revisão, antes da entrega:
  - Logos de TNT e Prime no quadro; dividida ao vivo enquadrada com o lance fora do centro; "o Colidio lança o David" coberto por outro lance. Só a revisão a cada 0,1s mostrou.
  - Narração sem a frase de abertura do roteiro, avisada só na entrega. Compare a transcrição com o roteiro antes de montar.
  - Abrir 4 ou mais folhas de contato por mensagem: várias voltaram "[media removed: request limit]". Junte num mosaico ou abra de 2 em 2.

- Calcutá / Índia x Brasil (03/out/2026). O usuário não pediu refação, mas apontou:
  - Gancho num plano parado (grupinho de brasileiros no setor vazio), com o take do torcedor batendo a cadeira disponível no material.
  - Torcedor com a 10 da Argentina batendo a cadeira cortado em 22,07s, com o golpe em 22,0–22,2s (e o segundo em 23,7–24,2s).
  - Panorama do Salt Lake lotado (2011) recortado numa fatia com upscale de 5,3x; hino, placa e cartaz com zoom 1,5–1,75. O contexto "lotou" e "estádio" sumiu.
  - "Um torcedor resumiu" coberto com arquibancada vazia, com o torcedor da CNN disponível; "bandeira do Brasil era difícil de achar" mostrando bandeiras do Brasil; "a própria imprensa brasileira" mostrando fotógrafos indianos; "ingresso de 3.500 rúpias" e "dez meses depois" com estádio vazio genérico.

- Modric e Endrick (comparados em 02/out/2026):
  - Gancho na massa (torcida de pé aplaudindo) porque era o clímax; ele quer uma pessoa em ação (o Yamal sentado na bola).
  - Gancho do Endrick na câmera alta da TV com ele já no chão, quando existia filmagem da arquibancada do bolo inteiro (o garimpo não achou; ele baixou).
  - "Depois do título da Copa" coberto com fogos do dia, no lugar dos campeões no túnel da Copa.
  - Gol do Yamal num take de torcida que não mostrava a bola entrar.

- Argentina sem a camisa 10 (01/out/2026):
  - Gancho num objeto parado (camisa pendurada no vestiário) escolhido por ser bonito e fechar o loop; ele trocou por ação com a pista visual (Passo 3, item 9).
  - `--shots 01,41` no PowerShell pulou o shot 01 sem aviso; o rascunho saiu com o gancho velho.
  - `--sem-bordas` no vídeo inteiro por causa de um alarme falso num shot só (use `ignorar_bordas` no shot).

- Raphinha cortado da Seleção (30/set/2026). Ele montou do zero; estes são os pontos em que a skill deixava a desejar:
  - Sem ícone de veredito no gancho: ele pôs o escudo da CBF riscado sobre a cabeça do Raphinha (item 15).
  - Gancho pelo evento mais recente num roteiro sobre um padrão: ele abriu na lesão mais forte, a da Copa (item 9).
  - Sem punch-in na parte do corpo narrada, sem imagem do lugar (Calcutá), sem um corte por item na enumeração, sem o rosto do técnico em "a Seleção tá sugando" (itens 16–19).
  - Legenda publicada com erros da automática do CapCut ("Rafinha"; "Rafinha teve uma lesão" no lugar de "a coxa dele tá pedindo socorro"), porque ele não tinha o texto certo para importar. Agora sai o `.srt`.
  - Narração do AI Studio sem "sábado, em Calcutá" e com "difícil" no lugar de "inédito", sem aviso antes da montagem (Passo 0).

- Endrick x Austrália (29/set/2026):
  - Keys de enquadramento escritas em tempo do vídeo final: a janela ficou parada e o gol da arquibancada saiu com a jogada fora do quadro.
  - Quatro defeitos de borda de shot (quadro de outro vídeo com marca "BTB", fusão, quadro de outra cena, quadro escuro) que a auditoria não pegou e o passo de 0,1s quase deixou passar. Agora há as folhas `bordas_XX.jpg`.
  - Montar com a skill instalada desatualizada (sem a v16): o HUB estava na frente. Confira a versão no começo.

- Vini x Austrália (29/set/2026):
  - Pênalti do Raphinha num ângulo da TNT que começava com o goleiro já caído: o chute não aparecia.
  - Payoff ("bateu rasteiro e fez o quarto") repetindo os quadros do gancho, com a câmera saindo da bola antes do gol.
  - Take de arquibancada, gol do Bruno e Vini derrubado com os jogadores pequenos demais; ele fechou o quadro na ação.
  - Telão com o rosto do Otávio em "segundo amistoso entre os dois": pessoa que o roteiro não cita, em close, numa fala genérica.

- Ronaldo e Arrascaeta (28/set/2026):
  - Picotar o lance-chave (a queda do Arrascaeta) em 4 cortes com círculo, câmera lenta e replay, em vez de repetir o take contínuo do gancho no momento da narração.
  - Cobrir "deu assistência… fez o segundo" com compacto horizontal em que os jogadores ficam pequenos e parados. Sem lance com qualidade, o close da comemoração dele.
  - Cobrir "sem entrar em campo" (Euro 2008) com plano aberto do árbitro, em vez do rosto do Ronaldo chorando; banco com o técnico na frente.
  - Deixar passar assinaturas pequenas (@brayanncrf, SportyNet, FUTSTATUS) e uma marca da CONMEBOL até a revisão final.
  - Usar foto de agência (Infobae) e print de post em falas que tinham vídeo do protagonista disponível no próprio garimpo; a revisão pediu vídeo com contexto.

- Kane e Atlético-GO (27/set/2026):
  - Abrir o Atlético-GO no goleiro comemorando no apito, com o grito para o camarote só depois. O auge (o grito) tem que ser o quadro 1.
  - Cobrir retrospecto e título ("quatro clássicos… campeão goiano") com torcida da Serrinha. Fato pede placar, taça e o rival campeão, mesmo que seja de outra data e exija voltar ao garimpo.
  - Deixar passar, até a revisão: pedaço do logo ITV, "diariodegoias.com.br" no rodapé, assinatura "@perfil" na borda de baixo, card do post da ESPN no shot de loop e uma fusão de cena da fonte. Meça cada fonte com `grade.py` antes da EDL (rodapé e 0–5s incluídos) e olhe o fim de cada trecho de compacto.
  - Círculo de destaque posicionado ao lado da bola no 1º render da prévia do Kane. Confira `destaque` no shot renderizado.
  - Rodar o `narracao.py` com o limiar antigo (-35 dB): só 2 pausas, e a auditoria recusaria quase todo corte. O padrão agora é -30 dB/0,12s.

- Fechar o vídeo num close de outro clipe porque o roteiro não tinha frase-ponte (Rayan x Austrália). A imagem tem que fazer loop sempre.

- Palermo/Diogo (set/2026). Na 1ª versão, zoom de até 9x em fotos de repost, que tirou o contexto do lance. Na 2ª, faixa 16:9 com fundo desfocado ("não gostei do desfoque"). O certo é tela cheia com zoom moderado seguindo a bola (`keys`/`segue`).
- Gancho com a mão ferida desfocada no lugar do lance (o Diogo subindo no alambrado). "Ele se machucou comemorando" coberto com a ambulância em vez da comemoração. Gol do Palermo num plano aberto fixo com a bola minúscula e um jogador adversário no centro. Muro caindo numa faixa pequena com zoom de 3,7x (borrão). Corte para o rosto no chão enquanto a narração ainda descrevia o muro sobre a perna (o usuário segurou o plano e pôs seta vermelha).
- Foto de outra pessoa (Wikimedia "Paulo Diogo") usada como o protagonista. Confira identidade contra os quadros do lance.

- Entregar com a marca de outros perfis e emissoras (WAMO, ge, sportv, Paramount+) aparecendo junto com a do canal (Rayan x Austrália). Use enquadramento, nunca `delogo`, que deixa borrão.

- Tampar marcas clonando textura sobre torcida, rosto, camisa e placa (Matheuzinho): ficou "reflexo muito aparente" no vídeo todo, com remendo bege, rostos duplicados e logo duplicado. Enquadre ou troque o trecho.
- Shot atravessando o corte interno da fonte e shots entrando no fade para preto de compilado (Matheuzinho): 1 quadro de outra cena piscando no começo do vídeo. Isso não pode acontecer; a auditoria agora barra.
- Shots com SAR diferente (1756:1755 nos sem máscara), que reiniciavam os filtros no meio do vídeo. O `prep_shots.py` agora força `setsar=1` e as tags de cor bt709.
- Usar o post/print da GE TV com texto no lugar do vídeo do lance, zoom 2x em entrevista cortando o rosto e elenco genérico em "primeira convocação" (Matheuzinho).

- Montar sem abrir os clipes de `_extras`: o melhor material do vídeo ficou de fora.
- Descartar clipe inteiro por ter react, legenda ou círculo; o certo é descartar só o trecho.
- Picar takes contínuos de torcida em vários ângulos de transmissão (41 planos/min contra os ~23 do usuário).
- Cobrir falas genéricas com torcida e estádio em vez do protagonista; abrir no estádio em vez de no jogador.
- Lance-chave em câmera lenta 0,5x esticado por 9s, sem o plano aberto que mostra o jogador voltando.
- Narração com as pausas longas intactas (hoje elas são cortadas; acelerar a 1,2x foi a regra antiga, trocada pelo usuário em set/2026). Legenda com palavra-chave fixa, grande, em 2 linhas e a 74% da altura.
- Marca d'água colada com `paste(logo, pos, logo)`: o alpha aplicou duas vezes e a logo sumiu (opacidade efetiva ~0,03). E a checagem numérica da entrega não pegou; olhe o recorte.
- Encadear 81 `overlay` no ffmpeg para a legenda: metade sumiu em silêncio. Use uma faixa única.
- `adelay`+`amix` para SFX com offset grande: os efeitos depois do primeiro não entraram. Use a cama em numpy.
- `setpts=N/FRAME_RATE/TB` no concat derrubou 1/3 dos quadros. Concatene com `-c copy`.
- Remotion com 1440x2560: o compositor falha no seek. Use o pipeline ffmpeg + PIL.
- Áudio final em -18,9 LUFS, baixo demais. Depois, -13,4; o usuário publica em -10.
- "Sem legenda" com a lupa gravada: o usuário editou a partir dele, e a lupa do TikTok vazou para a versão do YouTube (Faiq Bolkiah).
- Evitar a imagem literal (o time campeão com a taça) por medo de Content ID e cobrir "time principal" com estádio vazio.

## Fechamento obrigatório: Hub (fim da entrega e do rascunho do CapCut)

**Na entrega (sempre),** depois de gravar `<job>/prompt titulos e tags.txt` e antes de encerrar a resposta:

    python "C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\radardocampohub1.0\scripts\hub.py" --fonte montagem-de-video atualizar <id> --etapa montagem --pasta "<job>" --arquivo "Com legenda=<job>\Videos prontos\<apelido>-com-legenda.mp4" --arquivo "Sem legenda=<job>\Videos prontos\<apelido>-sem-legenda.mp4" --arquivo "Legenda para o CapCut=<job>\legenda para o CapCut.srt" --proximo-prompt-arquivo "<job>\prompt titulos e tags.txt" --nota "montagem entregue: <duração>s"

**Rascunho do CapCut (Passo 9),** logo depois de gerar:

    python "C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\radardocampohub1.0\scripts\hub.py" --fonte montagem-de-video atualizar <id> --arquivo "Rascunho no CapCut=Radar - <título>" --proximo-prompt-arquivo "<job>\prompt titulos e tags.txt" --nota "rascunho no CapCut; ele refina e exporta"

**A montagem nunca marca Pronto (31/out/2026, Kaio Jorge).** A pauta fica em Montagem do começo da montagem até a `titulos-e-tags` terminar: o vídeo que vai ao ar é o que ele exporta do CapCut, e o título, a capa e as tags são o último passo antes de postar. Antes a entrega marcava Pronto e o rascunho do CapCut voltava para Montagem, e ele viu a pauta ir e voltar. Quem passa para Pronto é só a skill `titulos-e-tags`, no fim dela. O rascunho do CapCut não mexe na etapa, só anexa.

**Correção depois da entrega:** rode de novo a linha da entrega (arquivo de mesmo caminho é trocado, não duplicado).

Feche a resposta com uma linha: `Hub: <título> em Montagem (Pronto vem com títulos e tags), arquivos e prompt de títulos e tags salvos.` Se o `hub.py` falhar, diga o erro nessa linha e siga (seção "Hub").
