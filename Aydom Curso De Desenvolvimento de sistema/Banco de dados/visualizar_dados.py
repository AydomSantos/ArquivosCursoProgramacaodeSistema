import sqlite3

conexao_sqlLite = sqlite3.connect("banco.tb")
cursor_sqlLite = conexao_sqlLite.cursor()

conexao_sqlLite.execute('SELECT * FROM dados')
conexao_sqlLite.commit()
conexao_sqlLite.close()

