# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista1 = []
clientes1 = adiciona_clientes('luiz', lista1)
adiciona_clientes('Joana', lista1)
adiciona_clientes('ccc', clientes1)
print(clientes1)

lista2 = []
clientes2 = adiciona_clientes('maria', lista2)
adiciona_clientes('cleber', lista2)
print(clientes2)
