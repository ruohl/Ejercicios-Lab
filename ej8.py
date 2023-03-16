class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
        
    def depositar(self):
        self.__saldo = int(self.__saldo)
        self.__saldo += Cantidad
        self.__saldo = str(self.__saldo)
        return self.__titular + ", Ahora tu saldo nuevo es: " + self.__saldo

    def retirar(self):
        self.__saldo = int(self.__saldo)
        self.__saldo -= Cantidad
        self.__saldo = str(self.__saldo)
        return self.__titular + ", Ahora tu saldo nuevo es: " + self.__saldo

Cantidad = 1000

c1 = CuentaBancaria("Roberto", "5000")

print(c1.depositar())
print(c1.depositar())
print(c1.retirar())