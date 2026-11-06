# Histórico do garimpo de vídeos (consulta)

## Linha de versão até 31/10/2026

**Atualizada em 2026-10-31 (tarde):** selo de andamento no Hub: `status <id> trabalhando` na abertura e `--status aguardando` com o texto do próximo passo no fechamento (seção "Hub"). **Antes, 2026-10-31:** todo garimpo termina com o "Fechamento obrigatório: Hub" (fim do arquivo): clipes ligados, pasta e o prompt de montagem na pauta. **Antes, 2026-10-30:** a pauta do Hub acompanha o garimpo (seção "Hub", Passos 1, 8 e 9). **Antes, 2026-10-18:** prints do que o roteiro cita (comentário, súmula, story), começar pelos links da pesquisa, nada de clipe de canal concorrente, arquivos de trabalho fora da raiz.

## Erros já cometidos (até 31/10/2026)

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

