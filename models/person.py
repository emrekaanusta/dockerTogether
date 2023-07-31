class Person:
    name: str
    isAdmin: int
    project: str
    username: str

    def __init__(self, name, isAdmin, project, username):
        self.name = name
        self.isAdmin = isAdmin
        self.project = project
        self.username = username
