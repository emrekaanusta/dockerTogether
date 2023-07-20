from pymongo import MongoClient
from bson import ObjectId
import json
 
'''
database = Database()
database.connect_database()
person = database.people_collection
'''


    #enables to read and upload json file into the MongoDB for device


def file_upload(filepath):
    if filepath:
        with open(filepath) as json_file:
            data = json.load(json_file)
            #print("data type is: ",type(data))
            return data

    else:
        print("This file does not exist!")

'''    
#enables to read and upload json file into the MongoDB for person and project

def others_upload(person, filepath):
    if filepath:
         with open(filepath) as json_file:
            data = json.load(json_file)

            for item in data:
                if not person.find_one(item):
                        person.insert_one(item)  

            print("\nFile has been successfully uploaded to the database after the checking of duplicates!")

    else:
        print("This file does not exist!")
'''