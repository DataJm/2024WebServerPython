'''
TODO:

Crea un sitio web estático donde puedas mostrar tu curriculum, tus proyectos, tus habilidades
y una sección de "comentarios".

- Pagina de inicio con una breve presentación
- Pagina de proyectos con detalles y enlaces
- Pagina "about me" con tu experiencia y habilidades
- Página de dejar comentario

Tecnologías: Flask, HTML, Bootstrap5

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