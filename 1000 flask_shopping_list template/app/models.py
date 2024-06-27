from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Declarative base que define el modelo de datos
Base = declarative_base()

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
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    lists = relationship('ShoppingList', backref='owner', lazy=True)

# class ShoppingList(Base):
#     """
#     Modelo que representa la tabla 'ShoppingList' en la base de datos.
    
#     Attributes:
#         id (int): Identificador único de la lista de compras.
#         name (str): Nombre de la lista de compras, no nulo.
#         items (str): Artículos en la lista de compras, no nulo.
#         user_id (int): Identificador del usuario que posee la lista, no nulo.
#     """
class ShoppingList(Base):
    __tablename__ = "shopping_list"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    items = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)


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
def create_sessionLocal(database_url):
    # Configurar la base de datos
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(bind=engine)
    # Crear la base de datos y las tablas
    Base.metadata.create_all(engine)
    return SessionLocal

if __name__ == "__main__":
    # Ejemplo de uso de las clases en la base de datos
    from config import SQLALCHEMY_DATABASE_URI

    session_local = create_sessionLocal(SQLALCHEMY_DATABASE_URI)

    new_user =User(username='john_doe', email='john@example.com', password='securepassword')
    session_local.add(new_user)
    session_local.commit()

    shopping_list = ShoppingList(name='Groceries', items='Milk, Bread, Eggs', user_id=new_user.id)
    session_local.add(shopping_list)
    session_local.commit()

    # Para qué sirve relationship ?
    '''
    select * from user
    left join user.id = ShoppingList.user_id
    '''
    # Cuando cree la tabla de user y shopping list, establecí
    #que en owner viene la información de quien es el usuario
    # dueño de la lista

    # "de la tabla de listas, la primera lista y quien es el dueño"
    owner_user = session_local.query(ShoppingList).first().owner
    # en owner_user tengo la información de john_doe
