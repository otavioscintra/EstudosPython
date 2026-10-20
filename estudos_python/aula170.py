# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\pc\Documents\EXEMPLO
# caminho = r'C:\\Users\\pc\\Documents\\EXEMPLO'
import os

caminho = os.path.join('C:\\Users', 'pc', 'Documents', 'EXEMPLO')
print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo):
        continue
    for imagem in os.listdir(caminho_completo):
        print(imagem)
