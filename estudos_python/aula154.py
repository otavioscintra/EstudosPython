# Classes decoradoras (Decorator classes)

class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def intern(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return intern


@Multiplicar(11)
def soma(x,y):
    return x + y

two_plus_four = soma(2,4)
print(two_plus_four)