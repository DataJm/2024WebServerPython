from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    mensaje = '<h1>Valor desde python</h1>'

    valores = {
        'nombre': 'jose',
        'trabajo': 'instructor'
    }

    return render_template('index.html', mensaje=mensaje, **valores)

'''
TODO:

Crea una ruta '/about' donde venga información
sobre el creador de esta página web (o sea tú)

- Coloca nombre
- Pasatiempos
Y todo que creas pertinente para tus visitantes

'''



if __name__=='__main__':
    app.run(debug=True)