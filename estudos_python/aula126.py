# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2025 # já É 2026, mas colocando 2025 o calculo fica mais correto(pelo menos no dia que estou. 06/01)
    atributo = 'Valor'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def GetAnoNascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome': 'Otávio', 'idade': 15} 
p1 = Pessoa(**dados)
p1.__dict__['outra'] = 'coisa'
print(p1.__dict__)
print(p1.outra)
print(vars(p1))