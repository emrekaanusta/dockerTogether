import json
from pymongo import MongoClient 

client = MongoClient('mongodb://localhost:27017/')
db = client['device_list']
collection = db['devices']

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

def add_device(db, device_num, ip, port, username, password, device_number_list):
    if device_num not in device_number_list:
        device_number_list.append(str(device_num))
        device_ip_list.append(ip)
        device_port_list.append(port)
        device_username_list.append(username)
        device_password_list.append(password)
        db.devices.insert_one({"device_number": device_num, 
                            "device_ip": ip, 
                            "device_port": port, 
                            "device_username": username, 
                            "device_password": password})
        
        #cursor = collection.find()
        #for document in cursor:
            #print(document)
        print("Device with the  device number ", device_num, " has been successfully added to the database!", sep="")
    else: 
        print("There is already a device with that specific device number.")
        
def delete_device(db, number):
    db.devices.delete_one({"device_number": number})
    print("Device with the device number", number, "has been successfully deleted from the database!")

def update_device(db, collection, device_num, device_number_list, device_port_list, device_username_list, device_password_list, device_ip_list):
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
        if new_device_number != "":
            if new_device_number.isdigit(): # if only numbers
                device_number_list.remove(str(device_num))
                device_number_list.append(new_device_number)
                db.devices.update_one({"device_number": device_num}, { "$set": { 'device_number': int(new_device_number) }})
                print("Device number is successfully updated!\n")
            else: 
                print("Please enter a number!")
        else:
            print("Device number will remain the same.")
        print("")
          
        new_ip = input("Please enter a new ip number: ")  
        if new_ip != "":
            db.devices.update_one({"device_ip": ip}, { "$set": { 'device_ip': new_ip }})
            device_ip_list.remove(ip)
            device_ip_list.append(new_ip)
            print("Device IP is successfully updated!\n")
        print("")

        new_port = input("Please enter a new port number: ")
        if new_port != "":  
            db.devices.update_one({"device_port": port}, { "$set": { 'device_port': new_port }})
            device_port_list.remove(port)
            device_port_list.append(new_port)
            print("Device port number is successfully updated!")
        print("")

        new_username = input("Please enter a new username: ")    
        if new_username != "":
            db.devices.update_one({"device_username": username}, { "$set": { 'device_username': new_username }})
            device_username_list.remove(username)
            device_username_list.append(new_username)
            print("Device username is successfully updated!")

        print("")
        new_password = input("Please enter a new password: ")
        if new_password != "":
            db.devices.update_one({"device_password": password}, { "$set": { 'device_password': new_password }})
            device_password_list.remove(password)
            device_password_list.append(new_password)
            print("Device password is successfully updated!\n")
                
        print("Device is updated successfully!")
    else: 
        print("There is no device with the number ", device_num , ".\n", sep="")

def json_file_upload(collection, file_path, device_number_list, device_port_list, device_username_list, device_password_list, device_ip_list):
    if file_path:
        with open(file_path) as json_file:
            data = json.load(json_file)

            for item in data:
                if item["device_number"] not in device_number_list:
                    if item["device_ip"] not in device_ip_list:
                        if item["device_port"] not in device_port_list:
                            if item["device_username"] not in device_username_list:
                                if item["device_password"] not in device_password_list:
                                    device_number_list.append(item["device_number"])
                                    device_ip_list.append(item["device_ip"])
                                    device_port_list.append(item["device_port"])
                                    device_username_list.append(item["device_username"])
                                    device_password_list.append(item["device_password"])
                                    collection.insert_one(item)
                                else:
                                    print("There is already a device with password ", item["device_password"], "!", sep="")
                            else:
                                print("There is already a device with username ", item["device_username"], "!", sep="")
                        else:
                            print("There is already a device with port number ", item["device_port"], "!", sep="")
                    else:
                        print("There is already a device with IP ", item["device_ip"], "!", sep="")        
                else:
                    print("There is already a device with device number ", item["device_number"], "!", sep="")   
            
            print("\nFile has been successfully uploaded to the database after the checking of duplicates!")
    else:
        print("This file does not exist!")
            

print("\nWelcome to Nokia device database. You can access, add, update and delete device informations.\n")
print("1. Read information about devices")
print("2. Add another device to the database")
print("3. Delete a device from the database")
print("4. Update informations of a device")
print("5. Upload json file to the database\n")



option = int(input("Please enter your choice: "))
device_number_list = []
device_ip_list = []
device_port_list = []
device_username_list = []
device_password_list = []

for i in collection.find():
    device_number_list.append(str(i["device_number"]))
    device_ip_list.append(i["device_ip"])
    device_port_list.append(i["device_port"])
    device_username_list.append(i["device_username"])
    device_password_list.append(i["device_password"])

print(" ")

while option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
    if option == 1:   
        devicenumber = int(input("Please enter the device number of the device that you would like to get information about: "))
        read_device(collection, devicenumber) 

    elif option == 2:
        device_num = int(input("Please enter the device number of the device that you would like to add to the database: "))
        ip = input("Please enter the ip number: ")
        port = input("Please enter the port number: ")
        username = input("Please enter the username: ")
        password = input("Please enter the password: ")
        add_device(db, device_num, ip, port, username, password, device_number_list)

    elif option == 3:
        number = int(input("Select the number of the device that you want to delete: "))
        delete_device(db, number)

    elif option == 4:
        device_num = int(input("Please enter the device number of the device that you would like to update: "))
        update_device(db, collection, device_num, device_number_list, device_port_list, device_username_list, device_password_list, device_ip_list)

    elif option == 5:
        file_path = input("Enter the path to the JSON file: ")
        print("")
        json_file_upload(collection, file_path, device_number_list, device_port_list, device_username_list, device_password_list, device_ip_list)

    print(" ")
    option = int(input("Please enter 1, 2, 3, 4 or 5 to continue database operations and anything other than these to stop the program: "))
  

print("You entered a number different than 1, 2, 3, 4 and 5")
print(" ")     

print("See you later!")