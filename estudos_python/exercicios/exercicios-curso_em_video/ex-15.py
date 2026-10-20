import os

while True:
    dias_alugados = input('Quantos dias alugados? ')
    km_rodados = input('Quantos Km rodados? ')

    try:
        dias_alugados = int(dias_alugados)
        km_rodados = float(km_rodados)
    except:
        os.system('cls')
        print('Você não digitou um número. Tente novamente.')
        continue

    pagar_dias = dias_alugados * 60
    pagar_km_rodados = km_rodados * 0.15
    total_pagar = pagar_dias + pagar_km_rodados

    print(f'O total a pagar é {total_pagar} reais.')

    deseja_continuar = input('print deseja efetuar mais um calcula para descobrir o valor a pagar? [S]im: ').lower()

    if deseja_continuar == 's':
        os.system('cls')
    else:
        os.system('cls')
        break
print('Você saiu.')
