class CuentaBancaria:
    def __init__(self, nombre, DNI, saldo):
        self.__nombre = nombre
        self.__DNI = DNI
        self.__saldo = saldo
        self.__HTransacciones = {self.__DNI : []}

    def ingresar(self, saldo):
        self.__saldo += saldo
        saldo = "+" + str(saldo)
        self.agregarTransacciones(self.__DNI, saldo)

    def retirar(self, saldo):
        self.__saldo -= saldo
        saldo = "-" + str(saldo)
        self.agregarTransacciones(self.__DNI, saldo)
    
    def agregarTransacciones(self, DNI, saldo):
        self.__HTransacciones[DNI].append(saldo)

    def verHistorialTransacciones(self, DNI):
        transacciones = self.__HTransacciones[DNI]
        for t in transacciones:
            print(t)
        return "\n".join(transacciones)

            

    def __str__(self):
        return (" Nombre: " + self.nombre + "\n DNI: " + str(self.DNI) + "\n Saldo: " + str(self.saldo))
    
    @property
    def HTransacciones(self):
        return self.__HTransacciones
    
    @property
    def saldo(self):
        return self.__saldo
    @property
    def nombre(self):
        return self.__nombre
    @property
    def DNI(self):
        return self.__DNI

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
        try:
            cuenta = self.__cuentas[DNI]
        except:
            raise Exception("La cuenta no existe")
        else:
            cuenta.ingresar(Dinero)

    def RetirarDineros(self, DNI, Dinero):
        try:
            cuenta = self.__cuentas[DNI]
        except:
            raise Exception("La cuenta no existe")
        else:
            cuenta.retirar(Dinero)
    
    def BuscarCuentas(self, DNI):       
        try:
            cuenta = self.__cuentas[DNI]
        except:
            raise Exception("La cuenta no existe")
        else:
            return cuenta
        
    def verHistorialTransacciones(self, DNI):
        try:
            cuenta = self.__cuentas[DNI]
        except:
            raise Exception("La cuenta no existe")
        else:
            cuenta.verHistorialTransacciones(DNI)

    @property
    def saldo(self):
        return self.__saldo


D1 = Banco("GO")
D1.NuevaCuenta("Sara", 46872582, 0)
D1.IngresarDineros(46872582, 100)
D1.IngresarDineros(46872582, 100)
D1.IngresarDineros(46872582, 100)
print(D1.BuscarCuentas(46872582))
D1.verHistorialTransacciones(46872582)