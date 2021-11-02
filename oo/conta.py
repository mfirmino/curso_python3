

class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Contruindo um objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O saldo do titular {self.__titular} é: {self.__saldo}")

    def depositar(self, valor = 0.0):
        self.__saldo += valor
    
    def retirar(self, valor = 0.0):
        self.__saldo -= valor

    def transferir(self, conta_destino, valor = 0.0):
        self.retirar(valor)
        conta_destino.depositar(valor)
