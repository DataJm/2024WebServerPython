from flask import Flask
from config import SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    '''
    Agregar las rutas a app, registrar esos blueprints
    '''
    from app.auth.routes import auth
    from app.main.routes import main

    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
