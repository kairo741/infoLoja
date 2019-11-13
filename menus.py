from colorama import Fore, Back, init



#Código para semrpe resetar a cor a cada print
init(autoreset=True)




def menu_inicial():
    print(Fore.CYAN +"""
    ========================================""","""
    1. Controle de usuários
    2. Controle de ordem de serviços (O.S.)
    3. Sair""", Fore.CYAN + """
    ========================================""")


def menu_usuario():
    print(Fore.CYAN + """
    ========= Controle de usuários =========""","""
    1. Cadastrar usuário
    2. Excluir usuário
    3. Modificar atributo do usuário
    4. Voltar
    5. Sair""", Fore.CYAN + """
    ========================================""")

def menu_os():
    print(Fore.CYAN + """
    = Controle de ordem de serviços (O.S.) =""","""
    1. Criar ordem de serviço
    2. Alterar ordem de serviço
    3. Ler ordem de serviço
    4. Imprimir ordem de serviço
    5. Voltar
    6. Sair""", Fore.CYAN + """
    ========================================""")
