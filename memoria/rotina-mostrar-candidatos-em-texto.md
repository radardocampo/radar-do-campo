---
name: rotina-mostrar-candidatos-em-texto
description: "rotina do dia - escrever a lista completa de candidatos no texto da resposta, nunca só na caixa de resumo; e não fechar sem as 7 redes pelo Chrome"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 9ea89624-719f-49b0-9bae-3f94d60de664
  modified: 2026-10-18T15:15:17.337Z
---

Em 2026-10-18 o usuário reclamou ("segundo dia") que a rotina terminou sem passar nas redes pelo navegador dele e sem mostrar os candidatos, só números. Eu tinha fechado só com a caixa do wrap_up (sem texto), então a lista nunca apareceu; e o Claude in Chrome estava desconectado e eu entreguei assim mesmo.

**Why:** ele escolhe os roteiros pela lista; sem ela e sem as redes a rotina não serve.

**How to apply:** na rotina, escrever no texto da resposta, antes do wrap_up, cada candidato (o que aconteceu, detalhe obscuro, tipo, repercussão, fontes) + a grade candidato × rede. Se o Chrome não conectar, tentar de novo e avisar que a etapa está pendente, pedindo que ele reconecte, em vez de entregar como se estivesse pronta. Busca do TikTok no navegador embutido exige login: não serve de substituto. Relacionado: [[garimpo-temas-todas-as-redes]].
