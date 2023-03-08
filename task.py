class Task:
    def __init__(self, task, amount, desc) -> None:

        '''
        Initializes Task object
        :param task: this is name of the task
        :param amount: this is time amount for the task
        :param desc: this is description of the the task
        '''

        self.task = task
        self.amount = amount
        self.desc = desc

    def __str__(self) -> str:

        '''
        returns task as string
        '''

        return f'{self.task}, {self.desc}, {self.amount} hours'
    
    def toObject(self):

        '''
        Returns object version of the task
        '''
        
        object = {
            "task": self.task,
            "description": self.desc,
            "duration": self.amount
            }
        return object
