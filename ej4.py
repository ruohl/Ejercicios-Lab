class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def nombre(self):
        return self.__nombre

    def saludar(self, persona_saludada):
        persona_saludada.__nombre = "LALA"
        return "Hola " + persona_saludada.nombre

    def presentarse(self):
        return "Mi nombre es " + self.__nombre + " " + self.__apellido


p1 = Persona("Pepe", "Landrún")
p2 = Persona("Armando", "Pleitos")
p3 = Persona("Pocho", "Clo")

print(p1.presentarse())
print(p1.saludar(p2))
print(p2.presentarse())