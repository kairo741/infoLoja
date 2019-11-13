import sqlite3


# Import dos Meus Arquivos
import user
import menus
import funcoes
import cliente
import servicos
from funcoes import cls




#Conexão ao Banco
conexao = sqlite3.connect("infoLoja.sqlite")

menus.menu_inicial()
# cliente.criarTabelaCliente(conexao)
# user.criarTabelaUser(conexao)
# servicos.criar_tabela_servicos(conexao)

conexao.close()
