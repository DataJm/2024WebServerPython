from flask import Blueprint, render_template, redirect, url_for, flash, request, session, abort
from config import SQLALCHEMY_DATABASE_URI
from app.models import ShoppingList, create_sessionLocal
from functools import wraps

# Creación del Blueprint para el módulo principal
main = Blueprint('main', __name__)
SessionLocal = create_sessionLocal(SQLALCHEMY_DATABASE_URI)

# def login_required(f):
#     """
#     Decorador que redirige a la página de inicio si el usuario no está autenticado.
    
#     Args:
#         f (function): La función a decorar.
        
#     Returns:
#         function: La función decorada.
#     """

# @main.route('/')
# @main.route('/index')
# def index():
#     """
#     Maneja la página principal. Si el usuario está autenticado, redirige a la lista de compras.
#     Si no está autenticado, muestra la página de inicio.
    
#     Returns:
#         str: Redirige a la lista principal en caso de estar autenticado o renderiza la plantilla de inicio.
#     """

# @main.route('/list', methods=['GET', 'POST'])
# def list():
#     """
#     Maneja la creación y visualización de listas de compras. Si la solicitud es GET, muestra todas las listas del usuario.
#     Si la solicitud es POST, crea una nueva lista de compras.
    
#     Returns:
#         str: Renderiza la plantilla de listas en caso de GET o redirige a la lista principal en caso de éxito.
#     """

# @main.route('/list/<list_id>/delete', methods=['POST'])
# def delete_list(list_id):
#     """
#     Maneja la eliminación de una lista de compras.
    
#     Args:
#         list_id (int): El ID de la lista a eliminar.
        
#     Returns:
#         Redirige a la lista principal después de eliminar la lista.
#     """