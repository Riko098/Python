class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0-limite

    def sacar(self, valorsaque):#METODO 1
        if self.saldo-valorsaque<self.limite:
            print("saldo insuficiente")
        else:
            self.saldo -= valorsaque
            print("Foi sacado:", valorsaque)

    def depositar(self, valordeposito):#METODO 2
        if valordeposito >0:
            self.saldo +=valordeposito
            print('Foi depositado:', valordeposito)
        else:
            print('erro no deposito')

    def consultasaldo(self):
         return self.saldo

