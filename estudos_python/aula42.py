frase = 'aaaooo'

i = 0
qnt_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ' :
        i += 1
        continue

    qnt_atual = frase.count(letra_atual)

    if qnt_apareceu_mais_vezes < qnt_atual:
        qnt_apareceu_mais_vezes = qnt_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}", com {qnt_apareceu_mais_vezes} aparições.')