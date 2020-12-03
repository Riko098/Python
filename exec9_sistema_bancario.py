'''

EXERCICIO: Crie um software de gerenciamento bancario
esse Software podera ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar , depositar e consultar saldo
'''

from cliente import Cliente
from conta import Conta


cliente1 = Cliente('erico', '074.548.455.20', '22')

print(cliente1)

conta_do_erico = Conta(cliente1, 10.50, 5000)

print(conta_do_erico.cliente.nome, conta_do_erico.consultasaldo())

conta_do_erico.depositar(1500)
print(conta_do_erico.cliente.nome, conta_do_erico.consultasaldo())
conta_do_erico.sacar(500)
conta_do_erico.sacar(4500)
print(conta_do_erico.consultasaldo())