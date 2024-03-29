import timetable
import person
import task
import utils

# init timetable

currentTimetable = timetable.Timetable('default', 7, 8, 24)
print('')

#print menu

while True:
    json = utils.getDataFromJson()
    print('[1] Add Person')
    print('[2] Add Task')
    print('[3] Create Event')
    print('[4] Show Timetable')
    print('[5] Show Persons')
    print('')

    while True:
        try:
            option = int(input('Choose action [number] >> '))
            if option not in range(1,6):
                print('Your choice needs to be between 1 and 5.')
                continue
        except ValueError:
            print('Your choice needs to be a number.')
            continue
        else:
            break

    print('')
    
    match option:
        case 1:
            print('***')
            print('ADD PERSON')
            print('***')
            print('')

            name = input('Name of the person >> ')
            age = input('Age of the person >> ')
            newperson = person.Person(name, age)

            print(newperson)

            utils.writeToJson('person', newperson.toObject())
            json = utils.getDataFromJson()

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
            json = utils.getDataFromJson()

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
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            i = 0
            for entry in days:
                print('[{}] '.format(i) + entry)
                i+=1
            print('')

            while True:
                try:
                    day = int(input('Choose day for the event [number] >> '))
                    if day not in range(0, len(days)):
                        print('You choice need to be between 0 and {}.'.format(len(days)))
                        continue
                except ValueError:
                    print('Your choice needs to be number.')
                    continue
                else:
                    break

            day = days[day]

            # set start time for event
            while True:
                try:
                    startTime = int(input('Set start time for the event [number] >> '))
                    print(currentTimetable)
                    if startTime not in range(currentTimetable.start, currentTimetable.end):
                        print('Timetable currently accept only events between {} and {}.'.format(currentTimetable.start, currentTimetable.end))
                        continue
                except ValueError:
                    print('Your choice needs to be number.')
                    continue
                else:
                    break

            # check overlaps
            timeRange = range(startTime, startTime + int(job['duration']))

            overlapping = False

            for dayEntry in json['timetable']:
                tasks = json['timetable'][dayEntry]
                for entry in tasks:
                    if entry['person']['name'] == who['name']:
                        if entry['start'] in timeRange or entry['start'] + int(entry['task']['duration']) in timeRange:
                                overlapping = True

            # add to json if no overlap
            if overlapping:
                print('Person already has another event that overlaps with this one. Cancelling this event...')
                print('')
            else:
                currentTimetable.addEvent(job, who, day, startTime)
                print('Event added to timetable.')
                print('')
            json = utils.getDataFromJson()

        case 4:
            print('***')
            print('TIMETABLE')
            print('***')
            print('')

            # get latest timetable
            json = utils.getDataFromJson()
            current = json['timetable']

            # check longest entry in task
            task_len = utils.checkMaxEntryLen(current, 'task')
            person_len = utils.checkMaxEntryLen(current, 'person')
            status_len = utils.checkMaxEntryLen(current, 'status')

            # print headers
            print(utils.printTextWithMinLen('DAY', 5), ' | ', 'START', ' | ', utils.printTextWithMinLen('TASK', task_len), ' | ', utils.printTextWithMinLen('PERSON', person_len), ' | ', utils.printTextWithMinLen('STATUS', status_len))
            print('-' * (task_len + person_len + status_len + 8)*2)

            for day in current:
                tasks = current[day]
                for entry in tasks:
                    if len(str(entry['start'])) < 2:
                        newTime = '0' + str(entry['start']) + ':00'
                    else:
                        newTime = str(entry['start']) + ':00'

                    print(utils.printTextWithMinLen(day, 2, False), ' | ', utils.printTextWithMinLen(newTime, 2, False), ' | ', utils.printTextWithMinLen(entry['task']['task'], task_len, False), ' | ', utils.printTextWithMinLen(entry['person']['name'], person_len, False), ' | ', entry['status'])

            print('')

        case 5:
            print('***')
            print('PERSONS')
            print('***')
            print('')

            json = utils.getDataFromJson()

            for ind in json['person']:
                print('{} ({})'.format(ind['name'], ind['age']))

            print('')

        case _:
            print('Not really an option, is it?')
            print('')