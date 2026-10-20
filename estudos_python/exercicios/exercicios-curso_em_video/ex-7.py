import os

while True:
    primeira_nota = input('Digite a primeira nota do aluno: ')
    segunda_nota = input('Digite a segunda nota do aluno: ')

    try:
        primeira_nota = float(primeira_nota)
        segunda_nota = float(segunda_nota)
    except ValueError:
        os.system('cls')
        print('Você não digitou um número em uma das notas.')
        continue

    media = (primeira_nota + segunda_nota) / 2

    print(f'a media entre {primeira_nota} e {segunda_nota} é {media:.1f}')

    deseja_sair = input('Deseja [S]air: ').lower()

    if deseja_sair == 's':
        break
    else:
        os.system('cls')
print('Você saiu')