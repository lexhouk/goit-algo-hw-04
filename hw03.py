from sys import argv
from pathlib import Path
from colorama import Back, Fore, Style


def tree(folder: str, depth: int = 0) -> None:
    '''
    Display nested files and files recursively.

    :param folder: string
    :param depth: integer

    :return: None
    '''

    path = Path(folder)

    if path.exists() and path.is_dir():
        # Show the selected folder with a special icon.
        if depth == 0:
            print(Back.BLACK, '📦', Fore.GREEN, path.absolute().name, sep='')

        groups = {True: [], False: []}
        count = 0

        # Split files and folders to separate lists to be able to show the
        # second ones before the first ones.
        for item in path.iterdir():
            groups[item.is_dir()].append(item.name)
            count += 1

        for is_dir, items in groups.items():
            for item in sorted(items):
                count -= 1

                print(Back.BLACK,
                      Fore.WHITE,
                      '┃ ' * depth,
                      '┣ ' if count else '┗ ',
                      '📂' if is_dir else '📜',
                      Fore.GREEN if is_dir else Fore.YELLOW,
                      item,
                      sep='')

                if is_dir:
                    tree(f'{folder}/{item}', depth + 1)
    else:
        print(f'{Back.BLACK}{Fore.RED}{folder} is absent or it is a file.')
    
    print(Style.RESET_ALL, end='')

def main() -> None:
    tree(argv[1] if len(argv) > 1 else '.')


if __name__ == '__main__':
    main()
