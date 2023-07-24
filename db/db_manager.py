from pymongo import MongoClient

def connect_collection(name):

    client = MongoClient("localhost", 27017)
    db = client["nokia_project"]
    return db[name]
