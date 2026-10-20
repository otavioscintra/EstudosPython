import os

while True:
    numero_escolhido = input('Digite um número: ')

    try:
        numero_escolhido = int(numero_escolhido)

    except ValueError:
        print('Você não digitou um número, Tente novamente.')
        continue

    antecessor = numero_escolhido - 1
    sucessor = numero_escolhido + 1 

    print(f'Analisando o valor {numero_escolhido}, seu antecessor é {antecessor} e seu sucessor é {sucessor}.')

