class Rectangulo:
    def __init__(self, Nombre, Altura, Base):
        self.__Nombre = Nombre
        self.__Altura = Altura
        self.__Base = Base
    
    @property
    def altura(self):
        return self.__Altura
    
    @property
    def base(self):
        return self.__Base
        
    def calcular_area(self):
        self.__Altura = int(self.__Altura)
        self.__Base = int(self.__Base)
        Total = self.__Altura * self.__Base
        Total = str(Total)
        self.__Altura = str(self.__Altura)
        self.__Base = str(self.__Base)
        return "Me llamo " + self.__Nombre + ", tengo de Base " + self.__Base + " y " + self.__Altura + " de altura. \n" + "Mi area es " + Total

R1 = Rectangulo("Pedro", "20", "50")
print(R1.calcular_area())