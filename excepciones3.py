def divide():

    try:

        op1 = (float(input("Introduce el primer número: ")))

        op2 = (float(input("Introduce el segundo número: ")))    

        print("La división es: " + str(op1/op2))
    
    except ValueError:
        print("El valor introducido es erróneo")

    except ZeroDivisionError:
        print("NO se puede dividir por 0!")

    finally:
        print("Programa finalizado.")


divide()