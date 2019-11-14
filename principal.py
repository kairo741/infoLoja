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
cls()
menus.menu_inicial()
a = input("Opção: ")
cls()
menus.menu_usuario()
# user.inserir_testes(conexao)
# user.listar_user(conexao)
# user.excluir_usuario(conexao)
# cliente.criarTabelaCliente(conexao)
# user.criarTabelaUser(conexao)
# servicos.criar_tabela_servicos(conexao)

conexao.close()

