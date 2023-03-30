class MascotaVirtual:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__humor = "Bien"
        self.__hambre = 0
        self.__aburrimiento = 0

    def comer(self):
        if (self.__hambre < 0):
            self.__hambre = 0
        else:
            self.__hambre -= 4
            self.pasar_tiempo()
        

    def jugar(self):
        if (self.__aburrimiento < 0):
            self.__aburrimiento = 0
        else:
            self.__aburrimiento -= 4
            self.pasar_tiempo()
        

        self.pasar_tiempo()

    def pasar_tiempo(self):
        self.__hambre += 1
        self.__aburrimiento += 1

    def hablar(self):
        self.pasar_tiempo()
        return "Hola me llamo " + self.__nombre + " y estoy " + self.humor

    @property
    def humor(self):
        if (0 <= (self.__aburrimiento + self.__hambre) < 10):
            return "Bien"
        elif (10 <= (self.__aburrimiento + self.__hambre) <= 20):
            return "Ok"
        elif ((self.__aburrimiento + self.__hambre) > 20):
            return "Enojado"

    @property
    def hambre(self):
        return self.__hambre

    @property
    def aburrimiento(self):
        return self.__aburrimiento

mascota = MascotaVirtual("Roberto")
for i in range(5):
    mascota.pasar_tiempo()
print(mascota.hablar())
for i in range(10):
    mascota.comer()
    mascota.jugar()
print(mascota.hablar())
for i in range(10):
    mascota.pasar_tiempo()
print(mascota.hablar())