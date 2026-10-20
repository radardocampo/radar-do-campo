---
name: agente-voz-pc
description: Agente de voz+tela do PC em BUSINESS\agente-voz (Whisper local + comandos prontos + Gemini de reserva); limites e decisões
metadata:
  node_type: memory
  type: project
  originSessionId: 76028705-24b8-4e99-95b4-52722cb03549
  modified: 2026-10-20T03:20:11.054Z
---

Projeto criado em 2026-10-19/20 em `C:\Users\bruno\Desktop\all\BUSINESS\agente-voz` (venv próprio, `iniciar.bat`, F8 fala, Esc aborta, F9 confirma ação destrutiva). Chave em `GEMINI_API_KEY` (variável de ambiente dele, nunca salvar).

- Gemini grátis = **20 requisições/dia por modelo** (429 com "limit: 20"); por isso a maior parte roda local: Whisper `small` (~2 s) + `comandos.py` (regras, yt-dlp para "vídeo mais viral do canal"). Só o que não tem regra vai ao Gemini (`gemini-3.5-flash`, thinking 0; reservas 3.1-flash-lite e 3.8-flash). `gemini-flash-latest` (3.8) vivia dando 503/504; `gemini-2.5-flash` foi descontinuado.
- Nomes que o Whisper erra: colocar em `nomes.txt` (vira dica de vocabulário).
- Mic certo: "USB PnP Sound Device"; só o monitor principal (DISPLAY2).
- Próximos passos combinados: planejamento em lote + macros aprendidas, provedor reserva (Groq/OpenRouter, a verificar), app de bandeja com contador de cota.

**Why:** ele quer controlar o PC todo por voz, de graça e rápido.
**How to apply:** ao mexer no agente, preferir resolver por regra local antes de gastar chamada de IA.
