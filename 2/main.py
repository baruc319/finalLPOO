def main():
    try:
        print('*' * 30)
        print('informe 5 numeros:')     
        print('*' * 30)

        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        num3 = int(input('Informe o terceiro número: '))
        num4 = int(input('Informe o quarto número: '))
        num5 = int(input('Informe o quinto número: '))
#        if num1 > num2,  num3, num4,  num5:
#            print(f'{num1:.0f}')
    except ValueError:
        print('opção inválida')
    
    return

if __name__ == '__main__':
    main()