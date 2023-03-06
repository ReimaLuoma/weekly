class Task:
    def __init__(self, task) -> None:
        '''
        Initializes Task object
        :param task: this is name of the task
        '''
        self.task = task

    def __str__(self) -> str:
        '''
        returns task as string
        '''
        return f'{self.task}'