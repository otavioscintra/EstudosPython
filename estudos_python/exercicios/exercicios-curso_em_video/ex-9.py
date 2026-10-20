import os

while True:
    numero_escolhido = input('Digite um número para ver sua tabuada: ')

    try:
        numero_escolhido = int(numero_escolhido)
    except ValueError:
        os.system('cls')
        print('Você não digitou um número. Tente novamente.')
        continue

    vezes_1 = numero_escolhido * 1
    vezes_2 = numero_escolhido * 2
    vezes_3 = numero_escolhido * 3
    vezes_4 = numero_escolhido * 4
    vezes_5 = numero_escolhido * 5
    vezes_6 = numero_escolhido * 6
    vezes_7 = numero_escolhido * 7
    vezes_8 = numero_escolhido * 8
    vezes_9 = numero_escolhido * 9
    vezes_10 = numero_escolhido * 10

    print(
        '-' * 12,\
         f'{numero_escolhido} X  1 = {vezes_1}',\
         f'{numero_escolhido} X  2 = {vezes_2}',\
         f'{numero_escolhido} X  3 = {vezes_3}',\
         f'{numero_escolhido} X  4 = {vezes_4}',\
         f'{numero_escolhido} X  5 = {vezes_5}',\
         f'{numero_escolhido} X  6 = {vezes_6}',\
         f'{numero_escolhido} X  7 = {vezes_7}',\
         f'{numero_escolhido} X  8 = {vezes_8}',\
         f'{numero_escolhido} X  9 = {vezes_9}',\
         f'{numero_escolhido} X 10 = {vezes_10}',\
         '-' * 12, 
         sep= '\n'
          )
    
    deseja_continuar = input('Deseja efetuar mais uma tabuaba? [S]im: ').lower()

    if deseja_continuar == 's':
        os.system('cls')

    else:
        os.system('cls')
        break

print('Você saiu.')
