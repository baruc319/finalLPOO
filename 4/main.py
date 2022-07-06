from pessoa import Pessoa

pessoa = Pessoa('pelé', 1970, 2)

print(pessoa.getNome(), pessoa.getData(), pessoa.getAltura())
print('A idade do Pelé é: ', pessoa.calcIdade())