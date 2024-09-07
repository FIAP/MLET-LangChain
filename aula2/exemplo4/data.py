import sqlite3

conn = sqlite3.connect('exemplo.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    profissao TEXT NOT NULL
)
''')

cursor.execute("INSERT INTO usuarios (nome, idade, profissao) VALUES ('Maria', 30, 'Engenheira')")
cursor.execute("INSERT INTO usuarios (nome, idade, profissao) VALUES ('João', 25, 'Designer')")
cursor.execute("INSERT INTO usuarios (nome, idade, profissao) VALUES ('Ana', 40, 'Gerente')")

conn.commit()
conn.close()
