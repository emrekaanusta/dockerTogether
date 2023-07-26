from pymongo import MongoClient

#connect MongoDB collection with sending collection name parameter
def connect_collection(name):

        client = MongoClient("localhost", 27017)
        db = client['nokia_project']         
        return db[name]
