class Coche():
    
    def __init__(self):

        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrencar(self, arrancamos): # self -> objeto pertenciente a la clase (this)
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            return "El coche está en marcha"

        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas, Un acho de ", self.__anchoChasis, " y un largo de ",
        self.__largoChasis)

miCoche = Coche() # instanciar una clase

print(miCoche.arrencar(True))

miCoche.estado()


print("- ----- A continuación creamos el segundo objecto ------")

miCoche2 = Coche()

print(miCoche2.arrencar(False))

# miCoche2.__ruedas = 2

miCoche2.estado()
