import random

def juegoAdivina():
    numero = random.randint(1, 100)
    intentos = 0
    numeroIntentos = 10
    numeroIngresado = int(input("Ingresa un numero entre 1 y 100: "))
    print(f'Numero de intentos: {numeroIntentos - intentos}')
    print("")
    
    while (numeroIngresado != numero and intentos != numeroIntentos):
        if (numeroIngresado > numero):
            print("El numero es menor")
            print("")
            intentos += 1
        else:
            print("El numero es mayor")
            print("")
            intentos += 1
        print(f'Numero de intentos: {numeroIntentos - intentos}')
        if (intentos != numeroIntentos):
             numeroIngresado = int(input("Intenta de nuevo: "))
        
        print("")
        
    print("")
    if (intentos == numeroIntentos):
        print("Perdiste")
    else:
        print("Ganaste")
    
juegoAdivina()