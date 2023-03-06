class Timetable:
    def __init__(self, timetable, days, hours) -> None:
        '''
        Initializes timetable object
        :param timetable: this is name of the timetable
        :param days: this is how many days timetable has
        :param hours: this is how many hours each day has
        '''
        self.timetable = timetable
        self.days = days
        self.hours = hours

    def __str__(self) -> str:
        '''
        returns timetable as string
        '''
        return f'{self.timetable} with {self.days} and each day consist of {self.hours}'