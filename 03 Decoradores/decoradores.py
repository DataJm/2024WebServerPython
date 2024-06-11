'''
Un decorador es una función que acepta una función
como argumento y devuelve una nueva función.

Es decir "extiende" las capacidades de una función.
'''
def mi_decorador(func):
    '''
    La función decoradora, puede hacer cosas aqui
    "cosas intermedias"
    Debe regresar una función...
    '''
    def nueva_funcion():
        print("Algo antes de ejecutar la funcion objetivo")
        func()
        print("ALgo después de ejecutar la función objetivo")

    return nueva_funcion

@mi_decorador
def funcion_a_decorar():
    print('Ejecutando la funcion_a_decorar')

funcion_a_decorar()