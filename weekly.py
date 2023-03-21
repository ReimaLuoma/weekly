import timetable
import person
import task
import utils

# read data from json

json = utils.getDataFromJson()

# init timetable

currentTimetable = timetable.Timetable('default', 7, 8, 24)
print(currentTimetable)
print('')

#print menu

while True:
    print('[1] Add Person')
    print('[2] Add Task')
    print('[3] Create Event')
    print('[4] Show Timetable')
    print('')
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
            timeRange = range(startTime, int(job['duration']))

            overlapping = False

            for event in json['timetable']:
                if event['person'] == who:
                    if event['day'] == day:
                        if event['start'] in timeRange:
                            if event['start'] + event['task']['duration'] in timeRange:
                                overlapping = True

            # add to json if no overlap
            print(overlapping)
            if overlapping:
                print('Person already has another event that overlaps with this one. Cancelling this event...')
                print('')
            else:
                print('Person already has another event that overlaps with this one. Cancelling this event...')
                print('')
                newEvent = currentTimetable.addEvent(job, who, day, startTime)
                utils.writeToJson('timetable', newEvent)
                print('Event added to timetable.')
                print('')

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
            print('-' * (task_len + person_len + status_len + 3)*2)
            for event in currentTimetable:

                if len(str(event['start'])) < 2:
                    newTime = '0' + str(event['start']) + ':00'
                else:
                    newTime = str(event['start']) + ':00'

                print(utils.printTextWithMinLen(newTime, 4, False), ' | ', utils.printTextWithMinLen(event['task']['task'], 5, False), ' | ', utils.printTextWithMinLen(event['person']['name'], 7, False), ' | ', event['status'])
            
            print('')

        case _:
            print('Not really an option, is it?')
            print('')