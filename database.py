import sqlite3  


# Criando e conectando ao banco de dados

conexao = sqlite3.connect('lista_tarefas.db')


# Cursor : usado para navegar e manipular o banco
# Execute : usado para ler e executar comandos de SQL puro direto no db.

cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS lista_tarefas (id INTEGER NOT NULL PRIMARY KEY, nome TEXT NOT NULL, concluida INTEGER)")

