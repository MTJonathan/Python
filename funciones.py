def funcion(profesor, curso):
    print (f"El profesor {profesor} dicta el curso de {curso}")
    
funcion("Jonathan", "Python")
'''Argumentos arbitrarios (multiples argumentos) '''
def calculadora(*numeros):
    suma = 1
    for i in numeros:
        print(f'suma {suma} + {i} = {suma + i}')
        suma += 1

calculadora(1,2,3,4,5)

'''Retornar '''
def suma(num1, num2):
    return num1 + num2

print(suma(1,2))