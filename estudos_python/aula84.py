# # Introdução à List comprehension em Python
# # List comprehension é uma forma rápida para criar listas
# # a partir de iteráveis.
# import pprint

# # print(list(range(10)))

# lista = []

# def p(v):
#     pprint.pprint(v, sort_dicts=False,width=40)

# for numero in range(10):
#     if numero % 2 == 0:
#         lista.append(numero)
#     else:
#         lista.append('-')

# # print(lista)

# lista = [
#      numero * numero
#        for numero in range(10)
#        ]

# # print(lista)

# # Mapeamento de dados em list comprehension
# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]

# novos_produtos = [
#     {**produto,'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]

# # print(*novos_produtos, sep ='\n')

# # pprint.pprint(novos_produtos, sort_dicts=False,width=40)

# # lista = [n for n in range(10) if n < 5]

# novos_produtos = [
#     {**produto,'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if produto['preco'] >= 20 and (produto['preco'] * 1.05) > 10 
# ]

# p(novos_produtos)



