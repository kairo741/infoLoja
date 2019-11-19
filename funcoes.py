import sqlite3
from colorama import Fore, init, Back
import time
from os import system




#Código para semrpe resetar a cor a cada print
init(autoreset=True)




#Função para limpar cmd
def cls():
    system('cls')



#Procedimento para o login
def login(conexao):
    cursor = conexao.cursor()

    login = input("Login: ")
    senha = input("Senha: ")

    sql = """
    SELECT rowid, * FROM user 
    """
    cursor.execute(sql)

    lista = cursor.fetchall()

    confirm = 0
    for i in range (0, len(lista)):
        if(lista[i][2] == login and lista[i][3] == senha):
            print(Fore.LIGHTGREEN_EX + "Bem Vindo ao INFO LOJA {}!".format(lista[i][1]))   
            confirm = 1
            nome = lista[i][1]
            return nome        
    if(confirm == 0):
        print("Login ou Senha incorreto(s)!")

  
def sair():

    print(Fore.GREEN + "Saindo do sistema", end='', flush=True)
    for i in range(5):
        print(Fore.GREEN + '.', end='', flush=True)
        time.sleep(0.5)
    cls()
    exit()



def opcao():
    opcao = int(input("Insira a opção: "))
    return opcao


def continuar():
    continuar = input("Deseja continuar?(S/N) ")

    continuar = continuar.lower()
    if(continuar == "n"):
        sair()
    
    else:
        print()