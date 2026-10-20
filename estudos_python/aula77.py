# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

escolha = 0
acertos = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])

    for alternativa in pergunta['Opções']:
        print(f'{escolha}.) {alternativa}')
        escolha += 1

    escolhido_usuario_str = input('Escolha a opção correta: ')
    escolhido_usuario_int = int(escolhido_usuario_str)
    resposta_usuario = pergunta['Opções'][escolhido_usuario_int]
    print()

    if resposta_usuario == pergunta['Resposta']:
        print('Acertou 🎉')
    else:
        print('Errou ❌')
    print()

    escolha = 0
    if resposta_usuario == pergunta['Resposta']:
        acertos += 1

print(f'Você acertou {acertos} de 3 perguntas')
    
