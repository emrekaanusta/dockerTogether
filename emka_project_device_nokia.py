from pymongo import MongoClient 
client = MongoClient('mongodb://localhost:27017/')
db = client['device_list']
collection = db['devices']

def get_info(db, collection):
    devicenumber = int(input("Please enter the device number of the device that you would like to get information about: "))
    document = collection.find_one({'device_number': devicenumber})
    if document:   #meaning we have a device with that specific number
        print("Device number:", devicenumber)
        print("Device IP:", document["device_ip"])
        print("Device port number:", document["device_port"])
        print("Device username:", document["device_username"])
        print("Device password:", document["device_password"])
    else:  
        print("There is no device with the number" + devicenumber + ".")
    print(" ")  

def add_info(db, collection):
    device_num = int(input("Please enter the device number of the device that you would like to add to the database: "))
    ip = input("Please enter the ip number: ")
    port = input("Please enter the port number: ")
    username = input("Please enter the username: ")
    password = input("Please enter the password: ")
    db.devices.insert_one({"device_number": device_num, 
                           "device_ip": ip, 
                           "device_port": port, 
                           "device_username": username, 
                           "device_password": password})
    
    #cursor = collection.find()
    #for document in cursor:
        #print(document)
    print("Device with the  device number ", device_num, " has been successfully added to the database!", sep="")
      
def delete_info(db):
    number = int(input("Select the number of the device that you want to delete: "))
    db.devices.delete_one({"device_number": number})
    print("Device with the device number", number, "has been successfully deleted from the database!")

def update_info(db, collection):
    device_num = int(input("Please enter the device number of the device that you would like to update: "))
    print(" ")
    document = collection.find_one({'device_number': device_num})
    if document:   #meaning we have a device with that specific number
        ip = document["device_ip"]
        username = document["device_username"]
        password = document["device_password"]
        port = document["device_port"]
        num = document["device_number"]
        db.devices.delete_one({"device_number": num})
        print("Enter 1 to change device number")
        print("Enter 2 to change device IP")
        print("Enter 3 to change device port number")
        print("Enter 4 to change device username")
        print("Enter 5 to change device password")
        choice = int(input("Please enter your choice: "))
        print(" ")

        if choice == 1:   #if user wants to update device number
            new_device_num = int(input("Please enter the new device number: "))
            db.devices.insert_one({"device_number": new_device_num, 
                           "device_ip": ip, 
                           "device_port": port, 
                           "device_username": username, 
                           "device_password": password})
            
        if choice == 2:   #if user wants to update device ip
            new_device_ip = input("Please enter the new device IP: ")
            db.devices.insert_one({"device_number": device_num, 
                           "device_ip": new_device_ip, 
                           "device_port": port, 
                           "device_username": username, 
                           "device_password": password}) 
            
        if choice == 3:   #if user wants to update device port
            new_device_port = input("Please enter the new device port number: ")
            db.devices.insert_one({"device_number": device_num, 
                           "device_ip": ip, 
                           "device_port": new_device_port, 
                           "device_username": username, 
                           "device_password": password})
            
        if choice == 4:   #if user wants to update device username
            new_device_username = input("Please enter the new device username: ")
            db.devices.insert_one({"device_number": device_num, 
                           "device_ip": ip, 
                           "device_port": port, 
                           "device_username": new_device_username, 
                           "device_password": password})
            
        if choice == 5:   #if user wants to update device password
            new_device_password = input("Please enter the new device password: ")
            db.devices.insert_one({"device_number": device_num, 
                           "device_ip": ip, 
                           "device_port": port, 
                           "device_username": username, 
                           "device_password": new_device_password})  
       
        print("Device is updated successfully!")

    else: 
        print("There is no device with the number ", device_num , ".", sep="")
    print(" ") 




print(" ")
print("Welcome to Nokia device database. You can access, add, update and delete device informations.")
print(" ")
print("Enter 1 to get info")
print("Enter 2 to add info")
print("Enter 3 to delete info")
print("Enter 4 to update info")


option = int(input("Please enter your choice: "))
print(" ")

while option == 1 or option == 2 or option == 3 or option == 4 :
    if option == 1:   
        get_info(db, collection) 

    elif option == 2:
        add_info(db, collection)

    elif option == 3:
        delete_info(db)

    elif option == 4:
        update_info(db, collection)

        
    print(" ")
    option = int(input("Please enter 1, 2, 3 or 4 to continue database operations and anything other than these to stop the program: "))
  

print("You entererd a number different than 1, 2, 3 and 4")
print(" ")     

print("See you later!")