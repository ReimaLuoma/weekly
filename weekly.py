print('*---------------------------------*')

print('Select option:')
print('[1] Add person')
print('[2] Add task')

print('*---------------------------------*')

print('Enter your choice [number] >>')

option = input()

match option:
    case '1':
        print('adding person')
    case '2':
        print('adding task')
    case _:
        print('not really an option, is it?')