"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = '     Olha só que    , coisa interessante             '
lista_frases_raw = frase.split(', ')

lista_frases = []
for i, frase in enumerate(lista_frases_raw):
    lista_frases.append(lista_frases_raw[i].strip())

# print(lista_frases_raw)
# print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)