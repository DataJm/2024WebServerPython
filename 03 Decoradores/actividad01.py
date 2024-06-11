'''
TODO:
Escribe una función que tome un número variable
de argumentos no nombrados y que regrese
la multiplicación de todos los valores
'''

def multiplicar(*args):
    resultado = 1

    for x in args:
        # resultado = resultado * x
        resultado *= x

    return resultado

print(multiplicar(5,2,3))