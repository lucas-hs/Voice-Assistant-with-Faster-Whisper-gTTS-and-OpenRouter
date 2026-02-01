# 🎙️ Assistente de Voz com Faster-Whisper, OpenRouter e gTTS

Este projeto implementa uma assistente de voz simples com a utilização da linguagem **Python**. Sendo assim, ele é capaz de:

- Gravar voz de áudio (Linux)
- Transcrever o áudio com o auxílio do Faster-Whisper
- Enviar a transcrição para um LLM via OpenRouter
- Sintetizar a resposta em áudio com gTTS

O fluxo do projeto funciona de modo local, com exceção da chamada da API vinda do OpenRouter. 

---

## 🗒️ Funcionalidades

- Gravação de áudio com ajuda da biblioteca **sounddevice** 
- Transcrição realizada de modo offline com Whisper
- Incrementação de modelos LLM providenciados pelo OpenRouter
- Compatibilidade com Linux 

---

## 🤖 Tecnologias Usadas

- Python 3.9+
- sounddevice - Captura de áudio
- scipy - Tratamento do arquivo .wav 
- faster-whisper - Transcrição do áudio. Menor cosumo de CPU, maior eficiência.
- OpenRouter LLMs - Provedor de modelos LLM
- gTTS - Text to Speech
- dotenv - Gerenciamento das variáveis do ambiente

---

## 📋 Fluxo de Execução

1. O programa grava 5 segundos de áudio

2. O áudio é salvo como record01.wav

3. O Whisper realiza a transcrição

4. O texto é enviado para o modelo:

    <code>google/gemma-3n-e2b-it:free</code>

5. A resposta do modelo é convertida em voz

6. O áudio final é salvo como response_audio.wav

