import sys
from pathlib import Path
from hw4_3 import get_directory_contents


def main():
    user_input = ''
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    path = Path(user_input)
    if path.exists():
        if path.is_dir():
            get_directory_contents(path)
        else:
            print(f'{user_input} isn\'t directory')
    else:
        print(f'{path.absolute()} isn\'t exists')


if __name__ == '__main__':
    main()