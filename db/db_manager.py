from pymongo import MongoClient

class database:
    def connect_database():
        # connecting MongoDB instance
        client = MongoClient("localhost", 27017)

        #  If the 'projectdb' doesn't exist, it is created. Otherwise, it is used.
        db = client.main_db

        # If 'project' collection doesn't exist, it will be created. Otherwise, it is used.
        device_collection = db.collection
        person_collection = db.collection
        project_collection = db.collection
