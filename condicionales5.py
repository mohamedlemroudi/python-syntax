print("Asignaturas optativas Año 2022")
print("Asignaturas optativas: Informática gràfica - Pruebas de software - Usabilidad y accesibilidad")
opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower()

if asignatura in ("infomática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura escogida no está contemplada")