import platform, os


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
