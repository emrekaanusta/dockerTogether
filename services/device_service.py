def read_device(device_collection, devicenumber):
    document = device_collection.find_one({'device_number': devicenumber})
    if document:   #meaning we have a device with that specific number
        print("Device number:", devicenumber)
        print("Device IP:", document.get("device_ip"))
        print("Device port number:", document.get("device_port"))
        print("Device username:", document.get("device_username"))
        print("Device password:", document.get("device_password"))
    else:  
        print("There is no device with this specific device number.")

    print(" ")  

def add_device(device_collection, device):
    if not device_collection.find_one({'device_number': device.device_number}):
        new_document = {"device_number": device.device_number, "device_ip": device.device_ip, "device_port": device.device_port, "device_username": device.device_username, "device_password": device.device_password}
        device_collection.insert_one(new_document)
        print("Device with the  device number ", device.device_number, " has been successfully added to the database!", sep="")
    else: 
        print("There is already a device with that specific device number.")
        
def delete_device(device_collection, number):
    device_collection.delete_one({"device_number": number})
    print("Device with the device number", number, "has been successfully deleted from the database!")

def update_device(device_collection, device_num):
    print(" ")
    document = device_collection.find_one({'device_number': device_num})
    if document:   #meaning we have a device with that specific number
        print("Please enter the new device information. Enter 'none' if you want the information to stay the same.\n")
        new_device_number = input("Please enter a new device number: ")
        update_fields = {}

        if new_device_number != "":
            update_fields["device_number"] = new_device_number

        new_ip = input("Please enter a new ip number: ")  
        if new_ip != "":
            update_fields["device_ip"] = new_ip

        new_port = input("Please enter a new port number: ")
        if new_port != "":
            update_fields["device_port"] = new_port
                
        new_username = input("Please enter a new username: ") 
        if new_username != "":
            update_fields["device_username"] = new_username
              
        new_password = input("Please enter a new password: ") 
        if new_password != "":
            update_fields["device_password"] = new_password

        if update_fields:  # Check if any fields were updated
            device_collection.update_one({"device_number": device_num}, {"$set": update_fields})
                
        print("Device is successfully updated!\n")      
    else: 
        print("There is no device with the number ", device_num , ".\n", sep="")

def json_file_upload(device_collection, device_list):
    for device in device_list:
        device_number = device.get("device_number")
        existing_device = device_collection.find_one({"device_number": device_number})

        if not existing_device:
            new_document = {
                "device_number": device_number,
                "device_ip": device.get("device_ip"),
                "device_port": device.get("device_port"),
                "device_username": device.get("device_username"),
                "device_password": device.get("device_password")
            }
            device_collection.insert_one(new_document)
        else:
            print("There is already a device with device number", device_number, "!")

    print("\nFile has been successfully uploaded to the database after checking for duplicates!")

            