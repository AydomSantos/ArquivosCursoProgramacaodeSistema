# importando o sqlLite

import sqlite3

conexao_sqlLite = sqlite3.connect("banco.db")
cursor_sqlLite = conexao_sqlLite.cursor()

cursor_sqlLite.execute('''
                       
CREATE TABLE IF NOT EXISTS usuario(
  i_id_usuario_usuario INTEGER PRIMARY KEY ,
  s_nome_usuario VARCHAR(50)  NOT NULL ,
  i_idade_usuario INTEGER  NOT NULL               
)
''')

conexao_sqlLite.close()