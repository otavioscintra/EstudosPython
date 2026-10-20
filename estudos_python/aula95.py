# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você tentou dividir por zero.')
    return True
    
def apenas_int_float(n,d):
    if not isinstance((n), (int, float)):
        tipo_n = type(n)
        raise TypeError(f'"{n}" deve ser int ou float', f'"{tipo_n.__name__}" enviado.')
    if not isinstance((d), (int, float)):
        tipo_d = type(d)
        raise TypeError(f'"{d}" deve ser int ou float', f'"{tipo_d.__name__}" enviado.')
    
    return True

def divide(n, d):
    nao_aceito_zero(d)
    apenas_int_float(n,d)
    return n/d

print(divide(8,'i'))
