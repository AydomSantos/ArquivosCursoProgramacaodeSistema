import sqlite3

conexao_sqlLite = sqlite3.connect("banco.tb")
cursor_sqlLite = conexao_sqlLite.cursor()

cursor_sqlLite.execute('''
                       UPDATE usuario 
                       SET s_nome_usuario = ? , i_idade_usuario = ? 
                       WHERE i_id_usuario_usuario < 0''',('teste', 25))
conexao_sqlLite.commit()
conexao_sqlLite.close()