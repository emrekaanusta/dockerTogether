from pymongo import MongoClient

class Database:
    
    def connect_database(self):
        # connecting MongoDB instance
        client = MongoClient("localhost", 27017)

        #  If the 'persondb' doesn't exist, it is created. Otherwise, it is used.
        db = client.main_db
        client = MongoClient('mongodb://localhost:27017/')
        # If 'project' collection doesn't exist, it will be created. Otherwise, it is used.

        db = client['nokia_project']
        self.people_collection = db["people"]
