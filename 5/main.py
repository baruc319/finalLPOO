from produto import Produto


produto1 = Produto('Banana', 1, 3)
produto2 = Produto('Maçã', 2, 6)
produto3 = Produto('Pera', 3, 9)


def main():
    try:
        print('PRODUTO: ', produto1.getNome(), 'QUANTIDADE: ', produto1.getQuantidade(), 'PREÇO: ', produto1.getPreco())
        forma = int(input(''' Informe a forma de pagamento:
        1 - Dinheiro
        2 - Cheque
        3 - Cartão
        '''))
        if forma == 1:
            dinheiro = int(input('Informe o valor da cédula: '))
            troco = dinheiro - produto1.getPreco() * produto1.getQuantidade()
            print('O seu troco é: ', troco)
        elif forma == 2:
            print('pagamento com cheque efetuado') 
        elif forma == 3:
            print('pagamento com cartão efetuado')

        main()

    except ValueError:
        print('Opção inválida')

    return

if __name__ == '__main__':
    main()