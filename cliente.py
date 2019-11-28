import sqlite3
from colorama import Fore, init, Back
import time
from funcoes import continuar, sair, isnumber, op_invalida, cls
#Código para semrpe resetar a cor a cada print
init(autoreset=True)



#Criando tabela "cliente"
def criarTabelaCliente(conexao):

    cursor = conexao.cursor()

    #Criando tabela "cliente"
    sql = '''CREATE TABLE IF NOT EXISTS cliente(
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            rg TEXT,
            celular TEXT NOT NULL,
            rua TEXT NOT NULL,
            num_casa TEXT NOT NULL,
            complemento TEXT,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL
        );'''

    #Executando o código SQL
    cursor.execute(sql)
    print(Fore.RED + "Tabela criada com sucesso!")


#Inserindo dados na tabela "cliente"
def inserirCliente(conexao):
    print("Inserindo usuário!")
    nome = input("Insira o nome do cliente: ")
    cpf = input("insira o CPF do cliente: ")
    rg = input("Insira o RG do cliente: ")
    celular = input("Insira o celular do cliente: ")
    rua = input("Insira a rua do endereço: ")
    num_casa = input("Insira o Número do endereço: ")
    complemento = input("Insira o complemento (se necessário): ")
    cidade = input("Insira a cidade: ")
    estado = input("Insira o estado: ")

    cursor = conexao.cursor()

    sql = '''INSERT INTO cliente VALUES(
        "{}",
        "{}",
        "{}",
        "{}",
        "{}",
        "{}",
        "{}",
        "{}",
        "{}"
    );'''.format(nome, cpf, rg, celular, rua, num_casa, complemento, cidade, estado)

    cursor.execute(sql)

    conexao.commit()
    print(Fore.RED + "Dados inseridos com sucesso!")


def listar_cliente(conexao):
    print(Fore.CYAN + """
    =========== Lista de clientes ===========""")
    cursor = conexao.cursor()
    sql = """
    SELECT rowid, nome, cpf, celular FROM cliente 
    """

    cursor.execute(sql)
    # Atributo para retornar o resultado o Select
    lista = cursor.fetchall()
    usuario = int(input("Insira o cliente específico que deseja ver: "))
    # Print dos atributos principais do usuário
    print(Fore.RED + "ID\t Nome\t \t\t CPF \t\t\t Celular")

    for i in lista:
        if(i[0] == usuario):
            print(Back.RED + f'{i[0]}\t', Back.RED + f'{i[1]:<13}\t\t',Back.RED + f'{i[2]:<13}\t\t', Back.RED + f'{i[3]:<13}')
        else:
            print(f'{i[0]}\t', f'{i[1]:<13}\t\t',f'{i[2]:<13}\t\t', f'{i[3]:<13}')


    continuar()




# # Algoritmo para excluir cliente
def excluir_cliente(conexao):
    cursor = conexao.cursor()

    while(True):
        cls()
        print(Fore.CYAN + """
    ========= Exclusão de clientes =========""")
        rowid = input("Qual o ID do cliente que deseja excluir? ")

        if(isnumber(rowid)):
            rowid = int(rowid)
            break

        else:
            print("Apenas números de IDs, ", end="")
            op_invalida()

    # Select dos atributos para serem usados para a confirmação
    sql = """
    SELECT nome, cpf, rowid FROM cliente
    WHERE rowid = {} 
    """.format(rowid)
    cursor.execute(sql)
    lista = cursor.fetchall()
 

    excluir = input(f'Deseja excluir o cliente "{Fore.RED}{lista[0][0]}{Fore.RESET}" que tem o CPF "{Fore.RED}{lista[0][1]}{Fore.RESET}"?(S/N) ')
    excluir = excluir.lower()

    if (excluir == 's'):
        while(True):
           
            confirmar = input("Confirme o ID do cliente, para a exclusão: ")
            if(confirmar == str(lista[0][2])):
                print(Fore.GREEN+"Excluindo", end='', flush=True)
                for i in range(5):
                    print(Fore.GREEN + '.', end='', flush=True)
                    time.sleep(0.5)

                print("")

                sql_excluir = """
                    DELETE FROM cliente
                    WHERE rowid = {}
                    """.format(rowid)
                cursor.execute(sql_excluir)
                conexao.commit()

                print(Fore.RED + "Você excluiu o cliente {}!".format(rowid))
                break

            else:
                print(Fore.RED + "ID incorreta!")

            continuar = input("Deseja continuar (S/N)? ")
            continuar = continuar.lower()
            cls()
            print(Fore.CYAN + """
    ========= Exclusão de clientes =========""")
            if (continuar == 'n'):
                sair()


