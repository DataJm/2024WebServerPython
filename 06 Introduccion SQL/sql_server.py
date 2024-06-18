'''
Ejemplo de cómo conectarse a SQL Server
'''
import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
# 1er objeto importante: engine
# engine = create_engine('mssql+pyodbc://<username>:<password>@<dsnname>')
# SQL Server connection string
connection_string = (
    "Driver={SQL Server};"
    "Server=MXW20125004,65074;"
    "Database=BDCOBPROCESO;"
    "Trusted_Connection=yes;"
)
# Creating connection URL
connection_url = URL.create(
    "mssql+pyodbc", 
    query={"odbc_connect": connection_string}
)
# Creating the engine
engine = create_engine(connection_url)
query = text("""
SELECT * FROM DBO.MX_TW_USUARIOS LIMIT 10 ;
""")
with engine.connect() as connection:
    results = connection.execute(query)
    for row in results:
        print(row)


