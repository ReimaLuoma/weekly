import operations

operations.printRootMenu()

option = input()

match option:
    case '1':
        print('adding person')
    case '2':
        print('adding task')
    case _:
        print('not really an option, is it?')