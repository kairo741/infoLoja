import sqlite3
from colorama import Fore, init, Back
import time

#Código para semrpe resetar a cor a cada print
init(autoreset=True)


def criar_tabela_servicos(conexao):
    cursor = conexao.cursor()

    #Criando tabela "servicos"
    sql = '''CREATE TABLE IF NOT EXISTS servicos(
            idcli INTEGER NOT NULL,
            problema TEXT NOT NULL,
            iduser INTEGER NOT NULL,
            data_de_abertura DATE NOT NULL,
            solucao TEXT NOT NULL,
            data_de_fechamento TEXT NOT NULL,
            FOREIGN KEY (iduser) REFERENCES user (rowid),
            FOREIGN KEY (idcli) REFERENCES cliente (rowid)

        );'''

    #Executando o código SQL
    cursor.execute(sql)
    print(Fore.RED + "Tabela criada com sucesso!")
