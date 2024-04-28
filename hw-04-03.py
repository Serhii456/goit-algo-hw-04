import sys
from colorama import Fore, Style
from pathlib import Path

def display_directory_structure(directory_path, indentation=''):
    directory = Path(directory_path)
    try:
        for entry in directory.iterdir():
            if entry.is_dir():
                print (f"{Fore.BLUE}{indentation}{entry.name}{Style.RESET_ALL}")
                display_directory_structure(entry, indentation + '    ')
            else:
                print(f"{Fore.GREEN}{indentation}{entry.name}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(Fore.RED + "Директорія не існує.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Використання: python script.py /шлях/до/директорії")
        sys.exit(1)

    directory_path = sys.argv[1]
    display_directory_structure(directory_path)

if __name__ == "__main__":
    main()
