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
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            # Redirige al usuario al login si no está autenticado
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

# @main.route('/')
# @main.route('/index')
# def index():
#     """
#     Maneja la página principal. Si el usuario está autenticado, redirige a la lista de compras.
#     Si no está autenticado, muestra la página de inicio.
    
#     Returns:
#         str: Redirige a la lista principal en caso de estar autenticado o renderiza la plantilla de inicio.
#     """
@main.route('/')
@main.route('/index')
def index():
    if 'logged_in' in session:
        return redirect(url_for('main.list'))
    else:
        return render_template('main/index.html')

# @main.route('/list', methods=['GET', 'POST'])
# def list():
#     """
#     Maneja la creación y visualización de listas de compras. Si la solicitud es GET, muestra todas las listas del usuario.
#     Si la solicitud es POST, crea una nueva lista de compras.
    
#     Returns:
#         str: Renderiza la plantilla de listas en caso de GET o redirige a la lista principal en caso de éxito.
#     """
@main.route('/list', methods=['GET', 'POST'])
@login_required
def list():
    if request.method == 'POST':
        # Esta es la lógica para guardar listas
        list_name = request.form.get('list_name')
        items = request.form.get('items')
        new_list = ShoppingList(name=list_name, items=items, user_id=session["current_user_id"])

        session_local = SessionLocal()
        try:
            session_local.add(new_list)
            session_local.commit()
            session_local.refresh(new_list)
            flash('List created successfully!', 'success')
        except:
            session_local.rollback()
            flash('Ocurrió un error al guardar', 'danger')
        finally:
            session_local.close()
        return redirect(url_for('main.list'))

    session_local = SessionLocal()
    user_lists = session_local.query(ShoppingList).filter_by(user_id=session["current_user_id"]).all()
    session_local.close()
    return render_template('main/list.html', user_lists=user_lists)

# @main.route('/list/<list_id>/delete', methods=['POST'])
# def delete_list(list_id):
#     """
#     Maneja la eliminación de una lista de compras.
    
#     Args:
#         list_id (int): El ID de la lista a eliminar.
        
#     Returns:
#         Redirige a la lista principal después de eliminar la lista.
#     """
@main.route('/list/<list_id>/delete', methods=['POST'])
@login_required
def delete_list(list_id):
    session_local = SessionLocal()
    list_to_delete = session_local.query(ShoppingList).filter(ShoppingList.id==list_id).first()

    if list_to_delete.user_id != session["current_user_id"]:
        abort(403)

    try:
        session_local.delete(list_to_delete)
        session_local.commit()
        flash('List deleted successfully!', 'success')
    except:
        session_local.rollback()
        flash('Ocurrió un error al borrar', 'danger')
    finally:
        session_local.close()
    return redirect(url_for('main.list'))