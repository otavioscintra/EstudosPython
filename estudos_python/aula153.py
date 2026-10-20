# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe:
    def __init__(self,phone):
        self.phone = phone

    def __call__(self, nome):
        print(f'chamando o telefone {self.phone} de {nome}')
        return 'qlqr coisa'
    
call1 = CallMe('18237128')
return_ = call1('Otávio')
print(return_)