from colorama import init, Fore
import datetime

init(autoreset=True)

def green(module, text):
    print(Fore.GREEN + f"[{datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')}] {module} | {text}")

def yellow(module, text):
    print(Fore.YELLOW + f"[{datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')}] {module} | {text}")

def red(module, text):
    print(Fore.RED + f"[{datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')}] {module} | {text}")

def white(module, text):
    print(Fore.WHITE + f"[{datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')}] {module} | {text}")

def log(module, text):
    print(Fore.BLUE + f"[{datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')}] {module} | Debug: {text}")