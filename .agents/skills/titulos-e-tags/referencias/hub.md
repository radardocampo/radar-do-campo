# Hub do Radar do Campo: referência dos comandos (igual nas 4 skills)

Cada vídeo é uma **pauta** no Hub (radardocampo.online → Vídeos → Pautas). A esteira anda: pauta → roteiro → garimpo → montagem → pronto → no ar. As skills avisam o Hub pelo `hub.py`, no PC:

    python "C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\radardocampohub1.0\scripts\hub.py" --fonte <skill> <comando>

## Comandos (saída em JSON)
- `buscar [termo]` · `ler <id>`
- `criar "<título>" [--etapa E] [--notas-arquivo F] [--roteiro-arquivo F] [--refs-json F] [--proximo-prompt-arquivo F] [--status S] [--status-texto "..."]`
- `etapa <id> <etapa> [--status S] [--status-texto "..."] [--nota "..."]`
- `atualizar <id> [--roteiro-arquivo F] [--notas-arquivo F] [--pasta P] [--arquivo "rótulo=caminho"] [--titulo T] [--proximo-prompt-arquivo F] [--etapa E] [--status S] [--status-texto "..."] [--nota "..."]`
- `status <id> trabalhando|aguardando [--texto "..."]`: só o selo de andamento
- `prompt <id> <arquivo> [--etapa E]`: só o prompt do próximo passo
- `clipe <id> <url> [--tipo clipe|referencia] [--trecho gancho|lance|torcida|reacao|contexto] [--inicio 0:12] [--fim 0:25] [--nota "..."]` · `clipes <id> <lista.json>`

## Regras
- **Id da pauta:** a linha `PAUTA DO HUB: <id>` do pedido (o botão "Copiar prompt" do Hub e os prompts de chat novo trazem). Sem ela, `buscar "<jogador ou time>"`; se nada bater, `criar`.
- **Passe o id adiante:** todo prompt de chat novo leva `PAUTA DO HUB: <id>` logo depois do pedido.
- **Prompt do próximo passo:** grave na pauta com `--proximo-prompt-arquivo` (ou `prompt <id> <arquivo>`); o Hub mostra com botão de copiar.
- **Selo de andamento**, separado da etapa: `trabalhando` (bolinha pulsando) enquanto a skill executa e `aguardando` quando a parte dela termina. Sem texto, o Hub usa o padrão da etapa: roteiro "Escrevendo roteiro" / "Esperando garimpo"; garimpo "Garimpando" / "Esperando montagem"; montagem "Sendo montado pelo Claude" / "Esperando refinamento no CapCut"; pronto "Pronto para postar". Mudar a etapa sem `--status` já deixa em `aguardando`. Mais de 3 h em `trabalhando` sem atualização vira "sem notícias há Xh".
- **Quem marca Pronto é só a `titulos-e-tags`.** A montagem deixa a pauta em Montagem.
- **O Hub nunca trava o vídeo.** Se o `hub.py` falhar (sem internet, senha ausente, pauta excluída), diga o erro em uma linha e siga. Nunca peça para ele consertar o Hub no meio da rotina. Sem terminal no PC (chat sem acesso), diga em uma linha que o Hub não foi avisado.
- Arquivo temporário para o `hub.py` segue a regra de pastas da skill.
- As migrations do Hub se aplicam com `supabase db query --linked -f`, nunca `db push`.
