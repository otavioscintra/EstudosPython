# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a,b)



# (nome,nome1),(sobrenome,sobrenome1) = pessoa.items()
# print(nome,nome1,sobrenome,sobrenome1)

# for chave,valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 14,
    'altura': 1.79,
}

pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args,**kwargs):
    print('NÃO NOMEADOS:', args)
    for chave, valor in kwargs.items():
        print(chave,valor)

# mostro_argumentos_nomeados(1,2,nome='Joana',sobrenome='silva',)
# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,

}

mostro_argumentos_nomeados(**configuracoes)