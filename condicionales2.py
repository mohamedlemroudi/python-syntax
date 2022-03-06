print("Verificación de acceso")

nota_alumno = int(input("Introduice tu nota, por favor: "))

if nota_alumno < 5:
    print("Insuficiente")
elif nota_alumno < 6:
    print("Suficiente")
elif nota_alumno < 7:
    print("Bien")
elif nota_alumno < 9:
    print("Notable")
else:
    print("Sobresaliente")
