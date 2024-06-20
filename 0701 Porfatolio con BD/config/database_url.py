'''
En este script, hacemos todo lo relacionado
con la conexión a la base de datos
y debemos dejar listo el string de conexión
'''
# e.g. SQLServer
# connection_string = (
#     "Driver={SQL Server};"
#     "Server=MXW20125004,65074;"
#     "Database=BDCOBPROCESO;"
#     "Trusted_Connection=yes;"
# )
# # Creating connection URL
# connection_url = URL.create(
#     "mssql+pyodbc", 
#     query={"odbc_connect": connection_string}
# )

# e.g. Postgresql
# connection_url = postgresql+psycopg2://user:password@host:port/dbname

# sqlite
connection_url = "sqlite:///data/comentarios.db"