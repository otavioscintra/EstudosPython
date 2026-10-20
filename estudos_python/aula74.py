"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar
    

bom_dia = criar_saudacao('Bom dia')
boa_noite = criar_saudacao('Boa noite')

nomes_brasileiros = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Henrique", "Isabela", "João", "Karina",\
"Lucas", "Mariana", "Nicolas", "Olivia", "Paulo", "Quiteria", "Rafael", "Sofia", "Thiago", "Vanessa", "Wesley", "Yasmin", "Zé", "Lívia"]

for nome in nomes_brasileiros:
    print(bom_dia(nome))
    print(boa_noite(nome))
    print('----------------------')