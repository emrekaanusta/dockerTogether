from pymongo import MongoClient
from bson import ObjectId
import json
from db.db_manager import connect_collection 

'''
database = Database()
database.connect_database()
projects = database.project_collection
'''

#TODO classları kaldı model dışında, dictionarya oku 
    
#enables to read and upload json file into the MongoDB for person and project
def file_upload(filepath):
    if filepath:
        with open(filepath) as json_file:
            data = json.load(json_file)
            print("data type is: ",type(data))
            return data

    else:
        print("This file does not exist!")

#TODO return json file dict, dict objecte dönştür


'''
                for item in data:
                    if not projects.find_one(item):
                        projects.insert_one(item)  

                print("\nFile has been successfully uploaded to the database after the checking of duplicates!")
'''