#coding: utf-8

import sqlite3
from colorama import Fore, init, Back
import time
from funcoes import op_invalida, sair, cls


# Código para semrpe resetar a cor a cada print
init(autoreset=True)


# Criando tabela "user"
def criarTabelaUser(conexao):

    cursor = conexao.cursor()

    # Criando tabela "user"
    sql = '''CREATE TABLE IF NOT EXISTS user(
            nome TEXT NOT NULL,
            login TEXT NOT NULL,
            senha TEXT NOT NULL,
            cargo TEXT NOT NULL
        );'''

    # Executando o código SQL
    cursor.execute(sql)
    print(Fore.RED + "Tabela criada com sucesso!")


# Inserindo dados na tabela "user"
def inserirUser(conexao):
    print(Fore.CYAN + """
    ========= Cadastro de usuários =========""")
    nome = input("Insira o nome do Usuário: ")
    login = input("insira o login dejado para o Usuário: ")
    senha = input("Insira a senha desejada para o Usuário: ")
    cargo = input("Insira o cargo do Usuário: ")

    cursor = conexao.cursor()

    sql = '''INSERT INTO user VALUES(
        "{}",
        "{}",
        "{}",
        "{}"
    );'''.format(nome, login, senha, cargo)

    cursor.execute(sql)

    conexao.commit()
    print(Fore.RED + "Usuário cadastrado com sucesso!")


# Função para ver e listar usuários
def listar_user(conexao):
    print(Fore.CYAN + """
    =========== Lista de usuários ===========""")
    cursor = conexao.cursor()
    sql = """
    SELECT rowid, * FROM user 
    """

    cursor.execute(sql)
    # Atributo para retornar o resultado o Select
    lista = cursor.fetchall()
    usuario = int(input("Insira o usuário específico que deseja ver: "))
    # Print dos atributos principais do usuário
    print(Fore.RED + "ID\t Nome\t \t\t Login \t\t\t Cargo")

    for i in lista:
        if(i[0] == usuario):
            print(Back.RED + f'{i[0]}\t', Back.RED + f'{i[1]:<13}\t\t',Back.RED + f'{i[2]:<13}\t\t',Back.RED + f'{i[4]:<13}')
        else:
            print(f'{i[0]}\t', f'{i[1]:<13}\t\t', f'{i[2]:<13}\t\t',f'{i[4]:<13}')





# Algoritmo para dar UPDATE em um usuário
def update_usuario(conexao):
    cursor = conexao.cursor()
    print(Fore.CYAN + """
    ======== Modificação de usuário ========""")
    rowid = int(input("Qual o ID do usuario que deseja dar update? "))

    # Select dos atributos para serem usados para a confirmação
    sql = """
    SELECT nome, login,senha FROM user
    WHERE rowid = {} 
    """.format(rowid)
    cursor.execute(sql)
    
    while(True):
        update = input("O que deseja alterar (Nome, Login ou Senha)? ")
        update = update.lower()
        if(update == 'senha'):
            # Update_x: o x seria o que o usuario escolhe, senha, loguin ou nome
            update_x = 'a Senha'
            noSql = "senha"
            break

        elif(update == 'login'):
            update_x = 'o Login'
            noSql = "login"
            break

        elif(update == 'nome'):
            update_x = 'o Nome'
            noSql = "nome"
            break
        
        else:
            op_invalida()
            cls()
            print(Fore.CYAN + """
    ======== Modificação de usuário ========""")



    lista = cursor.fetchall()
    update = input(f'Deseja realmente alterar o usuário "{Fore.RED}{lista[0][0]}{Fore.RESET}" que tem o login {Fore.RED}{lista[0][1]}{Fore.RESET}"?(S/N) ')
    update = update.lower()

    
    if (update == 's'):
        while(True):
            confirmar = input("Insira a senha: ")
            if(confirmar == lista[0][2]):
                
                novo = input(f"Insira {update_x} novo(a) que deseja alterar: ")
                
                
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
                    continuar = continuar.lower()
                    
                    if (continuar == 'n'):
                        sair()

            else:
                print(Fore.RED + "Senha incorreta")

            
            continuar = input("Deseja alterar novamente (S/N)? ")
            continuar = continuar.lower()
            if (continuar ==  'n'):
                break
                




# Algoritmo para excluir usuário.
def excluir_usuario(conexao):
    cursor = conexao.cursor()
    
    while(True):
        cls()
        print(Fore.CYAN + """
    ========= Exclusão de usuários =========""")
        rowid = input("Qual o ID do usuario que deseja excluir? ")
        if(rowid != int):
            print("Apenas númerdos de IDs, ", end="")
            op_invalida()
        else:
            
            rowid = int(rowid)
            break

    # Select dos atributos para serem usados para a confirmação
    sql = """
    SELECT nome, login,senha FROM user
    WHERE rowid = {} 
    """.format(rowid)
    cursor.execute(sql)
    lista = cursor.fetchall()
    
    
    
    excluir = input(f'Deseja excluir o usuário "{Fore.RED}{lista[0][0]}{Fore.RESET}" que tem o login "{Fore.RED}{lista[0][1]}{Fore.RESET}"?(S/N) ')
    excluir = excluir.lower()



    if (excluir == 's'):
        while(True):
            confirmar = input("Insira a senha para a exclusão: ")
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
            continuar = continuar.lower()
            if (continuar == 'n'):
                sair()


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
