import os 

while True:
    numero_escolhido = input('Digite um número: ') 
    try:
        numero_escolhido = int(numero_escolhido)
    except ValueError:
        os.system('cls')
        print('Você não digitou um número, tente novamente.')
        continue

    dobro = numero_escolhido * 2
    triplo = numero_escolhido * 3
    raiz_quadrada = numero_escolhido ** 0.5

    print(f'o dobro de {numero_escolhido} é {dobro}',\
           f'o triplo de {numero_escolhido} é {triplo}',\
              f'a raiz quadrada de {numero_escolhido} é {raiz_quadrada:.2f}', sep=('\n'))
    
    deseja_sair = input('Deseja [S]air: ').lower()

    if deseja_sair == 's':
        break
    else:
        os.system('cls')
print('Você saiu')