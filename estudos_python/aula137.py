# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

    def informar_motor(self, motor='Não informado'):
        self.motor = motor 

    def informar_fabricante(self, fabricante='Não informado'):
        self.fabricante = fabricante

    def informacoes(self):
        print(f'Informações do Carro:', f'Modelo: {self.modelo}', f'Motor: {self.motor}', f'Fabricante: {self.fabricante}', sep='\n')

class Motor:
    def __init__(self, motor):
        self.motor = motor

    def __str__(self):
            return self.motor

class Fabricante:
    def __init__(self, fabricante):
        self.fabricante = fabricante

    def __str__(self):
        return self.fabricante

carro1 = Carro('Uno')
motor1 = Motor('Firefly 1.0')
fiat = Fabricante('Fiat')
carro1.informar_motor(motor1)
carro1.informar_fabricante(fiat)
carro1.informacoes()
print('#################################')
carro2 = Carro('EcoSport')
motor2 = Motor('1.5 Dragon')
ford = Fabricante('Ford')
carro2.informar_motor(motor2)
carro2.informar_fabricante(ford)
carro2.informacoes()
