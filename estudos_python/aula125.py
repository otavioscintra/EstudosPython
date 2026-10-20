# Atributos de classe


class Pessoa:
    ano_atual = 2025 # já É 2026, mas colocando 2025 o calculo fica mais correto(pelo menos no dia que estou. 06/01)
    atributo = 'Valor'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def GetAnoNascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Otávio', 15)
p2 = Pessoa('Cleber', 33)
print(p1.GetAnoNascimento())
print(p2.GetAnoNascimento())