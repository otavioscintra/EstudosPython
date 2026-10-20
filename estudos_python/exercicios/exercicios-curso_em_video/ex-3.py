
import os

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro numero número: ')

    try:
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
    except ValueError:
        os.system('cls')
        print('Você não digitou um número.')
        continue

    soma = numero_1 + numero_2

    print(f'A soma dos números ({numero_1} + {numero_2}) é {soma}.')

    opcao = input('Deseja [S]air: ').lower()

    if opcao == 's':
        os.system('cls')
        break

    else:
        continue

