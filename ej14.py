class CuentaBancaria:
    def __init__(self, nombre, DNI, saldo):
        self.__nombre = nombre
        self.__DNI = DNI
        self.__saldo = saldo

    def ingresar(self, saldo):
        self.__saldo += saldo

    def retirar(self, saldo):
        self.__saldo -= saldo

    @property
    def saldo(self):
        return self.__saldo

class Banco:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__cuentas = {}
    
    def NuevaCuenta(self, nombre, DNI, saldo):
        if saldo == "":
            saldo = 0
        nueva_cuenta = CuentaBancaria(nombre, DNI, saldo)
        self.__cuentas[DNI] = nueva_cuenta
    
    def IngresarDineros(self, DNI, Dinero):
        self.__cuentas[DNI].ingresar(Dinero)

    def RetirarDineros(self, DNI, Dinero):
        self.__cuentas[DNI].retirar(Dinero)
        
    @property
    def saldo(self):
        return self.__saldo

D1 = Banco("GO")
D1.NuevaCuenta("Sara", 46872582, 0)
D1.IngresarDineros(46872582, 100)