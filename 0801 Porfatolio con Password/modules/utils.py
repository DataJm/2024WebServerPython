'''
En este script vamos a dejar todo lo relacionado al ORM
- engine
- Base
- Session
'''
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

from datetime import datetime
# De nuestra carpeta config...
from config.database_url import connection_url

# engine
engine = create_engine(connection_url)

# Base
Base = declarative_base()

class Comentario(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True, index=True)
    comentario = Column(String(500), nullable=False)
    timestamp = Column(DateTime, default=datetime.now())

# Crear la base de datos / Tabla en caso de no existir
Base.metadata.create_all(bind=engine)

# Session
# Fábrica de sesiones
SessionLocal = sessionmaker(bind=engine)