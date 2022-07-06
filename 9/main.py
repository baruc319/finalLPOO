from pessoa import Pessoa
from aluno import Aluno

pessoa1 = Pessoa('Michelangelo', 10)

aluno1 = Aluno('Rafael', 20, 'engenharia')

def main():
    try:
        print('*' * 30)
        print('Deseja instanciar um aluno ou uma pessoa?')
        print('1 - PESSOA')
        print('2 - ALUNO')
        opcao = int(input('INFORME A OPÇÃO DESEJADA: '))
        print('*' * 30)

        if opcao == 1:
            print('pessoa: ', pessoa1.getNome(), 'idade: ', pessoa1.getIdade())
        elif opcao == 2:
            print('aluno: ', aluno1.getNome(), 'idade: ', aluno1.getIdade(), 'curso: ', aluno1.getCurso)


    except ValueError:
        print('Opção inválida')

    return

if __name__ == '__main__':
    main()