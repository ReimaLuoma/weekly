class Parent:
    def __init__(self, name = 'default') -> None:
        
        '''
        Initialize Parent object
        '''
        self.name = name

    def getName(self):

        '''
        Return the name of the object.
        '''

        return self.name
    
    def setName(self, name):

        '''
        Set name of the object.
        :param name: the name to set to the object [str]
        '''

        self.name = name

    def toObject(self):

        '''
        Return item in object form.
        '''

        object = {self}
        return object