class Parent:
    def __init__(self, name = 'default') -> None:
        
        '''
        Initialize Parent object
        '''
        self.name = name

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name