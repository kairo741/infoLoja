import sqlite3
from colorama import Fore, init, Back
import time
from datetime import datetime
from funcoes import op_invalida, sair, cls, continuar



#Código para semrpe resetar a cor a cada print
init(autoreset=True)


def criar_tabela_servicos(conexao):
    cursor = conexao.cursor()

    #Criando tabela "servicos"
    sql = '''CREATE TABLE IF NOT EXISTS servicos(
            idcli INTEGER NOT NULL,
            iduser INTEGER NOT NULL,
            problema TEXT NOT NULL,            
            data_de_abertura TEXT NOT NULL,
            solucao TEXT,
            data_de_fechamento TEXT,
            valor REAL,
            FOREIGN KEY (iduser) REFERENCES user (rowid),
            FOREIGN KEY (idcli) REFERENCES cliente (rowid)

        );'''

    #Executando o código SQL
    cursor.execute(sql)
    print(Fore.RED + "Tabela criada com sucesso!")


def inserir_os(conexao):
    cursor = conexao.cursor()

    print(Fore.CYAN + """
    =========== Inserção de O.S. ===========""")
    idcli  = int(input("Insira o número de cadastro do cliente desejado: "))
    iduser = int(input("Insira o número de cadastro do técnico: "))
    problema = input("Qual o problema? ")
    data_de_abertura = datetime.now()
    data_hora = data_de_abertura.strftime('%d/%m/%Y %H:%M')

    sql = f"""
    INSERT INTO servicos (idcli, iduser, problema, data_de_abertura) VALUES(
      {idcli},
      {iduser},
      "{problema}",
      "{data_hora}"
    );"""
    cursor.execute(sql)

    conexao.commit()
    print(Fore.RED + "O.S. criada com sucesso!")
    
    continuar()



#Função para fechar uma OS:
def fechar_os(conexao):
    num_os = int(input("Insira o número da O.S. que deseja finalizar: "))
    solucao = input("Insira a solução: ")
    data_de_fechamento = datetime.now()
    data_de_fechamento = data_de_fechamento
    data_hora = data_de_fechamento.strftime('%d/%m/%Y %H:%M')

    valor = input("Valor total dos serviços: ")
    cursor = conexao.cursor()

    
    sql2 = f"""
    UPDATE servicos SET solucao="{solucao}" WHERE rowid = {num_os};"""
    sql3 = f"""
    UPDATE servicos SET data_de_fechamento="{data_hora}" WHERE rowid = {num_os};"""
    sql4=f"""
    UPDATE servicos SET valor={valor} WHERE rowid = {num_os}; """
    
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)
    conexao.commit()
    print(Fore.RED + "Dados inseridos com sucesso!")






def excluir_tabela(conexao):
    cursor = conexao.cursor()

    sql= """
    DROP TABLE servicos"""
    
    cursor.execute(sql)
    print(Fore.GREEN + "Tabela excluída")


#Esse procedimento faz o select com base no que o usuario registrou na OS e cria um arquivo como BKP da OS.
def finalizar_os(conexao):
    cursor = conexao.cursor()
    num_os = int(input("Insira o número da O.S. que deseja finalizar: "))
    sql = '''
    SELECT servicos.rowid AS "Número da OS", user.nome AS "Técnico", cliente.nome AS "Nome do Cliente",
    servicos.problema AS "Problema", servicos.data_de_abertura AS "Data de Abertura",
    servicos.solucao AS "Solução", servicos.data_de_fechamento AS "Data de Fechamento",
    servicos.valor AS "Valor do serviço"
    FROM servicos INNER JOIN user
    ON servicos.iduser = user.rowid
    INNER JOIN cliente
    ON servicos.idcli = cliente.rowid'''


    cursor.execute(sql)
    #Atributo para retornar o resultado o Select
    lista = cursor.fetchall()

    arquivo = open(f"{num_os}.txt", "w")
    for i in range(0, len(lista[num_os])):
        escrita = str(lista[num_os-1][i])
        arquivo.write(escrita+"@_@")
    print(Fore.GREEN + "Finalizada a ordem de serviço e feito o BKP!")
    arquivo.close()

    continuar()





def visualizar_os():
    num_os = int(input("Insira o número da O.S. que deseja visualizar: "))

    arquivo = open(f"{num_os}.txt", "r")
    conteudo = arquivo.readline()
    x = conteudo.split("@_@")
    print("""
   |--------------------------------------------------------------
   | """,Fore.RED+"""OS: """, f"""{x[0]}""",Fore.RED + """\t\t\tData de Entrada:""",f""" {x[4]:<}
   |--------------------------------------------------------------
   |""", Fore.RED+ """Técnico:""", f"""{x[1]}                 """, Fore.RED + """Cliente:""",f""" {x[2]}
""","""  |--------------------------------------------------------------
   |""",Fore.RED+ """Problema:""","""
   |""",f"""{x[3]:<}
   |--------------------------------------------------------------
   |""", Fore.RED +"""Solução:
  """,f"""| {x[5]}
   |--------------------------------------------------------------
   |""", Fore.RED + """Valor:""",f""" {x[7]}           """,Fore.RED+"""Data de Saída: """,f"""{x[6]}
   |--------------------------------------------------------------""")


    arquivo.close()

    continuar()




def teste_select(conexao):
    cursor = conexao.cursor()


    sql= '''
    SELECT servicos.rowid AS "Número da OS", user.nome AS "Técnico", cliente.nome AS "Nome do Cliente",
    servicos.problema AS "Problema", servicos.data_de_abertura AS "Data de Abertura",
    servicos.solucao AS "Solução", servicos.data_de_fechamento AS "Data de Fechamento",
    servicos.valor AS "Valor do serviço"
    FROM servicos INNER JOIN user
    ON servicos.iduser = user.rowid
    INNER JOIN cliente
    ON servicos.idcli = cliente.rowid'''

    cursor.execute(sql)
    #Atributo para retornar o resultado o Select
    lista = cursor.fetchall()
    print(lista)

