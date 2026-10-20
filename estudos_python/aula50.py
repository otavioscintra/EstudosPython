"""
Exercício
Exiba os índices da lista
Maria
Helena
Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Otávio')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    