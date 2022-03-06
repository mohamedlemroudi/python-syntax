def generaPares(limite):
    num = 1

    while num < limite:
        yield num * 2
        num += 1
    
devuelvePares = generaPares(10) # entre llamada y llamada entre un estado de suspensión 

print(next(devuelvePares))

print("Aquí podria ir más código....")

print(next(devuelvePares))

print("Aquí podria ir más código....")

print(next(devuelvePares))