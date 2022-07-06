class Pessoa:
    def __init__(self, nome, data, altura):
        self.__nome = nome
        self.__data = data
        self.__altura = altura

    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome

    def getData(self):
        return self.__data
    def setData(self, data):
        self.__data = data

    def getAltura(self):
        return self.__altura 
    def setAltura(self, altura):
        self.__altura = altura

    def calcIdade(self):
        return  2022 - self.__data 

