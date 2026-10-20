import os

while True:
    valor = input('Digite um valor: ')

    try:
        valor_float = float(valor)
    except ValueError:
        os.system('cls')
        print('Você não Digitou um número. Tente novamente.')
        continue

    valor_int = int(valor_float)

    print(f'O valor digitado foi {valor_float} e sua porção inteira é {valor_int}.')

    deseja_continuar = input('Deseja quebrar mais um número? [S]im: ').lower()

    if deseja_continuar == 's':
        os.system('cls')
    else:
        os.system('cls')
        break
print('Você saiu.')