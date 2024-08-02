true = True
false = False
print(true, false)

print('')
'''Variables que retornan true'''
string = bool("Esto es un texto")
number = bool(2)
lista = bool([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
dicionario = bool({"Nombre": "Jonathan", "Apellido": "Matias", "Edad": 18, "Sexo": "Masculino"})
print(f"{string} \n{number} \n{lista} \n{dicionario}")

print("")
'''Variables que retornan false'''
string = bool("")
number = bool(0)
lista = bool([])
dicionario = bool({})
print(f"{string} \n{number} \n{lista} \n{dicionario}")