nombre = input("Ingresa tu nombre: ")
numero = input("Numero: ")
numero2 = input("Numero2: ")
numero3 = input("Numero3: ")
print(f"Hola mundo {nombre}")# Esto es un comentario en python

if(numero > numero2 and numero > numero3):
    print(f"{numero} es mayor que {numero2} y {numero3}")
elif(numero2 > numero3 and numero2 > numero):
    print(f"{numero2} es mayor que {numero} y {numero3}")
else:
    print(f"{numero3} es mayor que {numero} y {numero2}")