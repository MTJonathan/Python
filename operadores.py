a = 32
b = 23

'''Suma'''
print("Operadores Matematicos : ")
suma = a + b
print (f'Suma : {suma}')

'''Resta'''
resta = a - b
print (f'Resta : {resta}')

'''Multiplicacion'''
multiplicacion = a * b
print (f'Multiplicacion : {multiplicacion}')

'''Division'''
division = a / b
print (f'Division : {division}')

'''Exponenciacion'''
exponete = a ** b
print (f'Exponenciacion : {exponete}')

'''Modulo'''
modulo = a % b
print (f'Modulo : {modulo}')

'''Operadoredes de asignacion'''
print("")
print("Operadores de asignacion : ")
X = 10
X += 5 #Suma el valor anterio
print(X)
X -= 3 #Resta el valor anterio
print(X)
X *= 10 #Multiplica el valor anterio
print(X)
X /= 2 #Divide el valor anterio
print(X)
X **= 3 #Exponenciacion
print(X)
X %= 5 #Modulo
print(X)

'''Operadores de comparacion'''
print("")
print("Operadores de comparacion : ")
number = 32
number2 = 23
igualdad = number == number2
print(igualdad)
distintos = number != number2
print(distintos)
mayor = number > number2
print(mayor)
menor = number < number2
print(menor)
mayor_igual = number >= number2
print(mayor_igual)
menor_igual = number <= number2
print(menor_igual)

'''Operadores Logicos'''
print("")
print("Operadores Logicos : ")
edad = 17
tramite = edad >= 18 and edad <= 32
print(tramite)
semaforo = "Rojo"
cruzar = semaforo == "Verde" or semaforo == "Amarillo"
print(cruzar)
mentira = False
print(not mentira)

'''Operadores de Identidad'''
print("")
print("Operadores de Identidad : ")
nombre = "Jonathan"
profesor = "Jonathan"
sonElMismo = nombre is profesor
print(sonElMismo)
sonElMismo = nombre is not profesor
print(sonElMismo)

'''Operadores de pertencia'''
print("")
print("Operadores de pertencia : ")
palabra = "Hola Mundo"
txt = "Mundo"
pertenece = txt in palabra
print(pertenece)
noPertenece = txt not in palabra
print(noPertenece)