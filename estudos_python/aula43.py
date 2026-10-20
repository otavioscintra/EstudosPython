texto = 'python'

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
    
novo_texto = f'{novo_texto}*'
    
print(novo_texto)