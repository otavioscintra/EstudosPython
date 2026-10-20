import os

while True:
    preco = input('Qual o preço do produto? R$')

    try:
        preco = float(preco)
    except ValueError:
        print('Você não digitou um valor em reais. Tente novamente.')
        continue

    desconto = preco * 5 / 100
    preco_desconto = preco - desconto

    print(f'o produto custava {preco}, mas com o desconto de 5% passou a custar {preco_desconto:.2f}')

    deseja_continuar = input('Deseja calcular mais um desconto? [S]im: ').lower()

    if deseja_continuar == 's':
        os.system('cls')
        continue

    else:
        os.system('cls')
        break

print('Você saiu')