import person
import timetable

def initializeTimetable(name, days, start, end):

    '''
    Initializes timetable
    :param timetable: this is name of the timetable
    :param days: this is how many days timetable has
    :param start: this is when day starts in hours
    :param end: this is when day ends in hours
    '''
    
    newTimetable = timetable.Timetable(name, days, start, end)
    print(newTimetable)

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
            createTask()
        case _:
            print('not really an option, is it?')

def createPerson():

    '''
    Creates person with user input
    '''

    print('Give name of the person >>')
    name = input()
    print('Give age of {name}')
    age = input()

    newPerson = person.Person(name, age)
    
    print('_______________________')
    print('Added: ', newPerson)

def createTask():

    '''
    Creates task with user input
    name: name of the task
    desc: description of the task
    '''

    print('Give name to the task >>')
    name = input()
    print('Give description for the task >>')
    desc = input()

    print('_______________________')
    print('Create task:')
    print(name)
    print(desc)