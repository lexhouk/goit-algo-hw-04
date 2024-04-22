def get_cats_info(path: str) -> list[dict]:
    '''
    Read cats' data from a file.

    :param path: string

    :return: list[dict]
    '''

    cats = []

    try:
        with open(path, encoding='utf-8') as file:
            for cat in file.readlines():
                if cat.strip():
                    try:
                        id, name, age = [value.strip() for value in cat.split(',', 3)]
                        age = int(age)

                        if id and name and age > 0:
                            cats.append({
                                'id': id,
                                'name': name.capitalize(),
                                'age': age
                            })
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f'File {path} not found!')

    return cats
