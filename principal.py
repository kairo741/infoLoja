import sqlite3

# Import dos Meus Arquivos
import user
import menus
import funcoes
import cliente
import servicos
from funcoes import cls
from funcoes import sair, opcao, continuar, op_invalida

# Conexao ao Banco
conexao = sqlite3.connect("infoLoja.sqlite")


while(True):
    cls()
    menus.menu_login()
    opcao = input("Insira a opção: ")

    # Se escolhida a opção 1: Logar no sistema
    if(opcao == "1"):
        cls()
        #Logando no sistema
        login = funcoes.login(conexao)
        if(login == 1):

            while(True):
                cls()
                #Menu inicial, ir para Usuários ou O.S.s
                menus.menu_inicial()
                opcao = input("Insira a opção: ")

                if(opcao == "1"):
                    while(True):
                        cls()
                        #Entrando no menu usuário
                        menus.menu_usuario()
                        opcao = input("Insira a opção: ")
                        
                        #Escolhida a opção que entra no menu de cdastro de usuário
                        if(opcao == "1"):
                            cls()
                            user.inserirUser(conexao)
                            continuar()


                        #Escolhida a opção que entra no menu de Exclusão de usuário
                        elif(opcao == "2"):
                            cls()
                            user.excluir_usuario(conexao)
                            continuar()
                        
                        #Escolhida a opção que entra no menu de alterar dados do usuário de usuário
                        elif(opcao == "3"):
                            cls()
                            user.update_usuario(conexao)
                            continuar()

                        #Escolhida a opção que entra no menu de listar usuários
                        elif(opcao == "4"):
                            cls()
                            user.listar_user(conexao)
                            continuar()

                        #Se escolhida a opção de voltar
                        elif(opcao == "5"):
                            cls()
                            break
                        
                        #Se escolhida a opção de sair do sistema.
                        elif(opcao == "6"):
                            sair()


                        else:
                            op_invalida()

                elif(opcao == "2"):
                    while(True):
                        cls()
                        menus.menu_os()
                        opcao = input("Insira a opção: ")

                elif(opcao == "3"):

                    sair()

                else:
                   op_invalida()
    


    # Se escolhida a opção 2: Criar conta
    elif(opcao == "2"):
        cls()
        user.inserirUser(conexao)
        continuar()
    # Se escolhida a opção 3: Sair do sistema
    elif(opcao == "3"):
        sair()

    # Se digitado qualquer outro número
    else:
        print("Opção inválida!")
        continuar()


# Criar tabelas
# cliente.criarTabelaCliente(conexao)
# user.criarTabelaUser(conexao)
# servicos.criar_tabela_servicos(conexao)

conexao.close()
