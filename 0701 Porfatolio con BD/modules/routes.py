from flask import Blueprint, render_template, request, redirect, url_for, flash
from modules.utils import Comentario, SessionLocal

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
        # TODO: No olvides agregar sanitización a este comentario
        comentario = request.form.get('comentario')

        # Procesar el comentario
        # instanciar un nuevo comentario y crear una nueva sesión para mandarlo a la BD
        nuevo_comentario = Comentario(comentario=comentario)
        # Crear la sesión
        session = SessionLocal()

        try:
            # Vamos a "intentar" insertar el nuevo registro
            session.add(nuevo_comentario)
            session.commit()
            session.refresh(nuevo_comentario)
            # Mostrar un mensaje flash para informar al usuario que su comentario fue recibido
            flash('Hemos recibido tu comentario, muchas gracias !!!', 'success')
        except:
            # En caso de que cualquier linea de código del bloque "try" falle... ocurre esto
            session.rollback()
            flash('Ocurrió un error al guardar tu comentario. Intenta más tarde', 'danger')
        finally:
            session.close()

        # Redirigir a la misma página de comentarios
        return redirect(url_for('router.comentarios'))

    # Si el método de la solicitud es GET, renderizar la plantilla de comentarios
    return render_template('comentarios.html')

@router.route("/api/comentarios")
def api_comentarios():
    '''
    Esta será nuestra API de comentarios,
    Debemos conectarnos a la base de datos, extraer TODOS los comentarios
    y pasarselos al usuario en formato JSON
    '''
    session = SessionLocal()
    try:
        # select * from comentarios
        comentarios = session.query(Comentario).all()
        # recordar que esto nos regresa un cursor
        lista_comentarios = []
        for comentario in comentarios:
            lista_comentarios.append({
                "id": comentario.id,
                "texto": comentario.comentario,
                "fecha": comentario.timestampaa
            })

        return lista_comentarios
    except Exception as error:
        print(error)
        return {"error":"Ocurrió un problema"}
    finally:
        session.close()