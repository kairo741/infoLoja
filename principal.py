import funcoes
import sqlite3

#Conexão ao Banco
conexao = sqlite3.connect("infoLoja.sqlite")



# funcoes.criarTabelaUser(conexao)
# funcoes.inserirUser(conexao)

# funcoes.inserir_testes(conexao)

# funcoes.update_usuario(conexao)
# funcoes.listar_user(conexao)
funcoes.excluir_usuario(conexao)



conexao.close()
