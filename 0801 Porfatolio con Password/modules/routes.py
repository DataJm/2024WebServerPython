from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from modules.utils import Comentario, SessionLocal
from functools import wraps
from config.config import check_password
from config.enviroment import HASHED_PASSWORD

# Función para verificar que el usuario esta logeado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" not in session:
            # Redirigimos al usuario al login
            return redirect(url_for("router.login"))
        return f(*args, **kwargs)
    return decorated_function

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
        db = SessionLocal()

        try:
            # Vamos a "intentar" insertar el nuevo registro
            db.add(nuevo_comentario)
            db.commit()
            db.refresh(nuevo_comentario)
            # Mostrar un mensaje flash para informar al usuario que su comentario fue recibido
            flash('Hemos recibido tu comentario, muchas gracias !!!', 'success')
        except:
            # En caso de que cualquier linea de código del bloque "try" falle... ocurre esto
            db.rollback()
            flash('Ocurrió un error al guardar tu comentario. Intenta más tarde', 'danger')
        finally:
            db.close()

        # Redirigir a la misma página de comentarios
        return redirect(url_for('router.comentarios'))

    # Si el método de la solicitud es GET, renderizar la plantilla de comentarios
    return render_template('comentarios.html')

@router.route("/api/comentarios")
@login_required
def api_comentarios():
    '''
    Esta será nuestra API de comentarios,
    Debemos conectarnos a la base de datos, extraer TODOS los comentarios
    y pasarselos al usuario en formato JSON
    '''
    db = SessionLocal()
    try:
        # select * from comentarios
        comentarios = db.query(Comentario).all()
        # recordar que esto nos regresa un cursor
        lista_comentarios = []
        for comentario in comentarios:
            lista_comentarios.append({
                "id": comentario.id,
                "texto": comentario.comentario,
                "fecha": comentario.timestamp
            })

        return lista_comentarios
    except Exception as error:
        print(error)
        return {"error":"Ocurrió un problema"}
    finally:
        db.close()

@router.route('/dashboard')
@login_required
def dashboard():
    db = SessionLocal()
    try:
        # select * from comentarios
        comentarios = db.query(Comentario).all()
    except Exception as error:
        print(error)
        flash("Error en BD", "danger")
        comentarios = []
    finally:
        db.close()

    return render_template(
        'dashboard.html',
        comentarios=comentarios
    )

'''
De acuerdo con la documentación de Flask, los session están basados en cookies.
Es una forma fácil, con seguridad "intermedia" de implementar autenticación de usuarios.
Sin embargo cuenta con las mismas limitaciones que tendría una cookie: podrían
estar bloqueadas en la maquina de cliente, y además necesita "si o si" una maquina virtual
(es decir, nuestra aplicación no podría estar montada en un servicio "serverless")
Existen muchisimas alternativas para solucionar esto, pero todas requieren de librerías
adicionales a flask.
(like OAuth, OpenID Connect, JSON Web Tokens (JWTs))
Recomendación personal : Flask-JWT-Extended
'''
@router.route('/login', methods = ["GET", "POST"])
def login():
    if request.method=="POST":
        password = request.form.get("password")
        
        # Volver Bytes nuestro password
        hashed_password = bytes.fromhex(HASHED_PASSWORD)
        if check_password(password, hashed_password):
        # if password=="1234":
            session["logged_in"] = True
            return redirect(url_for("router.dashboard"))
        else:
            flash("Contraseña incorrecta", "danger")
            return redirect(url_for("router.login"))

    return render_template('login.html')

@router.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("router.home"))