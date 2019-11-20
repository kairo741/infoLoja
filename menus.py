from colorama import Fore, Back, init



#Código para semrpe resetar a cor a cada print
init(autoreset=True)


def menu_login():
    print(Fore.CYAN + """
    =============== InfoLoja ===============""", """
    1. Entrar
    2. Criar conta
    3. Sair""", Fore.CYAN + """
    ========================================""")




def menu_inicial():
    print(Fore.CYAN +"""
    ======== Bem Vindo ao InfoLoja! ========""","""
    1. Controle de usuários
    2. Controle de ordem de serviços (O.S.)
    3. Sair""", Fore.CYAN + """
    ========================================""")


def menu_usuario():
    print(Fore.CYAN + """
    ========= Controle de usuários =========""","""
    1. Cadastrar usuário
    2. Excluir usuário
    3. Alterar usuário
    4. Listar usuários
    5. Voltar
    6. Sair""", Fore.CYAN + """
    ========================================""")

def menu_os():
    print(Fore.CYAN + """
    = Controle de ordem de serviços (O.S.) =""","""
    1. Criar ordem de serviço
    2. Alterar ordem de serviço
    3. Ler ordem de serviço
    4. Finalizar ordem de serviço
    5. Relatório de ordem de serviços criadas no mês
    6. Voltar
    7. Sair""", Fore.CYAN + """
    ========================================""")
