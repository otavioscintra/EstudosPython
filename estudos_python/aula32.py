numero = input('Digite um número inteiro: ')
numero_int = int(numero)
if numero_int:
    if numero_int % 2 == 0:
        print(f'{numero} é um número par')
    else:
        print(f'{numero} é um número impar')

else:
    print('Você não digitou um número inteiro')


horario = input('Que horas são? ')
horario = int(horario)

if horario >= 0 and horario <= 11:
    print('Bom dia !!!')
elif horario >= 12 and horario <= 17:
    print('Boa tarde !!!')
else:
    print('Boa noite !!!')

nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print('seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('seu nome é normal')
    else:
        print('seu nome é muito grande')

else:
    print('Digite pelo menos uma letra')
