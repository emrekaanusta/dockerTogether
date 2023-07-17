import json
from pymongo import MongoClient 
from db.db_manager import database
client = MongoClient('mongodb://localhost:27017/')
db = client['nokia_project']
collection = db['device_database']

def read_device(collection, devicenumber):
    document = collection.find_one({'device_number': devicenumber})
    if document:   #meaning we have a device with that specific number
        print("Device number:", devicenumber)
        print("Device IP:", document["device_ip"])
        print("Device port number:", document["device_port"])
        print("Device username:", document["device_username"])
        print("Device password:", document["device_password"])
    else:  
        print("There is no device with this specific device number.")

    print(" ")  

def add_device(db, device_num, ip, port, username, password):
    if not collection.find_one({'device_number': device_num}):
        new_document = {"device_number": device_num, "device_ip": ip, "device_port": port, "device_username": username, "device_password": password}
        db.devices.insert_one(new_document)
        #cursor = collection.find()
        #for document in cursor:
            #print(document)
        print("Device with the  device number ", device_num, " has been successfully added to the database!", sep="")
    else: 
        print("There is already a device with that specific device number.")
        
def delete_device(db, number):
    db.devices.delete_one({"device_number": number})
    print("Device with the device number", number, "has been successfully deleted from the database!")

def update_device(db, collection, device_num):
    print(" ")
    document = collection.find_one({'device_number': device_num})
    if document:   #meaning we have a device with that specific number
        print("Please enter the new device information. Enter 'none' if you want the information to stay the same.\n")
        device_num = document["device_number"]
        ip = document["device_ip"]
        username = document["device_username"]
        password = document["device_password"]
        port = document["device_port"]
        num = document["device_number"]
        new_device_number = input("Please enter a new device number: ")
        if new_device_number == "":
            new_device_number = num
        else:
             new_device_number = int(new_device_number)
        new_ip = input("Please enter a new ip number: ")  
        if new_ip == "":
                new_ip = ip
        new_port = input("Please enter a new port number: ")
        if new_port == "":
                new_port = port
        new_username = input("Please enter a new username: ") 
        if new_username == "":
                new_username = username
        new_password = input("Please enter a new password: ") 
        if new_password == "":
                new_password = password

        new_device_info = {"device_number": new_device_number, "device_ip": new_ip, "device_port": new_port, "device_username": new_username, "device_password": new_password}
        db.devices.replace_one({"device_number": device_num}, new_device_info)

        print("Device is successfully updated!\n")      
    else: 
        print("There is no device with the number ", device_num , ".\n", sep="")

def json_file_upload(collection, file_path):
    if file_path:
        with open(file_path) as json_file:
            data = json.load(json_file)

            for item in data:
                if not collection.find_one(item):
                    collection.insert_one(item)  
                else:
                    print("There is already a device with device number ", item["device_number"], "!", sep="")   
            
            print("\nFile has been successfully uploaded to the database after the checking of duplicates!")
    else:
        print("This file does not exist!")
            