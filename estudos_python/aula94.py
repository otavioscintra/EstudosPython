# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('ABRIR ARQUIVO')
    8/0

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU POR ZERO.')

else:
    print('NÃO DEU ERRO.')
finally:
    print('FECHAR ARQUIVO')