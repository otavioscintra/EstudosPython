# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ],
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

# pessoa = {
#     'nome': 'Otávio',
#     'sobrenome': 'Cintra',
#     'idade': 14,
#     'altura': 1.79,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ],
# }

# print(pessoa, type(pessoa))

# print(pessoa['altura'])
# print(pessoa['nome'])
# print(pessoa['sobrenome'])
# print('------------')

# for chave in pessoa:
#     print(chave, pessoa[chave])


# Manipulando chaves e valores em dicionários
# pessoa = {}

# ##
# ##

# chave = 'Nome'

# pessoa[chave] = 'Otavio'
# pessoa['sobrenome'] = 'Cintra'

# print(pessoa[chave])

# pessoa[chave] = 'cleber'

# del pessoa['sobrenome']
# print(pessoa)
# print('nome')

# print(pessoa.get('sobrenome'))
# if pessoa.get('sobrenome', None) is None:
#     print('existe')


# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# pessoa = {
#     'nome': 'Otávio',
#     'sobrenome': 'Cintra',
#     # 'idade': 900,
# }
# pessoa.setdefault('idade', 33)
# print(pessoa['idade'])
# # print(len(pessoa))
# # print(tuple(pessoa.keys()))
# # print(list(pessoa.items()))
# # print(list(pessoa.items()))


# for valor in pessoa.items():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2]
# }

# d2 = copy.deepcopy(d1)

# d2['c1'] = 777
# d1['l1'][1] = 99999

# print(d1)
# print(d2)

p1 ={
    'nome': 'Otávio',
    'sobrenome': 'Cintra'
}
# print(p1.get('nome', 'sem nome'))

# nome = p1.pop('nome')
# print(nome, p1)

# sobrenome = p1.popitem()
# print(sobrenome, p1)

# p1.update({
#     'sobrenome': 'silveira',
#     'idade': 14,
# })
# p1.update(nome= 'novo valor', idade= '14')
tupla = ('nome', 'novo valor'), ('idade', 14)
lista = ['nome', 'novo valor'], ['idade', 14]
p1.update(tupla)
p1.update(lista)
print(p1)

