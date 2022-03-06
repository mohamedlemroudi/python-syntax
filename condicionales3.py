salario_presidente = int(input("Introduce salario presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduce salario director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area = int(input("Introduce salario Jefe Área: "))
print("Salario Jefe Área: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduce salario Administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))


if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")