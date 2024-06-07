'''
TODO:

Crea una función que convierta temperatura C a F

F = 9/5C + 32
'''

def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

user_input = input('Introduce temp en C: ')
user_input = float(user_input)

print(f'''
La temperatura C: {user_input} equivale a F: {celsius_a_fahrenheit(user_input)}
''')




