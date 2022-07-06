class Country:
    def __init__(self, iso, nome, populacao, dimensao):
        self.iso = iso
        self.nome= nome
        self.populacao = populacao
        self.dimensao = dimensao

    def getIso(self):
        return self.iso
    def setIso(self, iso):
        self.iso = iso

    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome

    def getPopulacao(self):
        return self.populacao
    def setPopulacao(self, populacao):
        self.populacao = populacao

    def getDimensao(self):
        return self.dimensao
    def setDimensao(self, dimensao):
        self.dimensao = dimensao