# verificador de idade
"""
qtdPessoas = int(input("Digite a quantidade de Pessoas: "))
idades = []

for i in range(qtdPessoas):
    nomePessoa = input("Digite o Nome: ")
    idadePessoa = int(input("Digite a idade: "))
    idades.append(idadePessoa)

    if idadePessoa < 13:
        print(f"{nomePessoa} idade {idadePessoa} - Criança")
    elif idadePessoa == 13 or idadePessoa < 18:
        print(f"{nomePessoa} idade {idadePessoa} - Adolecente ")
    elif idadePessoa < 18 or idadePessoa < 60:
        print(f"{nomePessoa} idade {idadePessoa} - Adulto")
    elif idadePessoa > 60:
        print(f"{nomePessoa} idade {idadePessoa} - Idoso")

"""

"""
import math

def calcFatorial(valor):
    return math.factorial(valor)

inseriValor = int(input("Digite um valor: "))
print(calcFatorial(inseriValor))

"""
contato = {}
agenda = []

def buscaApelido():
    apelido = input("Digite o apelido a procurar: ")
    for ele in agenda:
        if ele["apelido"] == apelido:
            print(f"nome completo = {ele['Nome']}")
            print(f"Telefone fixo = {ele['Telefone Fixo']}")
            print(f"Telefone celular = {ele['celular']}")
            return ele 

while True:
    opcao = int(input("Digite 0 para inserir um novo contato: "))
    opcao = int(input("digite 3 para encerrar o programa: "))
    match opcao:
        case 0:
            contato = {}
            apelido = str(input("Digite o apelido: "))
            contato["Apelido"] = apelido
            nomeCompleto = str(input("Digite o nome completo: "))
            contato["Nome"] = nomeCompleto
            telFixo = int(input(" Digite o telefone fixo: "))
            contato["Telefone Fixo"] = telFixo
            celular = input("Digite o telefone celular: ")
            contato["celular"] = celular
            agenda.append(contato)
        case 2:
            pass
        case 3:
            break
    
while True:
     opcao = int(input("Digite 1 para Pesquisar o contato: "))
     opcao = int(input("digite 2 para excluir o ultimo contato: "))
     opcao = int(input("Digite 3 para encerrar o programa: "))
     match opcao:
         case 1:  
            buscaApelido(agenda)   
         case 2:
              agenda.pop()  
         case 3:
          break




    






       
        

        

"""

agenda = []
contato = {}

while True:
    opcao = int(input(f"Digite 0 para inserir um novo contato: ") )  
    match opcao:

        case 0:
            contato = {}#sem isso, vai ficar tudo repetido...
            apelido = input("Digite o apelido: ")
            contato["apelido"] = apelido
            nome_completo = input("Digite o nome completo: ")
            contato["nome_completo"] = nome_completo
            fixo = input(" Digite o telefone fixo: ")
            contato["fixo"] = fixo
            celular = input("Digite o telefone celular: ")
            contato["celular"] = celular
            agenda.append(contato)
        case 2:#consultar um contato a partir do nome usual
            buscaApelido(agenda)
            if  buscaApelido(agenda):
                 print("Contato Inexistente")
            break


        case 3:#exibir a listagem de todos os contatos em ordem alfabética
            pass
        case 4:#sair
            break

def buscaApelido(Agenda):
    apelido = input("Digite o apelido a procurar: ")
    for ele in Agenda:
        if ele["apelido"] == apelido:
            #print(f"nome completo = {ele['nome_completo']}")
            #print(f"Telefone fixo = {ele['fixo']}")
            #print(f"Telefone celular = {ele['celular']}")
            return ele        








"""
