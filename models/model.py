class projectService:
    

    def __init__(self):
        self.name = None
        self.description = None
        self.project = None
    

    def read_project(self):
        for p in self.collection.find():
            print(p)

    def create_project(self,name, description, project):
        if name is None or project is None:
            print("Name and Project cannot be NULL")
            return __name__()
        elif description == "":
            self.db.projects.insert_one({"name": name, "desc": "", "project": project})
        else:
            self.db.projects.insert_one({"name": name, "desc": description, "project": project})


projects = projectService()
projects.create_project("Emre", "Nokia5", "p5")
projects.read_project()