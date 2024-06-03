

# questão 6 - Facil

"""

def fatoralValor(valor):
    result = 1
    for i in range(2 , valor + 1):
        result *= i


numValor = int(input("Digite um numero Inteiro: "))
print(f"o Fatorial de {numValor} : {fatoralValor(numValor)}")

"""

# = = = = = = = = = = = = = = = = = = = = = = = = =

# questão 7

"""
import re

def validaSenha(valor):
    if (len(valor) >= 8 and 
       re.search(r"[A-Z]", valor) and 
       re.search(r"[a-z]", valor) and
       re.search(r"[\d]", valor) and
       re.search(r"[!@#$%¨&*()_+{}[]]")):
       return True
    else:
        return False

     

"""

# questão 5

def listaCompras():
    compras = []
    while True:
        print("\n Menu da Lista de Compras")
        print("1. Adcionar item")
        print("2. Remove item")
        print("3. Visualizar item")
        print("4. Sair")
        escolha = input("Insira a opção escolhida: ")
        if escolha == "1":
            item = input("Digite o item que deva ser adicionado: ")
            compras.append(item)
        elif escolha == "2":
            item = input("Digite o item que voçê deseja remover: ")
            if(item in compras):
                compras.remove(item)
            else:
                print("Item não encontrado ! ")
        elif escolha == "3":
            print("lista de Compras Atual")
            for item in compras:
                print(item)
        elif escolha == "4":
            break
        else:
            print("Opção invalida")

listaCompras()