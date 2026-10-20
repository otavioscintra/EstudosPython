import os

while True:
    metros = input('Digite uma distância em metros: ')
    try:
        metros = float(metros)
    except ValueError:
        os.system('cls')
        print('Você não digitou um número. Tente novamente')
        continue

    km = metros / 1000
    hm = metros / 100
    dam = metros / 10
    dm = metros * 10
    cm = metros * 100
    mm = metros * 1000

    print(f'a medida de {metros} corresponde a',\
          f'{km} km', f'{hm} hm', f'{dam} dam', f'{dm} dm', f'{cm} cm', f'{mm} mm', sep= '\n')
    
    deseja_sair = input('Deseja [S]air: ').lower()

    if deseja_sair == 's':
        break
    else:
        os.system('cls')
os.system('cls')
print('Você saiu')
    