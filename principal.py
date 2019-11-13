import sqlite3


# Import dos Meus Arquivos
import user
import menus
import funcoes
import cliente
import servicos




#Conexão ao Banco
conexao = sqlite3.connect("infoLoja.sqlite")


# cliente.criarTabelaCliente(conexao)
# user.criarTabelaUser(conexao)
# servicos.criar_tabela_servicos(conexao)

conexao.close()
