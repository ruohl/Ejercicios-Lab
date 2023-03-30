class Ventilador:
    def __init__(self, Marca, Modelo):
        self.__Marca = Marca
        self.__Modelo = Modelo
        self.__Velocidad = 0
    
    def Subir_velocidad(self):
        if self.__Velocidad < 4:
            self.__Velocidad += 1
            return "La velocidad del " + self.__Marca + " subio al nivel: " + str(self.__Velocidad)
        else:
            raise NameError("No hay niveles arriba de 4")
    
    def Bajar_velocidad(self):
        if self.__Velocidad > 0:
            self.__Velocidad -= 1
            return "La velocidad del " + self.__Marca + " bajo al nivel: " + str(self.__Velocidad)
        if self.__Velocidad == 0:
            return "La velocidad del " + self.__Marca + " no puede bajar del nivel 0"
        
Ventilador1 = Ventilador("DP", "Grande")
Ventilador2 = Ventilador("Liliana Orbital", "3 Palas")

print(Ventilador1.Subir_velocidad())
print(Ventilador1.Subir_velocidad())
print(Ventilador1.Subir_velocidad())
print(Ventilador1.Subir_velocidad())
print(Ventilador1.Subir_velocidad())
print(Ventilador2.Subir_velocidad())
print(Ventilador2.Subir_velocidad())
print(Ventilador2.Bajar_velocidad())