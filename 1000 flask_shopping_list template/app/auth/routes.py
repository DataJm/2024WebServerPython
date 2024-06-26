from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from config import SQLALCHEMY_DATABASE_URI
from app.models import User, create_sessionLocal
import bcrypt
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

# def check_password(password, hashed_password):
#     """
#     Verifica si una contraseña coincide con su hash correspondiente.
    
#     Args:
#         password (str): La contraseña en texto plano.
#         hashed_password (bytes): El hash de la contraseña almacenada.
        
#     Returns:
#         bool: True si la contraseña coincide con el hash, False en caso contrario.
#     """

# def not_login_required(f):
#     """
#     Decorador que redirige a la página principal si el usuario ya está autenticado.
    
#     Args:
#         f (function): La función a decorar.
        
#     Returns:
#         function: La función decorada.
#     """


# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     """
#     Maneja el registro de un nuevo usuario. Si la solicitud es GET, muestra el formulario de registro.
#     Si la solicitud es POST, procesa los datos del formulario y crea un nuevo usuario.
    
#     Returns:
#         str: Renderiza la plantilla de registro en caso de GET o redirige a la lista principal en caso de éxito.
#     """

# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     """
#     Maneja el inicio de sesión de un usuario. Si la solicitud es GET, muestra el formulario de inicio de sesión.
#     Si la solicitud es POST, procesa los datos del formulario y autentica al usuario.
    
#     Returns:
#         str: Renderiza la plantilla de inicio de sesión en caso de GET o redirige a la lista principal en caso de éxito.
#     """

# @auth.route('/logout')
# def logout():
#     """
#     Maneja el cierre de sesión de un usuario.
    
#     Returns:
#         Redirige a la página principal después de cerrar sesión.
#     """
