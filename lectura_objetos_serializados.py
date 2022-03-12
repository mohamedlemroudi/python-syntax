import pickle

from serializar_objetos import Vehiculo

ficheroAperatura = open("losCoches", "rb")

misCoches = pickle.load(ficheroAperatura)

ficheroAperatura.close()

for c in misCoches:
    print(c.estado())