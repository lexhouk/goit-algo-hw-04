def parse_input(user_input: str) -> list[str]:
    cmd, *args = user_input.split()
    return cmd.strip().lower(), *args

def add_contact(args: list[str], contacts: dict) -> str:
    name, phone = args

    if contacts.get(name) is not None:
        return 'Contact is already added!'
    
    contacts[name] = phone
    
    return 'Contact added.'

def change_contact(args: list[str], contacts: dict) -> str:
    name, phone = args

    if contacts.get(name) is None:
        return 'Contact is absent!'
    
    contacts[name] = phone

    return 'Contact updated.'

def show_phone(args: list[str], contacts: dict) -> str:
    return contacts.get(args[0]) or 'Name not found!'

def show_all(contacts: dict) -> str:
    def divider(left: str, right: str, middle: str, cell: str = '═'):
        return left + cell * (longest_name + 2) + middle + cell * \
            (longest_phone + 2) + right

    def row() -> str:
        right = ' ' * (longest_name - len(name) + 1)
        left = ' ' * (longest_phone - len(phone) + 1)
        return f'║ {name}{right}│{left}{phone} ║'
    
    if not contacts:
        return 'Contacts list is empty!'
    
    name, phone = 'Full name', 'Phone number'
    longest_name = max([len(name) for name in contacts.keys()])
    longest_phone = max([len(phone) for phone in contacts.values()])

    if longest_name < len(name):
        longest_name = len(name)

    if longest_phone < len(phone):
        longest_phone = len(phone)

    rows = [divider('╔', '╗', '╤'), row(), divider('╟', '╢', '┼', '─')]

    for name, phone in contacts.items():
        rows.append(row())

    rows.append(divider('╚', '╝', '╧'))
    
    return '\n'.join(rows)

def main() -> None:
    contacts = {}

    print('Welcome to the assistant bot!')
    
    while True:
        command, *args = parse_input(input('Enter a command: '))

        match command:
            case 'hello': print('How can I help you?')
            case 'add': print(add_contact(args, contacts))
            case 'change': print(change_contact(args, contacts))
            case 'phone': print(show_phone(args, contacts))
            case 'all': print(show_all(contacts))
            case _ if command in ['close', 'exit']:
                print('Good bye!')
                break
            case _: print('Invalid command.')

if __name__ == '__main__':
    main()
