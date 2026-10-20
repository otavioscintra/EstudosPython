import os

while True:
    cateto_oposto = input('comprimento do cateto oposto: ')
    cateto_adjacente = input('comprimento do cateto adjacente: ')

    try:
        cateto_oposto = float(cateto_oposto)
        cateto_adjacente = float(cateto_adjacente)
    except ValueError:
        os.system('cls')
        print('Você não digitou uma medida. Tente novamente.')
        continue

    hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5

    print(f'a hipotenusa vai medir {hipotenusa:.2f}')

    deseja_continuar = input('Deseja calcular mais uma hipotenusa? [S]im: ').lower()

    if deseja_continuar == 's':
        os.system('cls')
    else:
        os.system('cls')
        break
print('Você saiu.')