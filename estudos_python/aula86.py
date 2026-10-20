# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave,valor in produto.items()
    if chave != 'nome' 
    }

lista = [
    ('a',' valor a'),
    ('d','valor d'),
    ('c','valor c'),
]

# dc = {
#     chave: valor
#     for chave, valor in lista
# }

print(dict(lista))

s1 = {i ** 2 for i in range(1,11)}

print(s1)

