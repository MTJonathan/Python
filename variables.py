import random
integer = 32 #Variable de tipo entero
float_var = 3.2 #Variable de tipo flotante
string = 'Esto es un texto' #Esto es una cadena de texto
numero_ramdom = random.randint(0,10)
boolean = True #Variable de tipo booleano
numeroComplejo = 5 + 2j #Variable de tipo complejo
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3] #Esto es una lista
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) #Esto es una tupla no es modificable
set_var = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3} #Esto es un set no permite valores duplicados
frozenset_var = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) #Esto es un frozenset no es modificable
rango = range(1,10) #Esto es un rango
diccionario = {"Nombre": "Jonathan", "Apellido": "Matias", "Edad": 18, "Sexo": "Masculino"}

print ("")
print ("Esto son algunas Tipos de Datos en python : ")
print ("")
print(f"Numero entero: {integer}")
print(f"Numero decimal: {float_var}")
print(f"Cadena de texto: {string}")  
print(f"Numero aleatorio: {numero_ramdom}")
print(f"Booleana: {boolean}")
print(f"Numero Complejo: {numeroComplejo}")
print(f"Array: {array}")
print(f"Tupla: {tupla}")
print(f"Set: {set_var}")
print(f"Frozenset: {frozenset_var}")
print(f"Rango: {rango}")
print(f"Direccion: {diccionario}")