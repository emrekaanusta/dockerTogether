
from bson import ObjectId
from services.project_service import create_project,menu,read_project,update_project,delete_project
from common.file_reader import file_upload
from models.project import Project

from common.file_reader import file_upload
from services.device_service import (
    read_device,
    add_device,
    update_device,
    delete_device,
    read_all_devices,
)
from models.device import Device

def main():
    print("------Welcome to 'DockerTogether' App------\n")
    print(
        "Please select one of the option:\n"
        "1. Person\n"
        "2. Project\n"
        "3. Device\n"
        "4. Exit\n"
    )
    option = int(input())
    if option == 4:
        print("Good Bye!\n")
        exit(0)
      
    while(option != 4):
        if option == 1:
            print("görkem")

        elif option == 2: 
            menu() #function call
            selection = int(input())

            if selection == 5:
                print("Good Bye!\n")
                exit(0)

            while selection != 5:
                if selection == 0:
                    filepath = input("Enter the JSON file path: ")
                    data = file_upload(filepath,"project_dict")
                    
                    for i in data:
                        value = Project(**i)
                        create_project(value)
                    
                elif selection == 1:
                    name = str(input("\nEnter name: "))
                    description = str(input("\nEnter description: "))
                    device = str(input("\nEnter device: "))            
                    
                    project_model = Project(name=name,description=description,device=device)
                    create_project(project_model) 

                elif selection == 2:
                    read_project()

                elif selection == 3:
                    updated_project = str(input("Enter the unique object ID of the information you want to update: "))
                    uid = ObjectId(updated_project)
                    name = str(input("\nEnter name: "))
                    description = str(input("\nEnter description: "))
                    device = str(input("\nEnter device: "))

                    project_model = Project(name=name, description=description, device=device)                    
                    update_project(uid,project_model)

                elif selection == 4:
                    deleted_project = str(input("Enter the unique object ID you want to delete: "))
                    uid = ObjectId(deleted_project)
                    
                    delete_project(uid)

                else:
                    print("Good Bye!\n")
                    exit(0)
                
                menu()
                selection = int(input())
            
        elif option == 3:
            print("1. Read information about devices")
            print("2. Add another device to the database")
            print("3. Delete a device from the database")
            print("4. Update informations of a device")
            print("5. Upload json file to the database\n")

            option = int(input("Please enter your choice: "))
            print(" ")
            checker = False

            while not checker:
                if option == 1:
                    option = int(input("1. Read one device \n2. Read all devices\n"))
                    if option == 1:
                        devicenumber = int(
                            input(
                                "Please enter the device number of the device that you would like to get information about: \n"
                            )
                        )
                        read_device(devicenumber)
                    elif option == 2:
                        read_all_devices()

                elif option == 2:
                    device_num = int(
                        input(
                            "Please enter the device number of the device that you would like to add to the database: "
                        )
                    )
                    ip = input("Please enter the ip number: ")
                    port = input("Please enter the port number: ")
                    username = input("Please enter the username: ")
                    password = input("Please enter the password: ")
                    
                    device = Device(device_num, ip, port, username, password)
                    add_device(device)

                elif option == 3:
                    number = int(
                        input(
                            "Select the number of the device that you want to delete: "
                        )
                    )
                    delete_device(number)

                elif option == 4:
                    device_num = int(
                        input(
                            "Please enter the device number of the device that you would like to update: "
                        )
                    )
                    update_device(device_num)

                elif option == 5:
                    file_path = input("Enter the path to the JSON file: \n")
                    data = file_upload(file_path, "device_dict")
                    for i in data:
                        value = Device(**i)
                        add_device(value)

                else:
                    checker = True

                print(" ")
                if not checker:
                    option = int(
                        input(
                            "Please enter 1, 2, 3, 4 or 5 to continue database operations and anything other than these to stop the program: "
                        )
                    )

        else:
            print("Good Bye!\n")
            exit(0)


        print("\n------------------------------------")
        print("\nPlease select one of the option:\n" 
            "1. Person\n" 
            "2. Project\n"
            "3. Device\n"
            "4. Exit\n")
        option = int(input())


main()
