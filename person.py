import parent

class Person(parent.Parent):
    def __init__(self, name, age: int):

        '''
        Initializes Person object
        :param name: this is name of the person
        :param age: this is how old the person is [int]
        '''
        
        super().__init__(name)
        self.age = age

    def __str__(self) -> str:

        '''
        returns person as string
        '''
        
        return f'{self.name} ({self.age})'
    
    def getAge(self):

        '''
        Returns age of the person.
        '''

        return self.age
    
    def setAge(self, age:int):

        '''
        Set age of the person.
        :param age: the age to be set on person [int]
        '''

        self.age = age

    def toObject(self):

        '''
        Returns person in object form.
        '''

        object = {
            "name": self.name,
            "age": self.age
        }

        return object