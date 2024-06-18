import sqlalchemy
# Controlar la conexión a la base de datos
# Engine (1er objeto importante)
from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///usuarios.sqlite")
# Nuestro query es un string
query = "create table usuarios"
'''
Nota:
En versiones anteriores de SQLAlchemy podias hacer lo siguiente:
engine.execute(query)

Aunque era una muy buena idea, esto genero malas prácticas que si traían
problemas para la base de datos. Principalmente NO cerrar conexiones.
Además, siempre hay una "falla" de seguridad al mandar 
código SQL en crudo (raw SQL)
'''
# Cómo se trabaja hoy día
# Lo primero, utilizar la funcíon text para crear raw sql
# query = text(query)
query = text("""
CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY,
    nombre VARCHAR,
    rol VARCHAR
)
""")
with engine.connect() as connection:
    results = connection.execute(query)
    # for row in results:
    #     print(row)