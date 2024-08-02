edad = int(input("Ingresa tu edad: "))

if (edad >= 18 and edad <= 60):
    print("Puedes entrear al boliche")
elif (edad < 18):
    print("No puedes entrar al boliche por se menor de edad")
else:
    print("No puedes entrar al boliche por sobre pasar el limite de edad")
    
'''Shorthands'''
print("")
print("Shorthands")
a = 32
b = 23
print("Shorthands de una condicional")
if a>b : print ("a es mayor que b") #Del if solo
print("Shorthands de dos condicionales")
print("a es mayor que b") if a>b else print("b es mayor que a")