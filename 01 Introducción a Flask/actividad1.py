# TODO
# Crear una lista y una tupla.
# En la lista pondran nombres de alumnos
# En la tupla van a poner edades de alumnos
# Las edades estan entre 16 y 19 años
# Has un ciclo para imprimir en pantalla a cada persona con su edad
# En caso de que la persona sea mayor a 18 años, imprimir un mensaje

nombres = ['jose','alejandra','gilbero']
edades  = (17,18,19)

# for i in range(3):
for i in range(len(nombres)):
    # print(nombres[i], edades[i])
    print(f'La persona {nombres[i]}, tiene {edades[i]} años de edad ')
    if edades[i] >= 18 :
        print('Mayor de edad')


