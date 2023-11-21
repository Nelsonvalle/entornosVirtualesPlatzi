import random

# logica del juego
vidasUsuario = 3
vidasPC = 3
while vidasUsuario >0 and vidasPC >0:
    #Solicitar la entrada del usuario
    opcion= input("Favor ingrese su eleccion: Piedra, Papel, tijera: \n").lower()

    #validacion de entrada:
    while opcion != "piedra" and opcion != "papel" and opcion != "tijera":
        print("Error! eleccion invalida. Intentelo de nuevo")
        opcion= input("Favor ingrese su eleccion: Piedra, Papel, tijera: \n").lower()
    
    #opcion de la computadora Piedra, Papel, tijera
    opcionPC = random.choice(['piedra','papel','tijera'])
    
    if opcion == 'piedra' and opcionPC== 'tijera':
        print(f"Gana el usuario, por que saco {opcion} y PC saco {opcionPC}")
        vidasPC -= 1
        print(f"vidas usuario: {vidasUsuario} y vidas PC: {vidasPC}")
    elif opcion == 'papel' and opcionPC== 'piedra':
        print(f"Gana el usuario, por que saco {opcion} y PC saco {opcionPC}")
        vidasPC -= 1
        print(f"vidas usuario: {vidasUsuario} y vidas PC: {vidasPC}")
    elif opcion == 'tijera' and opcionPC== 'papel':
        print(f"Gana el usuario, por que saco {opcion} y PC saco {opcionPC}")
        vidasPC -= 1
        print(f"vidas usuario: {vidasUsuario} y vidas PC: {vidasPC}")
    elif opcion == opcionPC:
        print(f"Empate! No hay ganador se repite la jugada. Usuario saco {opcion} y PC saco {opcionPC}")
        print(f"vidas usuario: {vidasUsuario} y vidas PC: {vidasPC}")
    else:
        print(f"Gana el PC, por que saco {opcionPC} y usuario saco  {opcion}")
        vidasUsuario -= 1
        print(f"vidas usuario: {vidasUsuario} y vidas PC: {vidasPC}")
        
    