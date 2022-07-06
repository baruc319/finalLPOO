#from circulo import Circulo

#circulo = Circulo()
pi = 3.14

def main():
    try:
        area_circulo = int(input('Informe a área desejada: '))
        area = pi * area_circulo ** 2
        print(f'O resultado é: {area}')

    except ValueError:
            print('opção invállida')

    return

if __name__ == '__main__':
    main()
