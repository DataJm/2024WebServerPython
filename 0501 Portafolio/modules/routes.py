from flask import Blueprint, render_template, request, redirect, url_for, flash

router = Blueprint('router', __name__)

@router.route('/')
def home():
    return  render_template ('index.html')

@router.route('/proyectos')
def proyectos():
    return  render_template ('proyectos.html')

@router.route('/about')
def about():
    return  render_template ('about.html')

@router.route('/comentarios', methods=['GET','POST'])
def comentarios():
    if request.method=='POST':
        
        # TODO: Cuidar la seguridad (es confiable la información que viene en el comentario?)
        comentario = request.form.get('comentario')

        # TODO: Procesar el comentario
        print(f'Recibí el siguiente comentario: {comentario}')

        flash('Hemos recibido tu comentario, muchas gracias !!!')
        return redirect(url_for('router.comentarios'))

    return  render_template ('comentarios.html')
