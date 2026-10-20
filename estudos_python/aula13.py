nome = 'Otávio Cintra'
altura = 1.80
peso = 95.1
imc = peso / altura ** 2
dinheiro = 100000.444

linha_1 = f'{nome} tem {altura:.2f} metros de altura'

print(nome,'tem',altura,'metros de altura')
print(linha_1)
print(f'{nome} tem {dinheiro:,.2f} reais ')
#tem q f na frente da str ex: f''
# o nome disso é f-strings