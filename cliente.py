import sqlite3
from colorama import Fore, init, Back
import time

#Código para semrpe resetar a cor a cada print
init(autoreset=True)



#Criando tabela "cliente"
def criarTabelaCliente(conexao):

    cursor = conexao.cursor()

    #Criando tabela "cliente"
    sql = '''CREATE TABLE IF NOT EXISTS cliente(
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
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
