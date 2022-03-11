# ----------------- Validar edad -----------------
# edad = input("Introduce la edad: ")

# while(edad.isdigit() == False):
#     print("Por favor, introduce un valor numérico")

#     edad = input("Introduce la edad: ")

# if(int(edad)<18):
#     print("No puede pasar")
# else:
#     print("puede passar")


# ----------------- Programa @ -----------------
email = input("Introduce un correo electronico: ")

emailVarificado = True

arroba = email.count('@')

if (arroba != 1 or email.find('@') == 0 or email.find('@') == -1):
        print("El correo no es correcto")
else:
        print("El correo es correcto")
