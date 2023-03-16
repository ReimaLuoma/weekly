import timetable
import person
import task
import utils

# read data from json

json = utils.getDataFromJson()
print(json)

# init timetable

currentTimetable = timetable.Timetable('default', 7, 8, 24)
print(currentTimetable)

#print menu

while True:
    print('[1] Add Person')
    print('[2] Add Task')
    print('[3] Create Event')
    print('[4] Show Timetable')
    option = input('Choose action [number] >> ')
    option = int(option)
    
    match option:
        case 1:
            print('***')
            print('CREATE PERSON')
            print('***')
            print('')

            name = input('Name of the person >> ')
            age = input('Age of the person >> ')
            newperson = person.Person(name, age)

            print(newperson)

            utils.writeToJson('person', newperson.toObject())

            print('')
            print('***')

        case 2:
            print('***')
            print('CREATE TASK')
            print('***')
            print('')

            name = input('Name of the task >> ')
            time = input('Time it takes to finish the task >> ')
            desc = input('Describe the task at hand >> ')
            newTask = task.Task(name, time, desc)

            print(newTask)

            utils.writeToJson('task', newTask.toObject())

            print('')
            print('***')

        case 3:
            print('***')
            print('CREATE EVENT TO TIMETABLE')
            print('***')
            print('')

            job = input('Select task from the list above [number] >> ')

            currentTimetable.addEvent(job, who, day, startTime)