import user
import sqlite3


conexao = sqlite3.connect("infoLoja.sqlite")
user.update_usuario(conexao)
