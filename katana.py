import sys
import collections

from core.notify import Notify


class Katana:
    def __init__(self):

        arg_names = ['title', 'message', 'app_name', 'app_icon']        

        # x, y, z e w são os parametros informados 

        # Cria um dicionario de chave/valor ex: {title=x, message=y, app_name=z, app_icon=w}
        args = dict(zip(arg_names, sys.argv[1:]))

        # Cria uma lista do dicionario anterior ex: data(title=x, message=y, app_name=z, app_icon=w)
        arg_list = collections.namedtuple('data', arg_names) 

        # Percorre cada parabetro e atribui um valor default caso esteja sem valor, ex: data(title='', message='', app_name='', app_icon='')
        args =  arg_list(*(args.get(arg, "") for arg in arg_names))  

        self.title = args.title or "Katana"
        self.message = args.message or "Hello World from Katana"
        self.app_name = args.app_name or "Katana"
        self.app_icon = args.app_name or "./assets/katana-logo.svg"

    def notify(self):
        Notify().doNotify(self.title, self.message, self.app_name, self.app_icon)    


def main():
    Katana().notify()

if __name__ == "__main__":
    main()     
    
