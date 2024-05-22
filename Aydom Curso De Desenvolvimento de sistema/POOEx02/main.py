

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

    def ConsultarSaldo(self, visualizar):
        visualizar = self.valorSaldo
        print(f"Seu saldo atual e: {visualizar}")

    def Transferir(self, numAge, numConta, numTransferir):
        self.numAge = int(numAge)
        self.numConta = str(numConta)
        self.numTransferir = numTransferir
        

        if self.valorSaldo < 0:
            print("Não tem saldo")
        elif numAge < 5:
            print("o numero digitado e invalido !")
        elif len(numConta) < 6 and not numConta["zxcvbnmçlkjhgfdsaqwertyuiop"]:
            print("Numero invalido !!")
        else:
            print(f"Transferido com Sucesso o valor foi: {numTransferir}")
            result = self.valorSaldo - numTransferir
            print(f"Valor Atual e: {result}")
    def __str__(self):
        return f"Nome: {self.nomePessoa}\nNumero da conta: {self.numConta}\nSaldo: ${self.valorSaldo}"

        
testeUm = ContaBancaria("Aydom do teste silva", 123456, 12345, 1030)

testeUm.Depositar(1003)
testeUm.Sacar(500)
testeUm.ConsultarSaldo(testeUm)
testeUm.Transferir(12345, "1234565", 1000)



    


        