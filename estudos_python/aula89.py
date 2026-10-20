# dir, hasattr e getattr em Python
string = 'Otávio'
metodo = 'upper'

if hasattr(string, metodo):
    print('EXISTE')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)