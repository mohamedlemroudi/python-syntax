midiccionario = {
    "Alemania":"Berlín",
    "Francia":"París",
    "Reino Unido":"Londres",
    "España":"Madrid"
}

midiccionario["Italia"] = "Lisboa"

#print(midiccionario)

midiccionario["Italia"] = "Roma"

#print(midiccionario)

del midiccionario["Reino Unido"]

#print(midiccionario)

mitupla = ("España", "Francia", "Reino Unido", "Alemania")

midiccionario2 = {
    mitupla[0]: "Madrid",
    mitupla[1]: "París",
    mitupla[2]: "Londres",
    mitupla[3]: "Berlín"
}

#print(midiccionario2)

midiccionario3 = {
    23:"Jordan",
    "Nombre":"Michael",
    "Equipo":"Chicago",
    "anillos": {
        "temporades": (1991, 1992, 1993, 1996, 1997, 1998)
    } 
}

#print(midiccionario3["anillos"]["temporades"])

print(midiccionario3.keys())

print(midiccionario3.values())

print(len(midiccionario3))