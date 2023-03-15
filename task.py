import parent

class Task(parent.Parent):
    def __init__(self, name, time_allocation, desc):

        '''
        Initializes Task object
        :param name: this is name of the task
        :param time_allocation: this is time it takes for to finish the task
        :param desc: this is description of the the task
        '''

        self.name = name

        super().__init__(time_allocation, desc)
        self.time_allocation = time_allocation
        self.desc = desc

    def __str__(self) -> str:

        '''
        returns task as string
        '''

        return f'{self.name}, {self.desc}, {self.time_allocation} hours'
    
    def toObject(self):

        '''
        Returns object version of the task
        '''
        
        object = {
            "task": self.name,
            "description": self.desc,
            "duration": self.time_allocation
        }
        
        return object
    
    def getDescription(self):

        '''
        Returns description of the task.
        '''

        return self.desc
    
    def setDescription(self, desc):

        '''
        Sets new description to the task.
        :param desc: this is description of the the task
        '''
        
        self.desc = desc
