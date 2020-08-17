import sys
import collections

from core.notify import Notify


class Katana:
    def __init__(self):

        arg_names = ['title', 'message', 'app_name', 'app_icon']
        args = collections.namedtuple('data', arg_names)(
            *(dict(zip(arg_names, sys.argv[1:])).get(arg, "") for arg in arg_names))

        self.title = args.title if args.title else "Katana"
        self.message = args.message if args.message else "Hello World from Katana"
        self.app_name = args.app_name if args.app_name else "Katana"
        self.app_icon = args.app_name if args.app_name else "./assets/katana-logo.svg"

    def notify(self):
        Notify().doNotify(self.title, self.message, self.app_name, self.app_icon)    


def main():
    Katana().notify()

if __name__ == "__main__":
    main()     
    