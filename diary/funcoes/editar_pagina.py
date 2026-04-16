import os

def editar_pagina():
    PASTA_DIARIO = "diary_pages" 

    # Receber do usuario qual arquivo ele quer editar
    arquivos_existentes = os.listdir(PASTA_DIARIO)
    print("\nQual o arquivo que deseja editar?")
    for arquivo in arquivos_existentes:
        print(f"- {arquivo}")
    arquivo_escolhido = input("ARQUIVO ESCOLHIDO: ")

    # Validar se o arquivo existe
    if arquivo_escolhido not in arquivos_existentes:
        print(f"O arquivo '{arquivo_escolhido}' não existe")
    else:
        caminho_arquivo = os.path.join(PASTA_DIARIO, arquivo_escolhido)
        novo_conteudo = input("\nDigite um novo conteúdo: ")

        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"{novo_conteudo}\n")
        
        print(f"O arquivo '{arquivo_escolhido}' foi atualizado")

    
    

