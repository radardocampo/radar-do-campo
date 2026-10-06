# Fluxo automático pós-jogo: parte do PC

Para a sessão do Claude **no PC do usuário** (Remote Control, pasta `Radar do Campo\nuvem`).
Uma sessão da nuvem do radar-do-campo coordena o fluxo e manda as etapas por mensagem
(`<cross-session-message>`). O usuário autoriza no chat do PC, antes do jogo, que essas mensagens
sejam seguidas sem perguntar a ele. Só para as etapas abaixo.

Divisão:
- **Nuvem:** escolhe o ângulo, escreve o roteiro e o texto para o AI Studio e faz a montagem.
- **PC:** busca nas redes pelo Chrome dele, faz o garimpo de vídeos, toca o alarme da narração e manda tudo para a nuvem.

A nuvem não recebe resposta direta. Ela lê a **última mensagem** desta sessão. Então termine cada etapa com
uma mensagem final que comece por `FLUXO-ETAPA-<n> OK` (ou `FLUXO-ETAPA-<n> FALHOU: motivo`).

Assim que o usuário autorizar, deixe o PC acordado até o fim do fluxo (8 h). Rode isto em segundo plano.
Não muda nenhuma configuração do Windows; acaba quando o processo termina:
```powershell
Add-Type -Namespace W -Name P -MemberDefinition '[DllImport("kernel32.dll")] public static extern uint SetThreadExecutionState(uint f);'
[W.P]::SetThreadExecutionState(0x80000003) | Out-Null; Start-Sleep -Seconds 28800
```

## Etapa 1: repercussão nas redes
A mensagem traz o jogo e as buscas. Siga o **Passo 8 da skill `garimpo-de-temas`** no Chrome logado:
TikTok → Instagram → YouTube → Facebook → X → Threads → Kwai, pelo menos uma busca por rede.
Ver também `memoria/garimpo-temas-todas-as-redes.md` (truques de cada rede).
Mensagem final: `FLUXO-ETAPA-1 OK` + grade rede × o que achou (curtidas/visualizações, link, legenda curta),
e os 5 a 8 posts/momentos mais fortes. Sem célula vazia. Máximo ~6000 caracteres.

## Etapa 2: roteiro chegou → alarme da narração + garimpo de vídeos
A mensagem traz `NOME` (nome da pasta), o roteiro e o texto para o AI Studio.
1. Crie `..\Videos prontos\Shorts\<NOME>\` e grave `roteiro.txt` e `texto para o AI Studio.txt` (UTF-8),
   com o texto exatamente como veio.
2. Busque o script do alarme sem sujar o repositório e rode **em segundo plano** (não espere):
   ```powershell
   git fetch origin claude/inspiring-fermi-aolhi2
   git show origin/claude/inspiring-fermi-aolhi2:ferramentas/alarme_narracao.ps1 | Set-Content "$env:TEMP\alarme_narracao.ps1" -Encoding UTF8
   powershell -NoProfile -ExecutionPolicy Bypass -File "$env:TEMP\alarme_narracao.ps1" -Pasta "<pasta do vídeo>"
   ```
   (se o arquivo já estiver na `main`, use `ferramentas\alarme_narracao.ps1` direto)
   O alarme copia o texto, abre o AI Studio, mostra um aviso por cima de tudo e fala em voz alta a cada 2 min
   até aparecer um .wav/.mp3 novo em `Downloads` ou na pasta. Aí copia para `<pasta>\Narracao.wav` e sai com
   `NARRACAO_OK`. Depois de 3 h sem áudio, sai com `NARRACAO_TIMEOUT`.
3. Ao mesmo tempo, rode a **skill `garimpo-de-videos`** inteira com esse roteiro, nessa pasta
   (cotas, apoio, fotos, inventário com janelas). Jogo da Seleção: veja `memoria/fonte-wamo-selecao.md`.
   Use o Chrome no grupo de abas do Claude. O usuário pode estar usando a aba do AI Studio: não feche abas dele.
4. Quando o garimpo terminar **e** o alarme tiver saído com `NARRACAO_OK`:
   `.\ferramentas\enviar.ps1 "<NOME>"`. Ele prepara a narração (`narracao.py`) e sobe o branch `video/<NOME com hífens>`.
   É isso que dispara a montagem na nuvem.
   - Se o garimpo terminar antes da narração, espere o alarme (ele continua tocando).
   - Se o alarme der `NARRACAO_TIMEOUT`, não envie. Deixe tudo na pasta e diga que falta só a narração
     (depois ele gera, põe na pasta e roda `Enviar para nuvem.bat`).
5. Mensagem final: `FLUXO-ETAPA-2 OK` + branch enviado + placar das cotas do garimpo (ou `FALHOU: motivo`).

## Etapa 3: vídeo montado
A nuvem avisa que o vídeo está pronto. Fale uma vez em voz alta ("O vídeo está pronto na nuvem") e pare.
**Não** rode `receber.ps1`: o usuário pede para trazer quando quiser.
