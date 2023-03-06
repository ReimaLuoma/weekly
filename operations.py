import person
import timetable
import task

taskList = []
personList = []

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
    print('[1] Timetable')
    print('[2] Tasks')
    print('[3] Persons')

    print('*---------------------------------*')

    print('Enter your choice [number] >>')
    option = input()
    handleRootMenuChoice(option)

def handleRootMenuChoice(option):

    '''
    Handles choice made in root menu
    :param option: this is the choice made by user
    '''

    match option:
        case '1':
            timetableMenu()
        case '2':
            taskMenu()
        case '3':
            personsMenu()
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

def addToPersonList(person):

    '''
    Adds person to person list
    :param person: this is the person to add to the list
    '''

    personList.append(person)
    personList.sort()

def addToTaskList(task):

    '''
    Adds task to task list
    :param task: this is the task to add to the list
    '''

    taskList.append(task)
    taskList.sort()

def timetableMenu():
    
    '''
    Returns menu for timetable management
    '''

    print('*** TIMETABLE MENU ***')

def taskMenu():

    '''
    Returns menu for task management
    '''

    print('*** TASK MENU ***')
    print('')

    print('Choose action:')
    print ('[1] Add Task')
    print ('[2] Modify Task')
    print ('[3] Remove Task')
    print ('[4] Show Tasks')
    print ('[5] MAIN MENU')

    print('')
    print('choose action [number] >>')
    option = input()

    handleTaskMenuChoice(option)

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
    print('Give how long this task is going to take ([number] hours) >>')
    amount = input()

    print('_______________________')
    print('Create task:')
    print(name)
    print(desc)

    newTask = task.Task(name, amount, desc)

    addToTaskList(newTask)
    print(newTask)

def modifyTask():
    print('*** MODIFY TASK ***')
    print('')

    i = 1

    for task in taskList:
        print('[{i}]',task.task)
        i+1

def handleTaskMenuChoice(option):

    '''
    Handles choice made in task menu
    :param option: this is the choice made by user
    '''

    match option:
        case '1':
            createTask()
        case '2':
            modifyTask()
        case '3':
            print('to remove task')
        case '4':
            print('to show tasks')
        case '5':
            printRootMenu()
        case _:
            print('not really an option, is it?')

def personsMenu():

    '''
    Returns manu for person management
    '''

    print('*** PERSON MENU ***')
    print('')

    print('Choose action:')
    print ('[1] Add Person')
    print ('[2] Modify Person')
    print ('[3] Remove Person')
    print ('[4] Show Persons')
    print ('[5] MAIN MENU')