class Timetable:
    def __init__(self, timetable, days, start, end) -> None:
        '''
        Initializes timetable object
        :param timetable: this is name of the timetable
        :param days: this is how many days timetable has
        :param start: this is when day starts in hours
        :param end: this is when day ends in hours
        '''
        self.timetable = timetable
        self.days = days
        self.start = start
        self.end = end

    def __str__(self) -> str:
        '''
        returns timetable as string
        '''
        return f'{self.timetable} with {self.days} and each day has timeslots between {self.start} - {self.end}.'