class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    def arrencar(self): # self -> objeto pertenciente a la clase (this)
        self.enmarcha = True
    
    def estado(self):
        if (self.enmarcha):
            return "El coche está en marcha"
        
        else:
            return "El coche está parado"


miCoche = Coche() # instanciar una clase

print("El largo del chasis es: ", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas," ruedas.")
miCoche.arrencar()
print(miCoche.estado())