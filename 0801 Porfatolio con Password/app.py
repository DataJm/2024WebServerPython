'''
TODO:

- Guardar los comentarios en BD
- Crear una API para servir los comentarios en un JSON

'''

from flask import Flask, render_template
from modules.routes import router

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Registra el blueprint 'router' desde el módulo 'modules.routes'
app.register_blueprint(router)

# Establece una clave secreta para la aplicación Flask, utilizada para la gestión de sesiones y cookies seguras
app.secret_key = 'watever'


'''
Podemos controlar el tiempo de vida de las sesiones en flask con el siguiente código
El tiempo de vida default es 31 días:
https://flask.palletsprojects.com/en/3.0.x/api/#flask.session
'''
from datetime import timedelta
# Los time delta pueden configurarse en segundos, minutos, horas, dias y semanas
# app.permanent_session_lifetime = timedelta(seconds=5)
app.permanent_session_lifetime = timedelta(hours=2)

# puedes hacer la sesion permamente con 
# app.permanent_session_lifetime = True
# Si lo ponemos en false, la sesion se cierra cuando se cierra el navegador
# app.permanent_session_lifetime = False

# Ejecuta la aplicación en modo de depuración si este archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)