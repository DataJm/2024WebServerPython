'''
TODO:
Crear un decorador llamado 'medir_tiempo'
que mide y muestra el tiempo que una función
tarda en ejecutarse.
'''
import time

def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Algo antes de ejecutar la funcion objetivo")
        resultado = func(*args, **kwargs)
        print("ALgo después de ejecutar la función objetivo")
        return resultado
    return wrapper

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f'''
        Probando la función: {func.__name__}
        Inicio: {inicio}
        Fin: {fin}
        Tiempo de ejecución: {fin-inicio} segundos
        ''')
        return resultado
    return wrapper

@mi_decorador
@medir_tiempo
def sumar_hasta_n(n):
    resultado = 0
    for x in range(n):
        resultado += x

    return resultado
@medir_tiempo
def sumar(a,b):
    resultado = a +b 
    return resultado

super_calculo = sumar_hasta_n(500000)
calculo = sumar(5,10)

