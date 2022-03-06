import math

print("Programa de cálcula de raiz cuadrado")
numero = int(input("Introduce un numero por favor: "))

intentos = 0

while numero < 0:
    print("No se puede hallar la raíz de un número negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos. El programa ha finalizado.")
        break
    
    numero = int(input("Introduce un numero por favor: "))
    if numero < 0:
        intentos += 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))