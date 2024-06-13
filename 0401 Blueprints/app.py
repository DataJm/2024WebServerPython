from flask import Flask

# Importar el modulo (la ruta)
from modulos.rutas import admin_bp

app = Flask(__name__)

app.register_blueprint(admin_bp)

@app.route('/')
def inicio():
    return 'Welcome page!'

if __name__ == '__main__':
    app.run(debug=True)

