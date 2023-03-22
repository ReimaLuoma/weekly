import parent
import json

class Timetable(parent.Parent):
    def __init__(self, name, days: int = 7, start: int = 8, end: int = 24):

        '''
        Initializes timetable object
        :param name: this is name of the timetable
        :param days: this is how many days timetable has (default is 7 days)
        :param start: this is when day starts in hours (default is 8)
        :param end: this is when day ends in hours (default is 24)
        '''

        super().__init__(name)
        self.days = days
        self.start = start
        self.end = end

    def __str__(self) -> str:

        '''
        returns timetable as string
        '''
        
        return f'{self.name} timetable with {self.days} days and each day has timeslots between {self.start} - {self.end}.'
    
    def addEvent(self, task, person, day, start_time):
         
         '''
         Adds event to timetable in json.
         :param task: this is the task to add as event to timetable
         :param person: who is the task assigned to
         :param day: this is the day the task is set to [int]
         :param start_time: this is start time of the task
         '''

         object = {
             "task": task,
             "person": person,
             "start": start_time,
             "status": "wip"
         }

         filename = 'data.json'

         # open file and read
         with open(filename, 'r') as file:
             data = json.load(file)

         # add new data to correct level
         data['timetable'][day].append(object)

         # overwrite with new data
         with open(filename, 'w') as file:
             json.dump(data, file)

    def eventFinished(event):
        event.status = 'done'

