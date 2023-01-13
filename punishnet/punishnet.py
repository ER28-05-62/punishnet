from os import system
from colorama import Fore


from core.shell import Shell
from core.banner import BANNER, CONTACTS, SLOGAN

def banner():
    try:
        system("clear")
    except:
        print("\033[H\033[J")
        
    print(Fore.LIGHTRED_EX + BANNER)
    print(Fore.YELLOW + SLOGAN)

def contacts():
    print(Fore.LIGHTGREEN_EX + CONTACTS)

def main():
    try:
        banner()
        contacts()

        # launch panishnet
        panisher = Shell(
                        BANNER, SLOGAN, CONTACTS)
        panisher.launch_shell()
    
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
