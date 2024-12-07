import sys
from pathlib import Path
from colorama import Fore, Style, init


init(autoreset=True)

def visualize_directory_structure(directory_path: str):
    try:
        path = Path(directory_path)

      
        if not path.exists():
            print(Fore.RED + "Помилка: Шлях не існує.")
            return
        if not path.is_dir():
            print(Fore.RED + "Помилка: Вказаний шлях не є директорією.")
            return

        print(f"Структура директорії для: {Fore.YELLOW}{directory_path}\n")

       
        def walk_dir(current_path: Path, prefix: str = ""):
            for item in current_path.iterdir():
                if item.is_dir():
                    print(f"{prefix}{Fore.BLUE} {item.name}")
                    walk_dir(item, prefix + "  ")  
                else:
                    print(f"{prefix}{Fore.GREEN}- {item.name}")

        walk_dir(path)

    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")

if __name__ == "__main__":
  
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: Будь ласка, вкажіть шлях до директорії як аргумент. Наприклад python '3.py ./picture'")
    else:
        directory_path = sys.argv[1]
        visualize_directory_structure(directory_path)
