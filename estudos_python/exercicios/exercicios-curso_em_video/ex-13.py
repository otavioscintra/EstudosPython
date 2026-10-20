import os

while True:
    salario = input('Qual é o salário do funcionário? R$')

    try:
        salario = float(salario)
    except ValueError:
        os.system('cls')
        print('Você não digitou um valor em reais. Tente novamente.')
        continue

    aumento = salario * 15 / 100
    salario_com_aumento = salario + aumento

    print(f'um funcionário que ganhar {salario}, com 15% de aumento, passa a ganhar {salario_com_aumento:.2f}')

    deseja_continuar = input('Deseja calcular mais um aumento? [S]im: ').lower()

    if deseja_continuar == 's':
        os.system('cls')

    else:
        os.system('cls')
        break

print('Você saiu.')