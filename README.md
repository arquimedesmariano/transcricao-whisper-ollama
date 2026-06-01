# Transcrição de Áudio com Whisper e Pontos-Chave com Ollama

## Descrição

Este projeto implementa um pipeline em Python que recebe um arquivo de áudio, realiza a transcrição usando o modelo Whisper e envia o texto transcrito para o Ollama, que gera um resumo com os principais pontos-chave.

## Tecnologias utilizadas

- Python
- Whisper
- Ollama
- FFmpeg
- Requests

## Funcionalidades

- Recebe arquivos de áudio nos formatos `.mp3` ou `.wav`.
- Transcreve o áudio usando Whisper.
- Envia a transcrição para o Ollama.
- Gera resumo e pontos-chave.
- Salva os resultados em arquivos `.txt`.

## Instalação

Clone o repositório:

```bash
git clone LINK_DO_REPOSITORIO
cd transcricao-whisper-ollama