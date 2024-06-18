import sqlalchemy
# Importamos (1er importante) engine 
# y variables que necesitamos para construir los objetos de SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float
# Importamos el 2do objeto importante: Base
# Importamos el 3er objeto importante: Session
from sqlalchemy.orm import declarative_base, sessionmaker

# Conexión a la base de datos
engine = create_engine('sqlite:///usuarios.sqlite')

# base
# Mapear objetos a la base de datos
Base = declarative_base()

# Creamos el objeto "usuario"
# debe ser igual a la estructura de la tabla a la que hará relación
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    rol = Column(String)

# CREATE TABLE IF NOT EXIST usuarios;
Base.metadata.create_all(engine)

# 3er Objeto importante: session
# EL objeto sesion controla las sesiones en la base de datos para mandar queries
# Es muy importante cerrar estas sesiones para no dejar a la base de datos esperando más peticiones
# La función sessionmaker genera un objeto que puede construir nuevas sesiones
# esto será muy útil cuando trabajemos con flask
FabricaSessiones = sessionmaker(bind=engine)
session = FabricaSessiones()

# Crearemos 3 usuarios para mandar a la BD
usuario1 = Usuario(nombre='alfa', rol='admin')
usuario2 = Usuario(nombre='beta', rol='user')
usuario3 = Usuario(nombre='gamma', rol='user')

# Podría agregar de uno en uno...
# session.add(usuario1)
# session.add(usuario2)
# session.add(usuario3)
session.add_all([usuario1, usuario2, usuario3])
session.commit() #manda los cambios a la base de datos
# select * from usuarios;
resultados = session.query(Usuario).all()
for row in resultados:
    print(row.nombre, row.rol)
# cerramos la sesión
session.close()