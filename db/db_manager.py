from pymongo import MongoClient



class Database:

    def connect_database(self):
        
        
        '''
        # connecting MongoDB instance
        #client = MongoClient("localhost", 27017)

        #  If the 'projectdb' doesn't exist, it is created. Otherwise, it is used.
        db = client.main_db
        client = MongoClient("mongodb://localhost:27017/")
        db.client["projectdb"]
        
        # If 'project' collection doesn't exist, it will be created. Otherwise, it is used.
        #device_collection = db.collection
        #person_collection = db.collection
        self.project_collection = db["projects"]
        '''

        # connecting MongoDB instance
        client = MongoClient("localhost", 27017)
        

        #  If the 'projectdb' doesn't exist, it is created. Otherwise, it is used.
        db = client.main_db
        client = MongoClient("mongodb://localhost:27017/")

        # If 'project' collection doesn't exist, it will be created. Otherwise, it is used.
        self.project_collection = db.projects
