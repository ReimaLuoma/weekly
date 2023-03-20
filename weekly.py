import timetable
import person
import task
import utils

# read data from json

json = utils.getDataFromJson()

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
    print('')
    
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

            # choosing of task
            print('Tasks:')
            if(json['task']):
                for i in range(len(json['task'])):
                    print('[{}] '.format(i) + json['task'][i]['task'])

            print('')
            job = input('Select task from the list above [number] >> ')
            job = int(job)
            job = json['task'][job]
            print('')

            # choosing of person
            print('Persons:')
            if(json['person']):
                for i in range(len(json['person'])):
                    print('[{}] '.format(i) + json['person'][i]['name'])

            print('')
            who = input('Assign person to this event [number] >> ')
            who = int(who)
            who = json['person'][who]
            print('')

            # set day for event
            day = input('Choose day for the event [number] >> ')

            # set start time for event
            startTime = input('Set start time for the event [number]')
            startTime = int(startTime)

            # check overlaps

            # add to json
            newEvent = currentTimetable.addEvent(job, who, day, startTime)
            utils.writeToJson('timetable', newEvent)

        case 4:
            print('***')
            print('TIMETABLE')
            print('***')
            print('')

            # get latest timetable
            json = utils.getDataFromJson()
            currentTimetable = json['timetable']

            # check longest entry in task
            task_len = utils.checkMaxEntryLen(currentTimetable, 'task')
            person_len = utils.checkMaxEntryLen(currentTimetable, 'person')
            status_len = utils.checkMaxEntryLen(currentTimetable, 'status')

            print('START', ' | ', utils.printTextWithMinLen('TASK', task_len), ' | ', utils.printTextWithMinLen('PERSON', person_len), ' | ', utils.printTextWithMinLen('STATUS', status_len))
            for event in currentTimetable:
                print(event['start'], ':00', ' | ', event['task']['task'], ' | ', event['person']['name'], ' | ', event['status'])
            
            print('')

        case _:
            print('Not really an option, is it?')
            print('')