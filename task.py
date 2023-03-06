class Task:
    def __init__(self, task, amount, person) -> None:

        '''
        Initializes Task object
        :param task: this is name of the task
        :param amount: this is time amount for the task
        :param person: this is person to whom the task is assigned to
        '''
        
        self.task = task
        self.amount = amount
        self.person = person

    def __str__(self) -> str:
        '''
        returns task as string
        '''
        return f'{self.task}, {self.amount} hours, assigned to {self.person}'