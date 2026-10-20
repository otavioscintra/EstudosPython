"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []

while True:
    opcao = input(f'Escolha uma opção abaixo \n \
[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        

    elif opcao == 'l':

        if len(lista) == 0 :
            print('Nada para listar.')
            
            
        os.system('cls')
        for indice, valor in enumerate(lista):
            print(indice, valor)

    elif opcao == 'a': 
        indice_str = input('Escolha o indice do item que quer apagar: ')
        try :
            indice = int(indice_str)
            del lista[indice]

        except ValueError:
            print('Por favor digite número int.')

        except IndexError:
            print('Índice não existe na lista')

        except Exception:
            print('Erro desconhecido')

    else:
        print('Por favor, digite i, a ou l.')
        
        


    




