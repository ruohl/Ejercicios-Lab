class Cancion:
    def __init__(self, titulo, artista, letra):
        self.__titulo = titulo
        self.__artista = artista
        self.__letra = letra

    def reproducir(self):
        return "Estas escuchando " + self.__titulo + "\n Artista: " + self.__artista + "\n LETRA: \n" + self.__letra

C1 = Cancion("Gorda puerca", "Asspera", "En la esquina de un barrio, escuchamos la radio Mientras pinta un asado, metal y el escabio Nos cagamos de risa, el olor no es a pizza Pinta el faso, el descanso y miramos la esquina")
print(C1.reproducir())