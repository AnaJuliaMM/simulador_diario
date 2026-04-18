from datetime import datetime
import os

def criar_pagina():
    # Declarar constantes
    DTH_NOW = datetime.now().strftime("%d%m%Y_%H%M%S")
    DIARY_FOLDER = "diary_pages"
    FILE_NAME = f"diary_{DTH_NOW}.txt"
    FILE_PATH = os.path.join(DIARY_FOLDER, FILE_NAME)

    # Garantir a existência da pasta destino
    if not os.path.exists(DIARY_FOLDER):
        os.makedirs(DIARY_FOLDER)
        print(f"<Pasta '{DIARY_FOLDER}' criada>")

    # Criar e preencher o arquivo
    content = input("O que você gostaria de registrar hoje? ")

    with open(FILE_PATH, "a", encoding="utf-8") as file:
        file.write(datetime.now().strftime("%d/%m/%Y"))
        file.write(f"\n{content}\n")

    print("Seus pensamentos foram registrados!")