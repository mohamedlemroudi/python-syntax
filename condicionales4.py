print("Programa de becas Año 2022")

distancia_escula = int(input("Introduce la distancia a la escula en km: "))
print(distancia_escula)

numero_hermanos = int(input("Introduce el nº de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar = int(input("Introduce salario anual bruto: "))
print(salario_familiar)

if distancia_escula > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    print("Tienes derecho de beca")
else:
    print("No tienes derecho a beca")
