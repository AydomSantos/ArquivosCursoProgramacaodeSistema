
"""

class ContaBancaria:
    def __init__(self, nomePessoa, numAgencia, numConta, valorSaldo):
        self.nomePessoa = nomePessoa
        self.numAgencia = numAgencia
        self.numConta = numConta
        self.valorSaldo = valorSaldo

    def Depositar(self, saldoDeposito):
        self.valorSaldo += saldoDeposito

    def Sacar(self, valorRetirado):
        if self.valorSaldo == 0:
            print("Não possue saldo!")
        else:
            self.valorSaldo -= valorRetirado

    def consultarSaldo(self, visualizar):
        visualizar = self.valorSaldo
        print(f"Seu saldo atual e: {visualizar}")

    def Transferir(self, numAge, numConta, numTransferir):
        self.numAge = int(numAge)
        self.numConta = str(numConta)
        self.numTransferir = numTransferir
        

        if self.valorSaldo < 0:
            print("Não tem saldo")
        elif numAge < 5 and numAge == str:
            print("o numero digitado e invalido !")
        elif len(numConta) < 6 and not numConta["zxcvbnmçlkjhgfdsaqwertyuiop"]:
            print("Numero invalido !!")
        else:
            print(f"Transferido com Sucesso o valor foi: {numTransferir}")
            result = self.valorSaldo - numTransferir
            print(f"Valor Atual e: {result}")
    def __str__(self):
        return f"Nome: {self.nomePessoa}\nNumero da conta: {self.numConta}\nSaldo: ${self.valorSaldo}"

        
contaUm = ContaBancaria("teste", 12345, "123456a", 0)
contaDois = ContaBancaria("teste02", 54123, "123445l", 0)
        
contaUm.Depositar(1000)
print(contaUm)

print("==================================================")

contaUm.Transferir(54123, "545545o", 1000)

print("==================================================")

print(contaDois)



"""

# resposta

class ContaBancaria:
    def __init__(self, nome_titular, numero_conta, saldo_inicial = 0):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo_inicial = saldo_inicial

    def depositar(self, valor_deposito):
        if valor_deposito < 0:
            print("Valor de depoito invalido")
        else:
            self.saldo_inicial += valor_deposito
    def sacar(self, valor_sacar):
        if valor_sacar > 0:
            if self.saldo_inicial >= valor_sacar:
                self.saldo_inicial -= valor_sacar
            else:
                print("Saldo insuficiente !")
        else:
            print("Valor de saque invalido")
    def consultar(self):
        return self.saldo_inicial
    def transferir(self, valor_transferi, conta_recebe):
        if valor_transferi > 0:
            if self.saldo_inicial >= valor_transferi:
                self.saldo_inicial -= valor_transferi
                conta_recebe.depositar(valor_transferi)
                print("Transferencia feita com Sucesso")
            else:
                print("Não possui saldo !")
        else:
            print("valor da transferencia")
        