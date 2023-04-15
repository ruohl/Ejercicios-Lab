class Incrementador:
    def __init__(self, tope):
        self.__tope = tope
        self.__contador = 0

    @property
    def valor_actual(self):
        return self.__contador
    
    def autoincrementar(self):
        while (self.__contador + 1) <= self.__tope:
            self.__contador += 1
            

inc = Incrementador(10)
print(inc.valor_actual)
inc.autoincrementar()
print(inc.valor_actual)