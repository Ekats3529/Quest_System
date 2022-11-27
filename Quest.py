class Quest:
    status = "disable"
    name = None
    description = None

    def __init__(self, name):
        self.name = name

    def change_status(self, status):
        self.status = status



