import platform
from core.notify import Notify

def main():
    Notify().doNotify("Katana", "Hello World from Katana", "Katana", "./assets/katana-logo." + ('ico' if platform.system() == 'Windows' else 'png') )
    

if __name__ == "__main__":
    main()