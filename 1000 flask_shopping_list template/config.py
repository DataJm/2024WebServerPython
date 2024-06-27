import os
'''
TODO: Crea dos variables:
SECRET_KEY con un string que funcionará como llave secreta
SQLALCHEMY_DATABASE_URI con el string de conexión
'''
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'