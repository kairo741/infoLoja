import sqlite3

# Import dos Meus Arquivos
import user
import menus
import funcoes
import cliente
import servicos
from funcoes import cls


#Conexao ao Banco
conexao = sqlite3.connect("infoLoja.sqlite")


 
# cliente.inserirCliente(conexao)
# servicos.inserir_os(conexao)

# servicos.excluir_tabela(conexao)
# servicos.fechar_os(conexao)
# user.inserirUser(conexao)

# servicos.salvar_os(conexao)
servicos.visualizar_os()
# user.listar_user(conexao)
# user.excluir_usuario(conexao)



# Criar tabelas
# cliente.criarTabelaCliente(conexao)
# user.criarTabelaUser(conexao)
# servicos.criar_tabela_servicos(conexao)

conexao.close()

