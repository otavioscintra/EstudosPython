# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# numero_escolido_usuario = input('Escolha um número: ')

# def duplicar(numero_str):
#     numero_float = float(numero_str)
#     numero_duplicado = numero_float * 2
#     return numero_duplicado


# def triplicar(numero_str):
#     numero_float = float(numero_str)
#     numero_triplicado = numero_float * 3
#     return numero_triplicado


# def quadruplicar(numero_str):
#     numero_float = float(numero_str)
#     numero_quadruplicado = numero_float * 4
#     return numero_quadruplicado

# print(f'Duplicado: {duplicar(numero_escolido_usuario)}')
# print(f'Triplicado: {triplicar(numero_escolido_usuario)}')
# print(f'Quadruplicado: {quadruplicar(numero_escolido_usuario)}')


def criar_multiplicador(multiplicador):
    def multiplicado(numero):
        return numero * multiplicador
    return multiplicado

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)


print(triplicar(22))