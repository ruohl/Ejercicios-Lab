class Automovil:
    def __init__(self, marca, modelo, año, color):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__color = color
        self.__velocidad = 0

    @property
    def velocidad(self):
        return self.__velocidad
    
    def acelerar(self):
        if self.__velocidad < 220:
            self.__velocidad += 10
            return "Acelerando 10 km/h \n" + "Velocidad actual: " + str(self.__velocidad)
        
    def frenar(self):
        if self.__velocidad > 10:
            self.__velocidad -= 10
            return "Desacelerando 10 km/h \n" + "Velocidad actual: " + str(self.__velocidad)
        if self.__velocidad == 10:
            self.__velocidad -= 10
            return "Frenando 10 km/h \n" + "Velocidad actual: " + str(self.__velocidad)
        else:
            raise NameError("No se puede frenar si no te estas moviendo")

           
        
auto1 = Automovil("Ford", "F-150", "2016", "Azul")
auto2 = Automovil("Chevrolet", "ONIX", "2020", "Rojo")

print(auto1.acelerar())