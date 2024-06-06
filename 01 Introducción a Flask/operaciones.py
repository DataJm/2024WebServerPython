# Operadores lógicos
a = True
b = False

# and
# Ambas condiciones (izquiera y derecha) son verdaderas
x = 5

print(1>0 and x<2) # False

# or
# Regresa 'True' si una de las dos condiciones es 'True'

print(1>0 or x<2) # True

# not
print(not a) # False


# If
# if condicion:
#   codigo

edad = 17
credencial = True

if edad>=18 and credencial:
    print('Puede votar')
    print('Puede votar')
    print('Puede votar')

print('codigo fuera del if')


edad = 19
credencial = False
permiso_especial = False

if edad>=18:
    print('Edad suficiente')
    if credencial:
        print('Tiene edad y tiene credencial, puede votar')
    else:
        print('Te falta credencial')
elif permiso_especial:
    print('Permiso especial')
else:
    print('Edad no suficiente')


# Ciclos for
# for iterador in iterable:
#   codigo que repetiremos

alumnos = ['jose','rogelio','antonio']

for x in alumnos:
    print(x)

print('fin del ciclo')

for a in 'enciclopedia':
    print(a)
    if a=='c':
        break

# range
# Construye una serie numerica de 0 al valor dado
# NOTA: El rango es excluyente por la derecha
for i in range(5):
    print('Mensaje')

for i in range(5):
    print(i)

for i in range(3):
    print(alumnos[i])