from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Declarative base que define el modelo de datos

# class User(Base):
#     """
#     Modelo que representa la tabla 'user' en la base de datos.
    
#     Attributes:
#         id (int): Identificador único del usuario.
#         username (str): Nombre de usuario, debe ser único y no nulo.
#         email (str): Correo electrónico del usuario, debe ser único y no nulo.
#         password (str): Contraseña del usuario, no nula.
#         lists (relationship): Relación con la tabla 'ShoppingList'.
#     """

# class ShoppingList(Base):
#     """
#     Modelo que representa la tabla 'ShoppingList' en la base de datos.
    
#     Attributes:
#         id (int): Identificador único de la lista de compras.
#         name (str): Nombre de la lista de compras, no nulo.
#         items (str): Artículos en la lista de compras, no nulo.
#         user_id (int): Identificador del usuario que posee la lista, no nulo.
#     """

# def create_sessionLocal(database_url):
#     """
#     Configura la base de datos, crea las tablas y devuelve una sesión de la base de datos.
    
#     Args:
#         database_url (str): La URL de la base de datos.
        
#     Returns:
#         sessionmaker: Una clase configurada para manejar sesiones de la base de datos.
#     """
#     # Configurar la base de datos

#     # Crear la base de datos y las tablas

#     # return SessionLocal