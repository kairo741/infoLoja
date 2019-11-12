import sqlite3
from colorama import Fore, init, Back
import time

from os import system


#Função para limpar cmd
def cls():
    system('cls')

init(autoreset=True)

#Criando tabela "user"
def criarTabelaUser(conexao):

    cursor = conexao.cursor()

    #Criando tabela "user"
    sql = '''CREATE TABLE IF NOT EXISTS user(
            nome TEXT NOT NULL,
            login TEXT NOT NULL,
            senha TEXT NOT NULL,
            cargo TEXT NOT NULL
        );'''

    #Executando o código SQL
    cursor.execute(sql)
    print(Fore.RED + "Tabela criada com sucesso!")




#Inserindo dados na tabela "user"
def inserirUser(conexao):
    print("Inserindo usuário!")
    nome = input("Insira o nome do Usuário: ")
    login = input("insira o login dejado para o Usuário: ")
    senha = input("Insira a senha desejada para o Usuário: ")
    cargo = input("Insira o cargo do Usuário: ")

    cursor = conexao.cursor()

    sql='''INSERT INTO user VALUES(
        "{}",
        "{}",
        "{}",
        "{}"
    );'''.format(nome, login, senha, cargo)
    
    cursor.execute(sql)
       
    conexao.commit()
    print(Fore.RED + "Dados inseridos com sucesso!")



#Função para ver e listar usuários
def listar_user(conexao):
    cursor = conexao.cursor()
    sql = """
    SELECT rowid, * FROM user 
    """

    cursor.execute(sql)
    #Atributo para retornar o resultado o Select
    lista = cursor.fetchall()
    usuario = int(input("Insira o usuário específico que deseja ver: "))
    #Print dos atributos principais do usuário
    print("ID\t Nome\t \t\t Login \t\t Cargo")
    
    for i in lista:
        if(i[0] == usuario):
            print(Back.RED + '{} \t {}\t \t\t {} \t\t {}'.format(i[0], i[1], i[2], i[4]))
        else:
            print('{} \t {}\t \t\t {} \t\t {}'.format(i[0], i[1], i[2], i[4]))


#Algoritmo para dar UPDATE em um usuário
def update_usuario(conexao):
    cursor = conexao.cursor()
    rowid = int(input("Qual o ID do usuario que deseja dar update? "))

    #Select dos atributos para serem usados para a confirmação
    sql = """
    SELECT nome, login,senha FROM user
    WHERE rowid = {} 
    """.format(rowid)
    cursor.execute(sql)

    update = input("O que deseja alterar (Nome, Login ou Senha)? ")

    if(update == 'senha' or update == 'Senha'):
        #Update_x: o x seria o que o usuario escolhe, senha, loguin ou nome
        update_x = 'a Senha'
        noSql = "senha"

    elif(update == 'Login' or update == 'login'):
        update_x = 'o Login'
        noSql = "login"

    elif(update == 'nome' or update == 'Nome'):
        update_x = 'o Nome'
        noSql = "nome"

    lista = cursor.fetchall()
    update = input('Deseja realmente dar alterar {} do usuário "{}" que tem o login "{}"? (S/N)'.format(update_x, lista[0][0], lista[0][1]))

    if (update == 'S' or update == 's'):
        while(True):
            confirmar = input("Insira a senha: ")
            if(confirmar == lista[0][2]):
                novo = input(
                    "Insira {} novo(a) que deseja alterar: ".format(update_x))
                while(True):

                    confirmar = input("Confirme {}: ".format(update_x))
                    if(confirmar == novo):
                        print(Fore.GREEN + "Alterando", end='', flush=True)
                        for i in range(5):
                            print(Fore.GREEN + '.', end='', flush=True)
                            time.sleep(0.5)
                        print()
                        sql_alterar = """
                            UPDATE user
                            SET {} = '{}'
                            WHERE rowid = {};
                            """.format(noSql, novo, rowid)

                        cursor.execute(sql_alterar)
                        conexao.commit()

                        print("Você alterou {} do Usuário {}!".format(
                            update_x, rowid))
                        break
                    else:
                        print("Confirmação incorreta!")
                    continuar = input("Deseja continuar (S/N)? ")
                    if (continuar == 'N' or continuar == 'n'):
                        print("Você saiu!")
                        break

            else:
                print(Fore.RED + "Senha incorreta")

            continuar = input("Deseja continuar (S/N)? ")
            if (continuar == 'N' or continuar == 'n'):
                print("Você saiu!")
                break

    else:
        print("Até mais")


#Algoritmo para excluir de dados.
def excluir_usuario(conexao):
    cursor = conexao.cursor()
    rowid = int(input("Qual o ID do usuario que deseja excluir? "))
   
   
    #Select dos atributos para serem usados para a confirmação
    sql = """
    SELECT nome, login,senha FROM user
    WHERE rowid = {} 
    """.format(rowid)
    cursor.execute(sql)
    lista = cursor.fetchall()
    excluir = input(
        'Deseja dar excluir o usuário "{}" que tem o login "{}"? (S/N)'.format(lista[0][0], lista[0][1]))

    if (excluir == 'S' or excluir == 's'):
        while(True):
            confirmar = input("Insira a senha (atual) para alterar: ")
            if(confirmar == lista[0][2]):
                print(Fore.GREEN+"Excluindo", end='', flush=True)
                for i in range(5):
                    print(Fore.GREEN + '.', end='', flush=True)
                    time.sleep(0.5)

                print("")

                sql_excluir = """
                    DELETE FROM user
                    WHERE rowid = {}
                    """.format(rowid)
                cursor.execute(sql_excluir)
                conexao.commit()

                print(Fore.RED + "Você excluiu o Usuário {}!".format(rowid))
                break

            else:
                print(Fore.RED + "Senha incorreta")

            continuar = input("Deseja continuar (S/N)? ")
            if (continuar == 'N' or continuar == 'n'):
                print("Você saiu!")
                break

    else:
        print("Até mais")



def inserir_testes(conexao):
    cursor = conexao.cursor()


    sql = '''
        INSERT INTO user VALUES(
            "teste",
            "teste",
            "teste",
            "tecnico"
        );
    '''
    cursor.execute(sql)
    conexao.commit()


def criar_tabela_servicos(conexao):
    cursor = conexao.cursor()

    #Criando tabela "servicos"
    sql = '''CREATE TABLE IF NOT EXISTS servicos(
            idcli INTEGER NOT NULL,
            problema TEXT NOT NULL,
            iduser INTEGER NOT NULL,
            FOREIGN KEY (iduser) REFERENCES user (rowid),
            data_de_abertura DATE NOT NULL,
            solucao TEXT NOT NULL,
            data_de_fechamento TEXT NOT NULL
        );'''

    #Executando o código SQL
    cursor.execute(sql)
    print(Fore.RED + "Tabela criada com sucesso!")

def login(conexao):
    cursor = conexao.cursor()

    login = input("Login: ")
    senha = input("Senha: ")

    sql = """
    SELECT rowid, * FROM user 
    """
    cursor.execute(sql)

    lista = cursor.fetchall()


    for i in range (0, len(lista)):
        if(lista[i][2] == login and lista[i][3] == senha):
            print(Fore.LIGHTGREEN_EX + "Bem Vindo ao INFO LOJA {}!".format(lista[i][1]))   
            

  
