print("Programa de evaluación de notas de alumnos")

nota_alumno = float(input("Introduce la nota del alumno: "))

def evaluacion(nota):
    valoracion = "aprobado"

    if nota < 5:
        valoracion = "suspenso"

    return valoracion


print(evaluacion(nota_alumno))