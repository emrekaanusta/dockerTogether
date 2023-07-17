from pymongo import MongoClient

class Database:
        
    def connect_database(self):
        # connecting MongoDB instance
        client = MongoClient("localhost", 27017)
        db = client.main_db
        client = MongoClient('mongodb://localhost:27017/')
        db = client['nokia_project']
        self.device_collection = db['device_database']
