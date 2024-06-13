from flask import Blueprint, render_template

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

@router.route('/comentarios')
def comentarios():
    return  render_template ('comentarios.html')
