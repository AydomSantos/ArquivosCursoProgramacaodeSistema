"""
agenda = []

# função responsavel pela pesquisa do contato pelo apelido

def buscaApelido(agenda):
    apelido = input("Digite o apelido a procurar: ")
    for ele in agenda:
        if ele["Apelido"] == apelido:
            print(f"nome completo = {ele['Nome']}")
            print(f"Telefone fixo = {ele['Telefone Fixo']}")
            print(f"Telefone celular = {ele['celular']}")
            return ele 
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
        
# iniciara a inserção das informações a lista agenda e a biblioteca contatos
        
while True:
    opcao = int(input("Digite 1 para inserir um novo contato, 2 para encerrar o programa: "))
    if opcao == 1:
        contato = {}
        apelido = input("Digite o apelido: ")
        contato["Apelido"] = apelido
        nomeCompleto = input("Digite o nome completo: ")
        contato["Nome"] = nomeCompleto
        telFixo = input("Digite o telefone fixo: ")
        contato["Telefone Fixo"] = telFixo
        celular = input("Digite o telefone celular: ")
        contato["celular"] = celular
        agenda.append(contato)
    elif opcao == 2:
        break
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    
# fara pesquisa por apelido e retornara os dados relacionados a pesquisa
# e podera deletar o ultimo contato inserido
      
while True:
    opcao = int(input("Digite 1 para Pesquisar o contato, 2 para excluir o ultimo contato, 3 para encerrar o programa: "))
    if opcao == 1:
        buscaApelido(agenda)
    elif opcao == 2:
        if agenda:
            agenda.pop()
        else:
            print("Agenda vazia, não há contatos para excluir.")
    elif opcao == 3:
        break
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""

def listadeCompras():
    # iniciando a lista itens vazia 
    itens = []

    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Visualizar itens")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            item = input("Digite o nome do item a adicionar: ")
            itens.append(item)
            print(f"{item} adicionado à lista de compras.")
        elif opcao == "2":
            if itens:
                itemRemover = input("Digite o nome do item a remover: ")
                if itemRemover in itens:
                    itens.remove(itemRemover)
                    print(f"{itemRemover} removido da lista de compras.")
                else:
                    print(f"{itemRemover} não encontrado na lista de compras.")
            else:
                print("A lista de compras está vazia.")
        elif opcao == "3":
            if itens:
                print("\nItens na lista de compras:")
                for item in itens:
                    print(item)
            else:
                print("A lista de compras está vazia.")
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

listadeCompras()



