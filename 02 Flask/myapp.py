from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hola mundo!!!!!!</h1>'

@app.route('/saludo/<nombre>')
def saludar(nombre):
    return f'Hola {nombre}'

if __name__ == '__main__':
    app.run(debug=True)

