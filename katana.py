import sys
import collections

from core.notify import Notify

def main():
    arg_names = ['title', 'message', 'app_name', 'app_icon']

    args = collections.namedtuple('data', arg_names)(
        *(dict(zip(arg_names, sys.argv[1:])).get(arg, "") for arg in arg_names))

    TITLE = args.title if args.title else "Katana"
    MESSAGE = args.message if args.message else "Hello World from Katana"
    APP_NAME = args.app_name if args.app_name else "Katana"
    APP_ICON = args.app_name if args.app_name else "./assets/katana-logo.svg"

    Notify().doNotify(TITLE, MESSAGE, APP_NAME, APP_ICON)
    

if __name__ == "__main__":
    main()