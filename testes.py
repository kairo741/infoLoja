from colorama import Fore, Back, Style, init



init(autoreset= True)

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.NORMAL  + 'and in dim text')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
print(Fore.BLUE + 'Kairo bonito', Fore.RESET)
print(Fore.BLACK + 'Kairo bonito', Fore.RESET)
print(Fore.RED + 'Kairo bonito'+ Fore.RESET)
