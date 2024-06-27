from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from config import SQLALCHEMY_DATABASE_URI
from app.models import User, create_sessionLocal
import os
import hashlib
from functools import wraps

# Creación del Blueprint para el módulo de autenticación
auth = Blueprint('auth', __name__)
SessionLocal = create_sessionLocal(SQLALCHEMY_DATABASE_URI)

# def hash_password(password):
#     """
#     Genera un hash para una contraseña dada.
    
#     Args:
#         password (str): La contraseña en texto plano.
        
#     Returns:
#         bytes: El hash de la contraseña generada con una sal.
#     """
def hash_password(password):
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    return salt + hashed_password

# def check_password(password, hashed_password):
#     """
#     Verifica si una contraseña coincide con su hash correspondiente.
    
#     Args:
#         password (str): La contraseña en texto plano.
#         hashed_password (bytes): El hash de la contraseña almacenada.
        
#     Returns:
#         bool: True si la contraseña coincide con el hash, False en caso contrario.
#     """
def check_password(password, hashed_password):
    # print("123456"[:3])
    salt = hashed_password[:16]
    stored_hash = hashed_password[16:]
    new_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    return new_hash == stored_hash

# def not_login_required(f):
#     """
#     Decorador que redirige a la página principal si el usuario ya está autenticado.
    
#     Args:
#         f (function): La función a decorar.
        
#     Returns:
#         function: La función decorada.
#     """
def not_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' in session:
            # El usuario está autenticado
            return redirect(url_for('main.list'))
        return f(*args, **kwargs)
    return decorated_function

# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     """
#     Maneja el registro de un nuevo usuario. Si la solicitud es GET, muestra el formulario de registro.
#     Si la solicitud es POST, procesa los datos del formulario y crea un nuevo usuario.
    
#     Returns:
#         str: Renderiza la plantilla de registro en caso de GET o redirige a la lista principal en caso de éxito.
#     """
@auth.route('/register', methods=['GET', 'POST'])
@not_login_required
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password!=confirm_password:
            flash('Los passwords no coinciden', 'danger')
            return redirect(url_for('auth.register'))
        
        hashed_password = hash_password(password)

        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        session_local = SessionLocal()
        try:
            session_local.add(new_user)
            session_local.commit()
            session_local.refresh(new_user)
            flash('Usuario registrado!', 'success')
            user = session_local.query(User).filter(User.id==new_user.id).first()
            session["logged_in"] = True
            session["current_user_id"] = user.id
        except:
            session_local.rollback()
            flash('Ocurrió un error al crear', 'danger')
        finally:
            session_local.close()
        return redirect(url_for('main.list'))
    return render_template('auth/register.html')


# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     """
#     Maneja el inicio de sesión de un usuario. Si la solicitud es GET, muestra el formulario de inicio de sesión.
#     Si la solicitud es POST, procesa los datos del formulario y autentica al usuario.
    
#     Returns:
#         str: Renderiza la plantilla de inicio de sesión en caso de GET o redirige a la lista principal en caso de éxito.
#     """
@auth.route('/login', methods=['GET', 'POST'])
@not_login_required
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        session_local = SessionLocal()

        try:
            user = session_local.query(User).filter(User.email==email).first()
            if not check_password(password, user.password):
                flash('Password incorrecto', 'danger')
                return redirect(url_for('auth.register'))
            flash('Welcome!', 'success')
            session["logged_in"] = True
            session["current_user_id"] = user.id
        except:
            session_local.rollback()
            flash('Ocurrió un error', 'danger')
        finally:
            session_local.close()
        return redirect(url_for('main.list'))
    return render_template('auth/login.html')

# @auth.route('/logout')
# def logout():
#     """
#     Maneja el cierre de sesión de un usuario.
    
#     Returns:
#         Redirige a la página principal después de cerrar sesión.
#     """
@auth.route('/logout')
def logout():
    session.pop("logged_in", None)
    session.pop("current_user_id", None)
    return redirect(url_for('main.index'))