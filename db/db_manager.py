from pymongo import MongoClient

'''
def connect_database():
        
    #TODO connect_collection
        
    
    # connecting MongoDB instance
    client = MongoClient("localhost", 27017)
        

    #  If the 'projectdb' doesn't exist, it is created. Otherwise, it is used.
    db = client.main_db
    #client = MongoClient("mongodb://localhost:27017/")

    # If 'project' collection doesn't exist, it will be created. Otherwise, it is used.
    self.project_collection = db.projects

    #TODO return db[collection_name]
'''

def connect_collection(name):

        client = MongoClient("localhost", 27017)
        db = client['nokia_project']

        device_collection = db['device_database']
        project_collection = db['project_collection']
        person_collection = db['person_collection']

        if name == "device":
            return device_collection
        if name == "project":
            return project_collection
        if name == "person":
            return person_collection