

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
    
    def __pode_retirar(self, valor_pretendido):
        total_disponivel = self.__saldo + self.limite
        return valor_pretendido <= total_disponivel


    def retirar(self, valor = 0.0):
        if(self.__pode_retirar(valor)):
            self.__saldo -= valor
        else:
            print(f"Retirada inválida, o valor {valor} passou o limite possível.")

    def transferir(self, conta_destino, valor = 0.0):
        self.retirar(valor)
        conta_destino.depositar(valor)

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"