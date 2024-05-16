
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