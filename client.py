import os
from colorama import Fore, Back, Style, init
import pyfiglet

# Initialiser Colorama
init(autoreset=True)

def print_header():
    # Texte en grand avec pyfiglet
    ascii_banner = pyfiglet.figlet_format("Search 2K25", font="slant")
    print(Fore.CYAN + ascii_banner)
    print(Fore.YELLOW + "----------------------------")
    print(Fore.GREEN + "Bienvenue dans le search 2K25 !")
    print(Fore.YELLOW + "----------------------------\n")

def search_in_db(pseudo):

    db_folder = 'database/'
    

    files = [f for f in os.listdir(db_folder) if f.endswith('.txt')]
    
    print(Fore.YELLOW + f"Recherche du pseudo : {pseudo}...\n")
    
    found = False
    
    for file_name in files:
        file_path = os.path.join(db_folder, file_name)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                
                for line in lines:
                    if pseudo.lower() in line.lower():
                        print(Fore.GREEN + f"** Trouvé dans {file_name} **")
                        print(Fore.CYAN + f"  {line.strip()}")
                        found = True
                        break
        except UnicodeDecodeError:
            print(Fore.RED + f"Erreur d'encodage pour le fichier {file_name}.")
    
    if not found:
        print(Fore.RED + "Aucune correspondance trouvée.")

def main():
    print_header()

    pseudo = input(Fore.MAGENTA + "Entrez le pseudo de la personne à rechercher : ")
    search_in_db(pseudo)

if __name__ == "__main__":
    main()
