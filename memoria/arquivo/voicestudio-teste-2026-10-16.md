---
name: voicestudio-teste-2026-10-16
description: "Teste do VoiceStudio (TTS local) em 2026-10-16: instalado, erro de clonagem resolvido, mas na CPU é lento demais"
metadata:
  node_type: memory
  type: project
  originSessionId: b49d93cd-2b4b-414d-bae9-b9efb461bb7b
  modified: 2026-10-16T14:49:10.668Z
---

VoiceStudio v0.5.6 (Electron, github.com/debpalash/VoiceStudio) instalado em 2026-10-16 com pacote Equilibrado (4,8 GB). PC do usuário: GPU AMD integrada (sem CUDA), 16 GB RAM, então roda só na CPU.

**Erro de clonagem "Automatic reference transcription needs an installed speech-to-text model":** a causa é referência >20 s. Nesse caso o app ignora a transcrição do perfil e tenta transcrever com um Whisper próprio que não está instalado. Solução: perfil com referência ≤20 s (cortei 14 s do `voices/a950adf3.wav` em `%APPDATA%\OmniVoice\voices`) e transcrição exata. A aba Transcrever do app funciona e serve para obter o texto.

**Desempenho:** um trecho de ~12 s de fala estourou o limite de 600 s de computação e o app abandonou o job (backend python com 5,4 GB). Para um vídeo de 60 s é inviável. O próprio app sugere motores leves para CPU (OmniVoice GGUF, Supertonic-3), ainda não testados.

**Why:** decide se vale trocar o AI Studio pelo VoiceStudio na narração. [[narracao-feita-no-ai-studio]]
**How to apply:** só retomar se o usuário tiver GPU NVIDIA ou aceitar esperar; não recomendar como substituto do AI Studio no fluxo atual. Antes de comparar qualidade, medir o tempo.
