'''
Objetos en python (POO)
Utilizamos la palabra reservada class para iniciar una nueva clase
y dentro de la clase, colocamos las funciones (métodos)
que llevará el objeto
'''
class Persona():
    def __init__(self, nombre, rol):
        print("se está creando una nueva persona...")
        self.name = nombre
        self.rol = rol

    def saludar(self):
        print(f"Hola soy {self.name}")

persona1 = Persona(nombre='Jose', rol='Instructor')
persona2 = Persona(nombre='Jesica', rol='Estudiante')

persona1.saludar()
print(persona2.name)