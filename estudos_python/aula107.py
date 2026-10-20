# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

'''
Código que eu fiz (funcionando):
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']
def zipper(lista_1, lista_2):
    number = 0
    city_state = []
    if len(lista_1) < len(lista_2):
        amount = lista_1
    else:
        amount = lista_2
    for i in amount:
        city_state.append((cidades[number], estados[number]))
        number += 1
    return city_state

print(zipper(cidades, estados))

if zipper(cidades, estados) == [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]:
    print('Deu bom')
'''

'''
Código usando o que aprendi na resolução:
def zipper(lista_1, lista_2):   
    intervalo_maximo =  min(len(lista_1), len(lista_2))
    return [(lista_1[i], lista_2[i]) for i in range(intervalo_maximo)]



from itertools import zip_longest

cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']
print(list(zip_longest(cities,states)))
'''

"""
Exercicio - Somando duas listas.
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

def sum_lists(list_1,list_2):
    max_interval = min(len(list_1), len(list_2))
    try:
        return [(list_1[i] +list_2[i]) for i in range(max_interval)]
    except IndentationError:
        raise IndentationError('Não é possivel somar um dos valores acima. ')
    
list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = [1, 2, 3, 4, 55, 77]
    
print(sum_lists(list_1,list_2))







