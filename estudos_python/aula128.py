# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2026 # atributo de classe

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônimo', idade)

p1 = Pessoa('Otávio', 15)
p2 = Pessoa.criar_sem_nome(44)
p3 = Pessoa.criar_sem_nome(67)
p4 = Pessoa('Anônimo', 39)
print(p2.name, p2.age)