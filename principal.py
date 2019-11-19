import sqlite3

# Import dos Meus Arquivos
import user
import menus
import funcoes
import cliente
import servicos
from funcoes import cls
from funcoes import sair
from funcoes import opcao
from funcoes import continuar


#Conexao ao Banco
conexao = sqlite3.connect("infoLoja.sqlite")


while(True):
    cls()
    menus.menu_login()
    opcao = int(input("Insira a opção: "))
    
    #Se escolhida a opção 1: Logar no sistema
    if(opcao == 1):
        cls()
        login = funcoes.login(conexao)
        cls()
        menus.menu_inicial()
        


    #Se escolhida a opção 2: Criar conta
    elif(opcao == 2):    
        cls()
        user.inserirUser(conexao)



    #Se escolhida a opção 3: Sair do sistema
    elif(opcao == 3):
        sair()


    #Se digitado qualquer outro número
    else:
        print("Opção inválida!")
        continuar()













# Criar tabelas
# cliente.criarTabelaCliente(conexao)
# user.criarTabelaUser(conexao)
# servicos.criar_tabela_servicos(conexao)

conexao.close()

