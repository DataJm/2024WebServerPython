# Introducción a Python

# Variables y asignación

years = 5 
message = "hola"
peso = 89.5
experto = True

print(message)

# Estructuras de datos
# Lista, Tupla, Set, Diccionario

# Lista
# Ordenada, Indice, Mutable
# Puede tener cualquier tipo de objeto (y combinación)
mi_lista = ["jose","eloy","rogelio","lourdes"]

# Agregar un nuevo elemento
# método: append()
mi_lista.append("jesus")

print(mi_lista)

# Acceder a un ítem de la lista
print(mi_lista[0])

# Re asignación
mi_lista[0] = "999"

print(mi_lista)

# Ordenar
# método: sort()
mi_lista.sort()
print(mi_lista)

# Tupla
# Colección de items Ordenada, Indice, INMUTABLE
mi_tupla = ("claudia","dilan","alfredo")

# ESTO genera error (no existe el método append)
# mi_tupla.append("a")

# Esto genera error, no podemos reasignar items de una tupla
#mi_tupla[1] = False

print(mi_tupla)

# Set
# (conjuntos)
# Colección de items, SIN ORDEN, SIN INDICE, MUTABLES, no permite valores duplicados
mi_set = {"gilberto","jesica","antonio"}

print(mi_set)
print("antonio" in mi_set)

# Método : add()
mi_set.add("xyz")

print(mi_set)

# Diccionario
# Son colecciones desordenadas de pares llave-valor (clave-valor)
mi_diccionario = {"nombre":"Jose","rol":"Instructor","Experiencia":5}

print(mi_diccionario["rol"])

mi_diccionario["no_existe"] = 999

print(mi_diccionario)