import person
import timetable
import task
import utils

taskList = []
personList = []

#Person

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

#Task

def createTask():

    '''
    Creates task with user input
    name: name of the task
    desc: description of the task
    '''

    name = input('Give name to the task >>')
    desc = input('Give description for the task >>')
    amount = input('Give how long this task is going to take ([number] hours) >>')

    print('_______________________')
    print('Create task:')
    print(name)
    print(desc)

    newTask = task.Task(name, amount, desc).toObject()
    print(type(newTask))

    taskList.append(newTask)
    utils.writeToJson('tasks', newTask)

def modifyTask():
    print('*** MODIFY TASK ***')
    print('')

    for i in range (len(taskList)):
        print(i, task)
    option = input('Choose Task for modifying [number] >>')  

#Timetable

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

#General

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

    option = input('Choose Task for modifying [number] >>')
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

def timetableMenu():
    
    '''
    Returns menu for timetable management
    '''

    print('*** TIMETABLE MENU ***')

def taskMenu():

    '''
    Returns menu for task management
    '''

    utils.generateSubMenu('Task')
    option = input()
    handleTaskMenuChoice(option)

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

    utils.generateSubMenu('Person')
    option = input()

createTask()