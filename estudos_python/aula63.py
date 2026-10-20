""" 
essa aula está igual a aula passada, só copiei pra ficar com o numero de aulas igual ao do professor
"""



"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import sys

cpf_enviado_usuario = '908.787.950-49'.replace('.', '').replace('-', '')
nove_digitos = cpf_enviado_usuario[:9]
multiplicar = 10
soma = 0

enviado_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)
if enviado_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()


for numero in nove_digitos:
    numero = int(numero)
    numero_multiplicado = numero * multiplicar
    soma += numero_multiplicado
    multiplicar -= 1

soma_multiplicada = soma * 10
resto_divisao = soma_multiplicada % 11
primeiro_digito = resto_divisao if resto_divisao <= 9 else 0

primeiro_digito = str(primeiro_digito)
dez_digitos = nove_digitos + primeiro_digito
multiplicar = 11
soma = 0 

for numero in dez_digitos:
    numero = int(numero)
    numero_multiplicado = numero * multiplicar
    soma += numero_multiplicado
    multiplicar -= 1

soma_multiplicada = soma * 10
resto_divisao = soma_multiplicada % 11
segundo_digito = resto_divisao if resto_divisao <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_gerado_pelo_calculo == cpf_enviado_usuario:
    print(f'{cpf_enviado_usuario} é valido.')

else:
    print(f'{cpf_enviado_usuario} não é válido.')