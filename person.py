class Person:
    def __init__(self, name, age) -> None:

        '''
        Initializes Person object
        :param name: this is name of the person
        :param age: this is how old the person is
        '''
        
        self.name = name
        self.age = age

    def __str__(self) -> str:

        '''
        returns person as string
        '''
        
        return f'{self.name} ({self.age})'