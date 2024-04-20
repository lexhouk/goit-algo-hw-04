def total_salary(path: str) -> tuple:
    '''
    Get the total and average salary of employees which are read from a file.

    :param path: string

    :return: tuple
    '''

    salaries = []

    try:
        with open(path, encoding='utf-8') as file:
            for emploee in file.readlines():
                if emploee.strip():
                    try:
                        _, salary = emploee.split(',')
                        salaries.append(int(salary))
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f'File {path} not found!')

    return sum(salaries), sum(salaries) / len(salaries) if salaries else (0, 0)
