mensaje = '''
Esto
es
un mensaje
de 
multiples lineas

:=)
'''

print(mensaje)

'''
Funciones en python

Utilizamos la palabra reservada "def" para crear
nuestras propias funciones.
'''

def sumar(a,b=0):
    resultado = a + b
    return resultado

print(sumar(5,10))