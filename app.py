"""
Projeto: Transcrição de Áudio com Whisper e Extração de Pontos-Chave com Ollama

Autor: Arquimedes Mariano

Descrição:
Recebe um arquivo de áudio localizado na pasta audios/,
realiza a transcrição utilizando Whisper e gera um resumo
com pontos-chave utilizando Ollama.
"""

from pathlib import Path

import requests
import whisper


# Configurações do Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"


def transcrever_audio(caminho_audio, modelo_whisper="base"):
    """
    Realiza a transcrição de um arquivo de áudio.

    Parâmetros:
        caminho_audio (str): caminho do arquivo de áudio.
        modelo_whisper (str): modelo Whisper utilizado.

    Retorna:
        str: texto transcrito.
    """

    arquivo = Path(caminho_audio)

    if not arquivo.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {caminho_audio}"
        )

    print("Carregando modelo Whisper...")
    modelo = whisper.load_model(modelo_whisper)

    print("Transcrevendo áudio...")
    resultado = modelo.transcribe(
        str(arquivo),
        language="pt"
    )

    return resultado["text"]


def gerar_pontos_chave(texto):
    """
    Envia a transcrição para o Ollama
    e retorna um resumo com pontos-chave.
    """

    prompt = f"""
Você é um assistente acadêmico.

Analise a transcrição abaixo e gere:

1. Um resumo curto.
2. Os principais pontos-chave em tópicos.
3. Uma conclusão final.

Transcrição:

{texto}
"""

    print("Gerando resumo com Ollama...")

    resposta = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    resposta.raise_for_status()

    dados = resposta.json()

    return dados["response"]


def salvar_resultados(transcricao, resumo):
    """
    Salva a transcrição e o resumo em arquivos .txt.
    """

    pasta_saida = Path("resultados")
    pasta_saida.mkdir(exist_ok=True)

    with open(
        pasta_saida / "transcricao.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:
        arquivo.write(transcricao)

    with open(
        pasta_saida / "pontos_chave.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:
        arquivo.write(resumo)

    print("Arquivos salvos na pasta resultados/")


def main():
    """
    Função principal do programa.
    """

    # Arquivo fixo utilizado no projeto
    caminho_audio = "audios/exemplo.mp3"

    try:

        # Etapa 1 - Transcrição
        transcricao = transcrever_audio(
            caminho_audio,
            modelo_whisper="base"
        )

        print("\n===== TRANSCRIÇÃO =====\n")
        print(transcricao)

        # Etapa 2 - Resumo
        resumo = gerar_pontos_chave(transcricao)

        print("\n===== PONTOS-CHAVE =====\n")
        print(resumo)

        # Etapa 3 - Salvar arquivos
        salvar_resultados(transcricao, resumo)

    except Exception as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()