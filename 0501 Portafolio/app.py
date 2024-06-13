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

app = Flask(__name__)
app.register_blueprint(router)

if __name__ == '__main__':
    app.run(debug=True)

