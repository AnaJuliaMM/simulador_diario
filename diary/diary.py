from datetime import datetime
import os

from funcoes.criar_pagina import criar_pagina
from funcoes.editar_pagina import editar_pagina
from funcoes.visualizar_conteudo import visualizar_conteudo
from funcoes.deletar_pagina import deletar_pagina

print("Bem-vindo ao seu diário!🙏")
print(f"O que você gostaria de fazer hoje ({datetime.now().strftime("%d/%m/%Y")})?")
print("1 - Criar um registro")
print("2 - Visualizar um arquivo")
print("3 - Editar um arquivo")
print("4 - Deletar um arquivo")
opcao = input("Digite sua opção: ")

match(opcao):
    case "1":
        criar_pagina()
    case "2":
        visualizar_conteudo()
    case "3":
        editar_pagina()
    case "4":
        deletar_pagina()

    case _:
        print("OPÇÃO INVÁLIDA")
