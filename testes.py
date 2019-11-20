import user
import sqlite3
import servicos

import hashlib

conexao = sqlite3.connect("infoLoja.sqlite")
# user.listar_user(conexao)
# servicos.teste_select(conexao)

# servicos.salvar_os(conexao)
# servicos.visualizar_os()
# user.excluir_usuario(conexao)
# servicos.alterar_os(conexao)


# senha = hashlib.md5(b"Kairo")
# senha = senha.digest()
# print(senha)
servicos.relatorio_os_mes(conexao)
