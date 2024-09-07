from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine

engine = create_engine("sqlite:///exemplo.db") 

db = SQLDatabase(engine)

consulta_sql = "SELECT * FROM usuarios;"  

usuarios_retorno = db.run(consulta_sql)
print(usuarios_retorno)