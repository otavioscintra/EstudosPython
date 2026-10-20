# (Parte 2) try e except para tratar exceções
# a = 18
# b = 0
# c = a/b


try:
    a = 18
    b = 0
    # print(b[0])
    # print('oi'[1000])
    c = a/b
    print('oi dnv')
    ...

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)

except NameError:
    print('Algum nome não está definido.')

except (TypeError, IndexError) as error:
    print('TypeError Or IndexError')
    print('MSG:',error)
    print('NOME:',error.__class__.__name__)

except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
    