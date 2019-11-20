import user
import sqlite3
import servicos

conexao = sqlite3.connect("infoLoja.sqlite")
# user.listar_user(conexao)
# servicos.teste_select(conexao)

# servicos.salvar_os(conexao)
# servicos.visualizar_os()
# user.excluir_usuario(conexao)
servicos.alterar_os(conexao)
