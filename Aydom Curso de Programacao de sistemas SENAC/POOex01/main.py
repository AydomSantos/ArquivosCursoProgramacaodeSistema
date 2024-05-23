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
            print("Não possui saldo!")
        elif self.valorSaldo < valorRetirado:
            print("Saldo insuficiente!")
        else:
            self.valorSaldo -= valorRetirado

    def consultarSaldo(self):
        print(f"Seu saldo atual é: {self.valorSaldo}")

    def Transferir(self, contaDestino, valorTransferir):
        if self.valorSaldo < valorTransferir:
            print("Não tem saldo suficiente")
        else:
            self.valorSaldo -= valorTransferir
            contaDestino.Depositar(valorTransferir)
            print(f"Transferido com sucesso o valor de: {valorTransferir}")
            print(f"Seu saldo atual é: {self.valorSaldo}")

    def __str__(self):
        return f"Nome: {self.nomePessoa}\nNúmero da agência: {self.numAgencia}\nNúmero da conta: {self.numConta}\nSaldo: R${self.valorSaldo:.2f}"

# Exemplos de uso
contaUm = ContaBancaria("teste", 12345, "123456a", 0)
contaDois = ContaBancaria("teste02", 54123, "123445l", 0)

