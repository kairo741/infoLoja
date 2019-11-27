import sqlite3
from colorama import Fore, init, Back
import time
from datetime import datetime
from funcoes import op_invalida, sair, cls, continuar, isnumber



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
    continuar()





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
    #Print Configurado para o formato de os, futuramente gerar formatod HTML e criar o print com For
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



def alterar_os(conexao):
    cursor = conexao.cursor()
    
    while(True):
        cls()
        print(Fore.CYAN + """
        ========= Modificação de O.S. =========""")
        num_os = input("Qual o número da O.S. a ser modificada? ")

        if(isnumber(num_os) ):
            num_os = int(num_os)
            break

        else:
            print("Digite somente números! ", end="")
            op_invalida()

    # sql = f"""
    # SELECT servicos.rowid, user.nome, cliente.nome, servicos.problema, servicos.solucao, 
    # servicos.data_de_fechamento, servicos.valor
    # FROM servicos INNER JOIN user
    # ON servicos.iduser = user.rowid
    # INNER JOIN cliente
    # ON servicos.idcli = cliente.rowid
    # """    
    sql = f"""
    SELECT 
    rowid, idcli, iduser, problema, solucao, data_de_fechamento, valor
    FROM servicos  WHERE rowid = {num_os} """    
    cursor.execute(sql)
    lista = cursor.fetchall()

    

    print(lista[0])
    
    while(True):
        update = input("""O que deseja modificar? 
        (idcli [ID do Cliente], iduser [ID do Técnico], problema, solução ou valor)
        
        """)
        update = update.lower()


        if(update == "idcli" ):
            no_sql = "idcli"
            update_x = "o ID do Cliente"
            atual = lista[0][1]
            break

        elif( update == "iduser"):
            no_sql = "iduser"
            update_x = "o ID do Técnico"
            atual = lista[0][2]
            break
            
        
        elif(update == "problema" ):
            no_sql = "problema"
            update_x = "o problema"
            atual = lista[0][3]
            break

        elif(update == "solução" or update == "solucao"):
            no_sql = "solucao"
            update_x = "a solução"
            atual = str(lista[0][4])
            break
            
        elif(update == "valor"):
            no_sql = "valor"
            update_x = "o valor final"
            atual = str(lista[0][6])
            break
        
        else:
            op_invalida()
            cls()
            print(Fore.CYAN + """
        ========= Modificação de O.S. =========""")

    
    update = input(f"Deseja mesmo alterar {update_x} da {Fore.RED}O.S. {lista[0][0]}{Fore.RESET}? (S/N) ")
    update = update.lower()

    if(update == "s"):

        while(True):
            if(atual == "None"):
                print("Esse atibuto ainda não está prenchido!")   
                

            else: 
                novo = input(f"Insira {update_x} novo(a): ")
                while(True):
                    cls()
                    print(Fore.CYAN + f"""
        ========= Modificando {update_x} =========""")

                    print(f"Lembre-se {update_x} altual é '{Fore.CYAN}{atual}{Fore.RESET}'!")
                    
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
                    UPDATE servicos
                    SET {no_sql} = "{confirmar}"
                    WHERE rowid = {num_os} """
                    cursor.execute(sql)
                    conexao.commit()

                    print(f"Você alterou {update_x} da O.S. {num_os}!")
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



def relatorio_os_mes(conexao):
    cursor = conexao.cursor()

    mes = input("Insira o o número do mês que deseja ver o relatório de Ordens de Serviço criadas: ")


    sql = """
    SELECT servicos.rowid, servicos.data_de_abertura, user.nome FROM servicos
    INNER JOIN user 
    ON servicos.iduser = user.rowid

    """
    cursor.execute(sql)
    

    lista = cursor.fetchall()
    
    cls()
    # print(lista)
    print(Fore.CYAN + """
       == Relatório de criação mensal de O.S. =""")
    print(Fore.RED+"    |OS|\t|  Técnico  |\t|Data de Abertura|")
    for i in range(0, len(lista)):
        posicao = str(lista[i])
        if(posicao[8:10]== mes):
           print(f"    |{posicao[1]} |\t|{posicao[25:-2]:<8}   |\t|{posicao[5:21]:>15}|") 

    continuar()


