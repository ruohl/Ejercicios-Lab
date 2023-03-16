class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def saludar(self):
        return "Hola mi nombre es " + self.__nombre + " y tengo " + self.__edad + " " + "años."
        
    @property
    def edad(self):
        return self.__edad

    def cumplir_años(self):
        self.__edad = int(self.__edad)
        self.__edad += 1
        self.__edad = str(self.__edad)
        return "Cumplí " + self.__edad

p1 = Persona("Lala", "19")
p2 = Persona("Agustin", "17")
print(p1.saludar())
print(p2.cumplir_años())