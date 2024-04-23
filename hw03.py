from sys import argv
from pathlib import Path


def tree(folder: str, depth: int = 0) -> None:
    path = Path(folder)

    if path.exists() and path.is_dir():
        if depth == 0:
            print('📦', path.absolute().name, sep='')

        groups = {True: [], False: []}
        count = 0

        for item in path.iterdir():
            groups[item.is_dir()].append(item.name)
            count += 1

        for is_dir, items in groups.items():
            for item in sorted(items):
                count -= 1

                print('┃ ' * depth,
                      '┣ ' if count else '┗ ',
                      '📂' if is_dir else '📜',
                      item,
                      sep='')

                if is_dir:
                    tree(f'{folder}/{item}', depth + 1)

def main() -> None:
    tree(argv[1] if len(argv) > 1 else '.')


if __name__ == '__main__':
    main()
