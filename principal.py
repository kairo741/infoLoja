#coding: utf-8

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


# Criar tabelas
cliente.criarTabelaCliente(conexao)
user.criarTabelaUser(conexao)
servicos.criar_tabela_servicos(conexao)


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
                #Menu inicial, ir para Usuários ou OSs
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

                        # elif(opcao == "5"):
                        #     cls()
                        #     cliente.inserirCliente(conexao)
                        #     continuar()

                        # elif(opcao == "6"):
                        #     cls()
                        #     cliente.listar_cliente(conexao)
                        #     continuar()


                        #Se escolhida a opção de voltar
                        elif(opcao == "5"):
                            cls()
                            break
                        
                        #Se escolhida a opção de sair do sistema.
                        elif(opcao == "6"):
                            sair()


                        else:
                            op_invalida()

                #Se escolhida a opção 2, que entra no menu de OSs
                elif(opcao == "2"):
                    while(True):
                        cls()
                        menus.menu_os()
                        opcao = input("Insira a opção: ")

                        #Quando escolhida a opção de criar OSs
                        if(opcao == "1"):
                            cls()
                            servicos.inserir_os(conexao)
                        

                        elif(opcao == "2"):
                            cls()
                            servicos.fechar_os(conexao)
                            
                            
                        
                        #Quando escolhida a opção de Alterar OSs
                        elif(opcao == "3"):
                            cls()
                            servicos.alterar_os(conexao)

                        #Se escolhida a opção de Ler OS
                        elif(opcao == "4"):
                            cls()
                            servicos.visualizar_os()
                        

                        #Se escolhida a opção de finalizar ordem de serviço
                        elif(opcao == "5"):
                            cls()
                            servicos.finalizar_os(conexao)
                        

                        #Opção dos relatórios de OSs mensal
                        elif(opcao == "6"):
                            cls()
                            servicos.relatorio_os_mes(conexao)



                        #Opção para voltar do MENU DE OSs
                        elif(opcao == "7"):
                            break


                        #Opção para sair do sistema
                        elif(opcao == "8"):
                            sair()

                        #Se digitada uma opção inválida
                        else:
                            op_invalida()

                #Se escolhida a opção 3 que entra no menu de controle de clientes
                elif(opcao == "3"):
                    while(True):
                        cls()
                        menus.menu_cliente()
                        opcao = input("Insira a opção: ")

                        #Opção de cadastrar clientes na tabela "cliente"
                        if(opcao == "1"):
                            cls()
                            cliente.inserirCliente(conexao)

                        #Opção de listar todos os clientes cadastrados na tabela 'cliente'
                        elif(opcao == "2"):
                            cls()
                            cliente.listar_cliente(conexao)
                    

                        elif(opcao == "3"):
                            cls()
                            cliente.alterar_cliente(conexao)


                        #Opção de excluir o registro de cliente, da tabela "cliente"
                        elif(opcao == "4"):
                            cls()
                            cliente.excluir_cliente(conexao)


                        #Opção de volta ao menu anterior do sistema
                        elif(opcao == "5"):
                            break
                        
                        
                        #Opção de sair do sistema
                        elif(opcao == "6"):
                            sair()


                #Opção de sair do sistema
                elif(opcao == "4"):

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


conexao.close()
#Fim do código
