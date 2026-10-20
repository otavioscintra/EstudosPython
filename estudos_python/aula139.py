# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         return super().upper()

# string = MinhaString('Otávio')
# print(string.upper())


class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('pika')

    def metodo(self):
        # super().metodo()
        # super(B, self).metodo()
        # print('C')
        A.metodo(self)

c = C('atributo', 'outra coisa')
print(c.atributo)
print(c.outra_coisa)

# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
c.metodo()

# print(C.mro())