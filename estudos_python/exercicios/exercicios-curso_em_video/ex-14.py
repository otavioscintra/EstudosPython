import os

while True:
    temperatura_celsius = input('temperatura em °C: ')

    try:
        temperatura_celsius = float(temperatura_celsius)
    except ValueError:
        os.system('cls')
        print('Você não digitou um número. Tente novamente.')
        continue
    
    temperatura_fahrenheit = ((9*temperatura_celsius)/5) + 32

    print(f'A temperatura de {temperatura_celsius}°C corresponde a {temperatura_fahrenheit:.1f}°F. ')

    deseja_continuar = input('Deseja efetuar mais uma conversão? [S]im: ').lower()

    if deseja_continuar == 's':
        os.system('cls')
        continue

    else:
        os.system('cls')
        break

print('Você saiu.')