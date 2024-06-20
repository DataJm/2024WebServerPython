from flask import Blueprint, render_template, request, redirect, url_for, flash

# Crear un blueprint llamado 'router'
router = Blueprint('router', __name__)

@router.route('/')
def home():
    """
    Ruta para la página de inicio.
    """
    return render_template('index.html')

@router.route('/proyectos')
def proyectos():
    """
    Ruta para la página de proyectos.
    """
    return render_template('proyectos.html')

@router.route('/about')
def about():
    """
    Ruta para la página 'About me'.
    """
    return render_template('about.html')

@router.route('/comentarios', methods=['GET', 'POST'])
def comentarios():
    """
    Ruta para la página de comentarios.
    Permite tanto solicitudes GET como POST.
    """
    if request.method == 'POST':
        comentario = request.form.get('comentario')

        # Procesar el comentario
        print(f'Recibí el siguiente comentario: {comentario}')

        # Mostrar un mensaje flash para informar al usuario que su comentario fue recibido
        flash('Hemos recibido tu comentario, muchas gracias !!!', 'success')

        # Redirigir a la misma página de comentarios
        return redirect(url_for('router.comentarios'))

    # Si el método de la solicitud es GET, renderizar la plantilla de comentarios
    return render_template('comentarios.html')