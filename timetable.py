class Timetable:
    def __init__(self, timetable) -> None:
        '''
        Initializes timetable object
        :param timetable: this is name of the timetable
        '''
        self.timetable = timetable

    def __str__(self) -> str:
        '''
        returns timetable as string
        '''
        return f'{self.timetable}'