'''
Args

A las funciones de python podemos pasarles argumentos de tamaño "n"
llamagos *args

Argumentos no nombrados
'''

def sumar(a,b):
    resultado = a + b
    return resultado


def sumar_numeros(*args):
    resultado = 0
    for numero in args:
        # resultado = resultado + numero
        resultado += numero

    return resultado

print(sumar_numeros(5,10,100))

'''
Kwargs

Key word arguments
Argumentos nombrados

A las funciones de python les podemos pasar cualquier número de argumentos
que tengan nombre y para usamos **kwargs

'''

def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f'Clase: {clave} Valor : {valor}')


imprimir_info(nombre='jose', edad=37, profesion='Python')





