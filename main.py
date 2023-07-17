import db.db_manager
from services.device_service import read_device, add_device, update_device, json_file_upload, delete_device
from db.db_manager import Database
#from models.device import __init__
database = Database()
database.connect_database()
device_collection = database.device_collection


def main():
    print("------Welcome to 'DockerTogether' App------\n")
    print("Please select one of the option:\n" 
          "1. Person\n" 
          "2. Project\n"
          "3. Device\n"
          "4. Exit\n")
    option = int(input())
    if option > 3:
        print("Good Bye!\n")
        exit(0)
        
    while(option != 4):
        if option == 1:
            with open("Person.py") as f1:
                exec(f1.read())
        elif option == 2:
            with open("project.py") as f2:
                exec(f2.read())
        elif option == 3:
            print("1. Read information about devices")
            print("2. Add another device to the database")
            print("3. Delete a device from the database")
            print("4. Update informations of a device")
            print("5. Upload json file to the database\n")

            option = int(input("Please enter your choice: "))
            print(" ")
            checker = True

            while checker:
                checker = False
                if option == 1:   
                    devicenumber = int(input("Please enter the device number of the device that you would like to get information about: "))
                    read_device(device_collection, devicenumber) 
                    checker = True

                elif option == 2:
                    device_num = int(input("Please enter the device number of the device that you would like to add to the database: "))
                    ip = input("Please enter the ip number: ")
                    port = input("Please enter the port number: ")
                    username = input("Please enter the username: ")
                    password = input("Please enter the password: ")
                    add_device(db, device_num, ip, port, username, password)
                    checker = True

                elif option == 3:
                    number = int(input("Select the number of the device that you want to delete: "))
                    delete_device(db, number)
                    checker = True

                elif option == 4:
                    device_num = int(input("Please enter the device number of the device that you would like to update: "))
                    update_device(db, device_collection, device_num)
                    checker = True

                elif option == 5:
                    file_path = input("Enter the path to the JSON file: ")
                    print("")
                    json_file_upload(device_collection, file_path)
                    checker = True

                print(" ")
                if not checker == False:
                    option = int(input("Please enter 1, 2, 3, 4 or 5 to continue database operations and anything other than these to stop the program: "))     
                else:
                    print("You entered a number different than 1, 2, 3, 4 and 5\n")
                    print("See you later!")            

        else:
            print("Good Bye!\n")
            exit(0)


main()
