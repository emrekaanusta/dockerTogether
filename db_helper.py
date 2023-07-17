from pymongo import MongoClient

class database:
    
    def __init__(self, client, db, collection):
        self.client = client
        self.db = db
        self.collection = collection
    
    def connect_database():
        # connecting MongoDB instance
        client = MongoClient("localhost", 27017)

        #  If the 'projectdb' doesn't exist, it is created. Otherwise, it is used.
        db = client.projectdb

        # If 'project' collection doesn't exist, it will be created. Otherwise, it is used.
        collection = db.collection
