import sqlite3
from colorama import Fore, init, Back
import time
from datetime import date


#Código para semrpe resetar a cor a cada print
init(autoreset=True)


def criar_tabela_servicos(conexao):
    cursor = conexao.cursor()

    #Criando tabela "servicos"
    sql = '''CREATE TABLE IF NOT EXISTS servicos(
            idcli INTEGER NOT NULL,
            iduser INTEGER NOT NULL,
            problema TEXT NOT NULL,            
            data_de_abertura DATE NOT NULL,
            solucao TEXT,
            data_de_fechamento DATE,
            valor REAL,
            FOREIGN KEY (iduser) REFERENCES user (rowid),
            FOREIGN KEY (idcli) REFERENCES cliente (rowid)

        );'''

    #Executando o código SQL
    cursor.execute(sql)
    print(Fore.RED + "Tabela criada com sucesso!")


def inserir_os(conexao):
    cursor = conexao.cursor()

    print("Inserindo O.S.!")
    idcli  = int(input("Insira o número de cadastro do cliente desejado: "))
    iduser = int(input("Insira o número de cadastro do técnico: "))
    problema = input("Qual o problema? ")
    data_de_abertura = date.today()

    sql = f"""
    INSERT INTO servicos (idcli, iduser, problema, data_de_abertura) VALUES(
      {idcli},
      {iduser},
      "{problema}",
      {data_de_abertura}
    );"""
    cursor.execute(sql)

    conexao.commit()
    print(Fore.RED + "O.S. criada com sucesso!")


def fechar_os(conexao):
    num_os = int(input("Insira o número da O.S. que deseja finalizar: "))
    solucao = input("Insira a solução: ")
    data_de_fechamento = date.today()
    valor = input("Valor total dos serviços: ")
    cursor = conexao.cursor()

    sql = """
    SELECT rowid, * FROM servicos
    """
    cursor.execute(sql)
    #Atributo para retornar o resultado o Select
    lista = cursor.fetchall()

    sql2 = f"""
    UPDATE servicos SET solucao="{solucao}" WHERE rowid = {num_os};"""
    sql3 = f"""
    UPDATE servicos SET data_de_fechamento={data_de_fechamento} WHERE rowid = {num_os};"""
    sql4=f"""
    UPDATE servicos SET valor={valor} WHERE rowid = {num_os}; """
    
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)
    conexao.commit()
    print(Fore.RED + "Dados inseridos com sucesso!")
    print(data_de_fechamento)





def excluir_tabela(conexao):
    cursor = conexao.cursor()

    sql= """
    DROP TABLE servicos"""
    
    cursor.execute(sql)
    print(Fore.GREEN + "Tabela excluída")

# print(date.today())