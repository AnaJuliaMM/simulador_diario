from datetime import datetime
import os

from funcoes.write_page import write_page
from funcoes.editar_pagina import editar_pagina
from funcoes.visualizar_conteudo import visualizar_conteudo

print("Bem-vindo ao seu diário!🙏")
print(f"O que você gostaria de fazer hoje ({datetime.now().strftime("%d/%m/%Y")})?")
print("1 - Criar um registro")
print("2 - Visualizar um arquivo")
print("3 - Editar um arquivo")
print("4 - Deletar um arquivo")
opcao = input("Digite sua opção: ")

match(opcao):
    case "1":
        write_page()
    case "2":
        visualizar_conteudo()
    case "3":
        editar_pagina()
    case "4":
        pass

    case _:
        print("OPÇÃO INVÁLIDA")
