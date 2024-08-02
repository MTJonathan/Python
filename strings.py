cadenaTextos = "esto es una cadena de texto"

'''Convertir en mayúsculas y minúsculas'''
cadenaTextos = cadenaTextos.upper()
print(cadenaTextos)
cadenaTextos = cadenaTextos.lower()
print(cadenaTextos)
cadenaTextos = cadenaTextos.capitalize()
print(cadenaTextos)

'''Array de caracteres'''
caracter = cadenaTextos[3] # caracter de la posicion 3
print(caracter) 

'''Cortar una parte de la cadena'''
palabra = cadenaTextos[0:4] # para mostrar una parte de la cadena
print(palabra)

'''Longitud de una cadena'''
longitud = len(cadenaTextos)
print(longitud)

'''Verificar si una palabra existe en una cadena'''
existe = "texto" in cadenaTextos
print(existe) 
