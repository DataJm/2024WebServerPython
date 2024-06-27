from flask import Flask
from config import SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    '''
    Agregar las rutas a app, registrar esos blueprints
    '''


    return app
