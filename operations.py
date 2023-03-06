import person

def printRootMenu():
    '''
    Prints root menu
    '''
    print('*---------------------------------*')

    print('Select option:')
    print('[1] Add person')
    print('[2] Add task')

    print('*---------------------------------*')

    print('Enter your choice [number] >>')

def handleRootMenuChoice(option):
    '''
    Handles choice made in root menu
    :param option: this is the choice made by user
    '''
    match option:
        case '1':
            createPerson()
        case '2':
            print('adding task')
        case _:
            print('not really an option, is it?')

def createPerson():
    print('Give name of the person >>')
    name = input()
    print('Give age of {name}')
    age = input()

    newPerson = person.Person(name, age)
    
    print('_______________________')
    print('Added: ', newPerson)