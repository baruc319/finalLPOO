class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome
    def setNome(self,nome):
        self.nome = nome

    def getIdade(self):
        return self.idade
    def setIdade(self, idade):
        self.idade = idade

class Pai(Pessoa):
    def __init__(self, nome, idade, pai):
        super().__init__(nome, idade)
        self.pai = pai

    def getPai(self):
        return self.pai
    def setPai(self, pai):
        self.pai = pai 

class Mae(Pessoa):
    def __init__(self, nome, idade, mae):
        super().__init__(nome, idade)
        self.mae = mae

    def getMae(self):
        return self.mae
    def setMae(self, mae):
        self.mae = mae

pessoa = Pessoa('B', 3)
pai = Pai('E', 1, 'PAI')
mae = Mae('N', 2, 'MAE')

print(pessoa.getNome(), 'Idade: ', pessoa.getIdade())
print('Nome: ', pai.getNome(), 'Idade: ', pai.getIdade(), pai.getPai())
print('Nome: ', mae.getNome(), 'Idade: ', mae.getIdade(), mae.getMae())