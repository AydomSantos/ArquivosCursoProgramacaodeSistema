
# Introdução ao paradigma de programação POO:

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}"
    
    def Emagrecer(self, novoPeso):
         result = self.peso - novoPeso
         return f"O seu Novo Peso e: {result}"
    
    def Envelhecer(self, novaIdade):
        result = self.idade + novaIdade
        return f"Sua nova Idade e {result}"
    
    def AumentaAltura(self, novaAltura):
        result = self.altura + novaAltura
        return f"sua Nova Altura: {result}"


p1 = Pessoa("Aydom", 23, 60, 1.70)






    




# = = = = = = = = = = = = = = = = = = = = = 