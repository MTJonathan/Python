'''While'''
print("While")
array = []
contador = 0
while(contador < 10):
    array.append(contador)
    contador = contador + 1
print(array)

'''For'''
print("")
print("For")
array = []
for i in range(10):
    array.append(i)
print(array)

'''For con listas'''
print("")
print("For con listas")
array = ["Node" , "React" , "Vue" , "Angular"]
x = 1
for i in array:
    print(f'{x}. {i}')
    x+= 1
    
'''For con diccionarios'''
print("")
print("For con diccionarios")
diccionario = {"Nombre": "Jonathan", "Apellido": "Matias", "Edad": 18, "Sexo": "Masculino"}
for i in diccionario:
    print(diccionario[i])