import os
import math

while True:
    angulo = input('Digite o angulo que você deseja: ')

    try:
        angulo = float(angulo)
    except ValueError:
        os.system('cls')
        print('você não digitou um ângulo. Tente novamente.')
        continue

    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    tangente = math.tan(math.radians(angulo))

    print(f'o seno de {angulo} é {seno:.2f}')
    print(f'o cosseno de {angulo} é {cosseno:.2f}')
    print(f'a tangente de {angulo} é {tangente:.2f}')

    deseja_continuar = input('print deseja efetuar mais um calculo de seno, cosseno e tangente? [S]im: ').lower()

    if deseja_continuar == 's':
        os.system('cls')
    else:
        os.system('cls')
        break
print('Você saiu.')


