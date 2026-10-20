# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

class A:
    def __new__(cls, *args, **kwargs):
        print('antes de criar a instancia')
        instancia = super().__new__(cls)
        instancia.x = 231
        return instancia 

    def __init__(self,x):
        print('sou o init')

    def __repr__(self):
        return f'A()'
    
a = A()
print(a.x)