# def inserir_testes(conexao):
#     cursor = conexao.cursor()

#     sql = '''
#         INSERT INTO user VALUES(
#             "teste",
#             "teste",
#             "teste",
#             "tecnico"
#         );
#     '''
#     cursor.execute(sql)
#     conexao.commit()



#Procedimento para dar um Drop Table na tabela de clientes
def excluir_tabela(conexao):
    cursor = conexao.cursor()

    sql = """
    DROP TABLE cliente"""

    cursor.execute(sql)

    print(Fore.RED+"Tabela Excluida!")


def alterar_cliente(conexao):
    cursor = conexao.cursor()

    while(True):
        cls()
        print(Fore.CYAN + """
        ======== Modificação de Cliente ========""")
        rowid = input("Qual o ID do cliente a ser modificado? ")

        if(isnumber(rowid)):
            num_os = int(rowid)
            break

        else:
            print("Digite somente números! ", end="")
            op_invalida()

    
    sql = f"""
    SELECT 
    rowid, nome, cpf, rg, celular
    FROM cliente  WHERE rowid = {num_os} """
    cursor.execute(sql)
    lista = cursor.fetchall()

    print(lista[0])

    while(True):
        cls()
        print(Fore.CYAN + """
        ======== Modificação de Cliente ========""")
        update = input("""O que deseja modificar? 
        (Nome, CPF, RG, Celular)
        
        """)
        update = update.lower()

        if(update == "nome"):
            no_sql = "nome"
            update_x = "o Nome do Cliente"
            atual = lista[0][1]
            break

        elif(update == "cpf"):
            no_sql = "cpf"
            update_x = "o CPF do Técnico"
            atual = lista[0][2]
            break

        elif(update == "rg"):
            no_sql = "rg"
            update_x = "o RG do cliente"
            atual = lista[0][3]
            break


        elif(update == "celular"):
            no_sql = "celular"
            update_x = "o Celular do cliente"
            atual = str(lista[0][4])
            break

        else:
            op_invalida()
            cls()
            print(Fore.CYAN + """
        ======== Modificação de Cliente ========""")

    update = input(
        f"Deseja mesmo alterar {update_x} do {Fore.RED}cliente {lista[0][0]}{Fore.RESET}? (S/N) ")
    update = update.lower()

    if(update == "s"):

        while(True):
            cls()
            print(Fore.CYAN + f"""
    ========= Modificando {update_x} =========""")
            novo = input(f"Insira {update_x} novo(a): ")
            while(True):
                cls()
                print(Fore.CYAN + f"""
    ========= Modificando {update_x} =========""")

                print(
                    f"Lembre-se {update_x} altual é '{Fore.CYAN}{atual}{Fore.RESET}'!")

                print(f"Voce digitou: {novo}")
                confirmar = input("Confirme {}: ".format(update_x))

                update = input(f"Deseja mesmo alterar {update_x}? (S/N) ")
                update = update.lower()
                if(update == "n"):
                    cls()
                    break
                if(confirmar == novo):

                        print(Fore.GREEN + "Alterando", end='', flush=True)
                        for i in range(5):
                            print(Fore.GREEN + '.', end='', flush=True)
                            time.sleep(0.5)
                        print()

                sql = f"""
                UPDATE cliente
                SET {no_sql} = "{confirmar}"
                WHERE rowid = {rowid} """
                cursor.execute(sql)
                conexao.commit()

                print(f"Você alterou {update_x} do Cliente {rowid}!")
                break

            else:
                print("Confirmação incorreta!")
                continuar = input("Deseja continuar (S/N)? ")
                continuar = continuar.lower()

                if (continuar == 'n'):
                    sair()

            continuar = input("Deseja alterar novamente (S/N)? ")
            continuar = continuar.lower()
            if (continuar == 'n'):
                break

    else:
        sair()
