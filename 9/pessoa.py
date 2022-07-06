class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome
    
    def getIdade(self):
        return self.idade
    def setIdade(self, idade):
        self.idade = idade


#pessoa1 = Pessoa('Michelangelo', 10)

#dados = print('NOME: ', pessoa1.getNome(), 'IDADE: ', pessoa1.getIdade())