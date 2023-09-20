class Todo():
    def __init__(self, task):
        if type(task) != str:
            raise TypeError('Task must be a string')
        elif task.strip() == '':
            raise ValueError('Task cannot be empty')
        self.task = task
        self.complete = False
    
    def mark_complete(self):
        self.complete = True
    
    def format_string(self):
        return f'{self.task} : {"complete" if self.complete else "incomplete"}'