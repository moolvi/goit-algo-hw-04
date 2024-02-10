from pathlib import Path 
from colorama import Back

def get_directory_contents(path_directory: Path):
    print(Back.BLUE + path_directory.name + Back.WHITE)
    __view_catalog(path_directory)

def __view_catalog(path_directory: Path, i = 1):
    tab = '    ' * i
    for path in path_directory.iterdir():
        if path.is_dir():
            print(Back.BLUE + (tab + path.name) + Back.WHITE)
            __view_catalog(path, i + 1)
        else:
            print((tab + path.name) + Back.WHITE)