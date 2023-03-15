import parent

class Person(parent.Parent):
    def __init__(self, name, age):

        '''
        Initializes Person object
        :param name: this is name of the person
        :param age: this is how old the person is
        '''
        self.name = name
        
        super().__init__(name, age)
        self.age = age

    def __str__(self) -> str:

        '''
        returns person as string
        '''
        
        return f'{self.name} ({self.age})'
    
    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age