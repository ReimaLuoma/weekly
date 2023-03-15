import parent
import utils

class Timetable(parent.Parent):
    def __init__(self, name, days: int = 7, start: int = 8, end: int = 24):

        '''
        Initializes timetable object
        :param name: this is name of the timetable
        :param days: this is how many days timetable has (default is 7 days)
        :param start: this is when day starts in hours (default is 8)
        :param end: this is when day ends in hours (default is 24)
        '''

        self.name = name
        super().__init__(days, start, end)
        self.days = days
        self.start = start
        self.end = end

    def __str__(self) -> str:

        '''
        returns timetable as string
        '''
        
        return f'{self.timetable} timetable with {self.days} days and each day has timeslots between {self.start} - {self.end}.'
    
    def addEvent(task, day, start_time):
         
         '''
         Adds event to timetable based on given task.
         :param task: this is the task to add as event to timetable
         :param day: this is the day the task is set to [int]
         :param start_time: this is start time of the task
         '''

         object = {
             "task": task,
             "day": day,
             "start": start_time,
             "status": "wip"
         }

         utils.writeToJson("timetable", object)

    def eventFinished(event):
        event.status = 'done'

