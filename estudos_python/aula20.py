primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(
         f'O primeiro_valor={primeiro_valor} é maior '
         f'que o segundo_valor={segundo_valor}'
         ) 
elif segundo_valor > primeiro_valor:
    print(
         f'O segundo_valor={segundo_valor} é maior '
         f'que o primeiro_valor={primeiro_valor}'
         )
else: 
    print(
         f'o primeiro_valor={primeiro_valor} é igual '
         f'ao segundo_valor={segundo_valor}'
         )
    