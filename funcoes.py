import sqlite3


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
    print("Tabela criada com sucesso!")




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
    print("Dados inseridos com sucesso!")


def listar_usuario(conexao):
    cursor = conexao.cursor()
    sql = """
    SELECT rowid, * FROM user 
    """

    cursor.execute(sql)
    lista = cursor.fetchall()

    print("ID\t Nome\t \t\t Login")
    for i in lista:
        print('{} \t {} \t\t {}'.format(i[0], i[1], i[2]))
