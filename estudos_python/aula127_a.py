# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'C:\\Users\\pc\\Documents\\curso_python\\aulas\\arquivos_json\\aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Otávio', 15)
p2 = Pessoa('cleber', 22)
p3 = Pessoa('sla', 99)
bd = [vars(p1),vars(p2),vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(bd,  arquivo, ensure_ascii=False, indent=2)

if __name__ == 'main':
    fazer_dump()
