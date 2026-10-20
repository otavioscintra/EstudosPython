# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Escolha uma letra: ')
    letras.add(letra)

    if 'l' in letras :
        print('PIKA')
        break

    print(letras)

