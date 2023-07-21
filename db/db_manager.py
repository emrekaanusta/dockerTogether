from pymongo import MongoClient


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