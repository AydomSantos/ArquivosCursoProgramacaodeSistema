import sqlite3

conexao_sqlLite = sqlite3.connect("banco.tb")
cursor_sqlLite = conexao_sqlLite.cursor()

conexao_sqlLite.execute('DELETE FROM usuario WHERE i_id_usuario_usuario == i_id_usuario_usuario')
conexao_sqlLite.commit()
conexao_sqlLite.close()
