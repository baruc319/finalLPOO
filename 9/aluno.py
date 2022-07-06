from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    
    def getCurso(self):
        return self.curso
    def setCurso(self, curso):
        self.curso = curso

aluno1 = Aluno('Rafael', 20, 'engenharia')
