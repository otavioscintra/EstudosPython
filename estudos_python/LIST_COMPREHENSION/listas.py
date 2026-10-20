#https://www.youtube.com/watch?v=1YbTDczvqco

nomes = ['joão', 'maria', 'pedro', 'ana', 'lucas']
novos_nomes = [f'{nome[:-1].lower() + nome[-1].upper()}' for nome in nomes]
print(novos_nomes)