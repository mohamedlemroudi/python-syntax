from io import open

# --------------------------------------------- Escritura

#archivo_texto = open("archivo.txt","w")

#frase="Estupendo día para estudiar Python \n el viernes"

#archivo_texto.write(frase)

#archivo_texto.close()

# --------------------------------------------- Lectura

#archivo_texto = open("archivo.txt","r")

#texto = archivo_texto.read()

#archivo_texto.close()

#print(texto)

# --------------------------------------------- Lectura lineal (lista)

# archivo_texto = open("archivo.txt","r")

# lineas_texto = archivo_texto.readlines()

# archivo_texto.close()

# print(lineas_texto)

# print(lineas_texto[1])

# --------------------------------------------- Añadir

# archivo_texto = open("archivo.txt","a") # a -> append

# archivo_texto.write("\n siempre es una buena ocasión para estudiar Python")

# archivo_texto.close()


# --------------------------------------------- Seek

archivo_texto = open("archivo.txt","r+") # lectura y escritura

#print(archivo_texto.read())

#archivo_texto.seek(11) # posicióna el puntero

#print(archivo_texto.read(11))

#print(archivo_texto.read())

#archivo_texto.seek(len(archivo_texto.readline()))

#print(archivo_texto.read())

#archivo_texto.write("Comienzo del texto")

#print(archivo_texto.readlines())

lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta línea ha sido incluida des del exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()