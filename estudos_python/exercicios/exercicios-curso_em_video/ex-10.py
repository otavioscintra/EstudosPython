import os

while True:
    dinheiro_usuario = input('Quanto dinheiro você tem? R$')

    try:
        dinheiro_usuario = float(dinheiro_usuario)
    except ValueError:
        print('Você não digitou uma quantia em dinheiro. Tente novamente.')
        continue

    dolares_compraveis = dinheiro_usuario / 5.56
    euros_compraveis = dinheiro_usuario / 6.47
    yens_compraveis = dinheiro_usuario / 0.037


    print(f'Com R${dinheiro_usuario} você pode comprar:',\
           f'US${dolares_compraveis:.2f}',\
           f'¥{yens_compraveis:.2f}',\
           f'€{euros_compraveis:.2f}',\
           sep= '\n')

    deseja_continuar = input('Deseja efetuar mais uma conversão? [S]im.').lower()

    if deseja_continuar == 's':
        os.system('cls')
        continue

    else:
        os.system('cls')
        break

print('Você saiu')
