# Realizando a inserção de valores no campo nome e idade do banco de dados 


import sqlite3

conexao_sqlLite = sqlite3.connect("banco.tb")
cursor_sqlLite = conexao_sqlLite.cursor()

cursor_sqlLite.execute('INSERT INTO usuario(s_nome_usuario,  i_idade_usuario) VALUES(? , ?)', ('Aydom', 23))
cursor_sqlLite.execute('INSERT INTO usuario(s_nome_usuario,  i_idade_usuario) VALUES(? , ?)', ('Paulo', 28))
conexao_sqlLite.commit()
conexao_sqlLite.close()

# deletar 
# visualizar 
# edita