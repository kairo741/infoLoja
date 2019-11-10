import funcoes
import sqlite3

#Conexão ao Banco
conexao = sqlite3.connect("infoLoja.sqlite")




funcoes.criarTabelaUser(conexao)
# funcoes.inserirUser(conexao)




funcoes.listar_usuario(conexao)



conexao.close()
