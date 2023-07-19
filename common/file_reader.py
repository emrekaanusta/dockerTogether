from pymongo import MongoClient
from bson import ObjectId
import json
from db.db_manager import Database 
'''
database = Database()
database.connect_database()
person = database.people_collection
'''
class File_reader:

    #enables to read and upload json file into the MongoDB for device
    def device_upload(self, device_collection, file_path):
        if file_path:
            with open(file_path) as json_file:
                data = json.load(json_file)

                for item in data:
                    if not device_collection.find_one(item):
                        device_collection.insert_one(item)  
                    else:
                        print("There is already a device with device number ", item["device_number"], "!", sep="")   
                
                print("\nFile has been successfully uploaded to the database after the checking of duplicates!")
        else:
            print("This file does not exist!")

    
    #enables to read and upload json file into the MongoDB for person and project
    def others_upload(self,person, filepath):
        if filepath:
            with open(filepath) as json_file:
                data = json.load(json_file)

                for item in data:
                    if not person.find_one(item):
                        person.insert_one(item)  

                print("\nFile has been successfully uploaded to the database after the checking of duplicates!")

        else:
            print("This file does not exist!")