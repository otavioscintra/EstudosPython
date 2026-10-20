import os

while True:
    largura_parede = input('largura da parede(Metros): ')
    altura_parede = input('altura da parede da parede(Metros): ')
    
    try:
        largura_parede = float(largura_parede)
        altura_parede = float(altura_parede)
    except ValueError:
        os.system('cls')
        print('Você não digitou as medidas. tente novamente. ')
        continue

    area_parede = largura_parede * altura_parede

    litros_tinta = area_parede / 2

    print(f'Sua parede tem a dimensão de {largura_parede}X{altura_parede} e sua área é de {area_parede:.3f}m².',\
          f'Para pintar essa parede, você precisará de {litros_tinta}L de tinta.')

    deseja_continuar = input('Deseja continuar? [S]im: ').lower()

    if deseja_continuar == 's':
        os.system('cls')
        continue

    else:
        os.system('cls')
        break

print('Você saiu')
