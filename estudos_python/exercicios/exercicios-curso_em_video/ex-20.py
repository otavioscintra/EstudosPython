import random
import os

while True:
    aluno_1 = input('primeiro aluno: ')
    aluno_2 = input('segundo aluno: ')
    aluno_3 = input('terceiro aluno: ')
    aluno_4 = input('quarto aluno: ')

    alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
    random.shuffle(alunos)

    print('a ordem da apresentação será:',
           f'{alunos}', sep= '\n' )

    deseja_continuar = input('print deseja efetuar mais um sorteio? [S]im: ').lower()

    if deseja_continuar == 's':
        os.system('cls')
    else:
        os.system('cls')
        break
print('Você saiu.')