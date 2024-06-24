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

# Ejecuta la aplicación en modo de depuración si este archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)