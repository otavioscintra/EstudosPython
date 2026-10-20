"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método
"""

from bancos import Banco
from clientes import Cliente
from contas import ContaCorrente, ContaPoupanca


banco = Banco("0001", "Banco Dev")

joao = Cliente("Banco Dev")
joao.nome = "João Silva"
joao.idade = 25

maria = Cliente("Banco Dev")
maria.nome = "Maria Souza"
maria.idade = 30

conta_joao = ContaCorrente("0001", "12345", "Banco Dev", 500)
conta_maria = ContaPoupanca("0001", "67890", "Banco Dev")

joao.adicionar_conta(conta_joao)
maria.adicionar_conta(conta_maria)

banco.adicionar_cliente(joao)
banco.adicionar_cliente(maria)

banco.adicionar_conta(conta_joao)
banco.adicionar_conta(conta_maria)

conta_joao.depositar(1000)
conta_maria.depositar(500)

print("Saldo João:", conta_joao.saldo)
print("Saldo Maria:", conta_maria.saldo)

banco.sacar(joao, conta_joao, 1200) 
banco.sacar(maria, conta_maria, 200)

print("Saldo João após saque:", conta_joao.saldo)
print("Saldo Maria após saque:", conta_maria.saldo)

banco.sacar(joao, conta_maria, 100)