class Persona():
    def __init__ (self, nombre, edad, Lugar_residencia):
        self.nombre = nombre

        self.edad = edad

        self.lugar_residencia = Lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugar_residencia)


class Empleado(Persona):

    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        
        self.salario = salario

        self.antigüedad = antigüedad

    def descripcion(self):
        super().descripcion()

        print(" Salario: ", self.salario, "Antigüedad: " ,self.antigüedad)


Antonio = Empleado(1500, 15, "Antonio", 56, "España")

Antonio.descripcion()

print(isinstance(Antonio, Persona))