class DataBase:
    def __init__(self):
        self.users = []
        self.tasks = []
    
    def clear_all(self):
        self.users.clear()
        self.tasks.clear()

db = DataBase()