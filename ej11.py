class Ventilador:
    def __init__(self, Marca, Modelo):
        self.__Marca = Marca
        self.__Modelo = Modelo
        self.__Velocidad = 0
        self.__conectado = False
    def Subir_velocidad(self):
        if (self.__conectado):
            if self.__Velocidad < 4:
                self.__Velocidad += 1
                return "La velocidad del " + self.__Marca + " subio al nivel: " + str(self.__Velocidad)
            else:
                raise NameError("No hay niveles arriba de 4")
        else:
            raise "Error: No esta conectado"
    
    def Bajar_velocidad(self):
        if (self.__conectado):
            if self.__Velocidad > 0:
                self.__Velocidad -= 1
                return "La velocidad del " + self.__Marca + " bajo al nivel: " + str(self.__Velocidad)
            if self.__Velocidad == 0:
                return "La velocidad del " + self.__Marca + " no puede bajar del nivel 0"
        else:
            raise "Error: No esta conectado"
    
    def conectar(self):
        if (self.__conectado == False):
            self.__conectado = True
            return "Se ha conectado el ventilador " + self.__Marca
    
    def desconectar(self):
        if (self.__conectado):
            self.__conectado = False
            return "Se ha desconectado el ventilador " + self.__Marca

Ventilador1 = Ventilador("DP", "Grande")
Ventilador2 = Ventilador("Liliana Orbital", "3 Palas")
print(Ventilador1.conectar())
print(Ventilador1.Subir_velocidad())
print(Ventilador1.Subir_velocidad())
print(Ventilador1.desconectar())
print(Ventilador1.Subir_velocidad())
