from sqlalchemy.sql import text
from sqlalchemy import create_engine

import secrets


engine = create_engine(
    'mssql+pyodbc://{}:{}@MSSQL'.format(
        secrets.username, secrets.password
    )
)
conn = engine.connect()

s = text("SELECT * FROM users WHERE name = :name")
result = conn.execute(s, name=name).fetchall()
print result


