class Person:
    def __init__(self, name) -> None:
        '''
        Initializes Person object
        :param name: this is name of the person
        '''
        self.name = name

    def __str__(self) -> str:
        '''
        returns person as string
        '''
        return f'{self.name}'