def main():
    try:
        num = int(input('Informe um numero inteiro: '))
        if num / num == 1:
            print('Número primo')
#        if not num / num == 1:
#            print('não é primo')

    except ValueError:
            print('opção invállida')

    return

if __name__ == '__main__':
    main()
