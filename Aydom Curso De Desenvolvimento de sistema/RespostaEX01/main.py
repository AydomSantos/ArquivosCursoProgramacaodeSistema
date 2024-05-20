

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

       
    

