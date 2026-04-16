import os

def visualizar_conteudo():
    PASTA_DIARIO = "diary_pages" 

    # Receber do usuario qual arquivo ele quer visualizar
    arquivos_existentes = os.listdir(PASTA_DIARIO)
    print("\nQual o arquivo você deseja visualizar?")
    for arquivo in arquivos_existentes:
        print(f"- {arquivo}")
    arquivo_escolhido = input("ARQUIVO ESCOLHIDO: ")

    # Validar se o arquivo existe
    if arquivo_escolhido not in arquivos_existentes:
        print(f"O arquivo '{arquivo_escolhido}' não existe")
    else:
        caminho_arquivo = os.path.join(PASTA_DIARIO, arquivo_escolhido)

        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            print(arquivo.read())
        