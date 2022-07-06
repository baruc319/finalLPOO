from country import Country

country1 = Country(123, 'Brasil', 200, 10)
country2 = Country(456, 'Guiné', 80, 2)

print('PAÍS 1')
print('ISO: ', country1.getIso(), 'NOME: ', country1.getNome(), 'POPULAÇÃO: ', country1.getPopulacao(), 'DIMENSÃO: ', country1.getDimensao())
print('*' * 30)
print('PAÍS 2')
print('ISO: ', country2.getIso(), 'NOME: ', country2.getNome(), 'POPULAÇÃO: ', country2.getPopulacao(), 'DIMENSÃO: ', country2.getDimensao())
