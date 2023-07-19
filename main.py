from pymongo import MongoClient
from services.person_service import create_person,read_person_list,update_person,delete_person, check_username, person_file_operation
from models.person import PersonService
from db.db_manager import Database
import json
import os
from common.file_reader import File_reader

#person_model = PersonService()

database = Database()
database.connect_database()
person_collection = database.people_collection

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
            while True: #Does not exit the code until you give command to exit

                    selection = int(input("\nWhat would you like to do with Person database?\n1 Read\n2 Write\n3 Update\n4 Delete\n5 Add Document\n6 Exit\n"))

                    if selection == 1: #Printing everything in people collection
                        
                        read_person_list()
                        

                    elif selection == 2: #Adding a new entry to the collection PERSON 
                        
                        #Taking user input for the fields of the new entry
                        nameInput = input("Name: ")
                        adminInput = input("Is this an admin? Yes or No ")
                        projectInput = input("Project: ")
                        usernameInput = input("Username: ")

                        pObject = PersonService(name = nameInput, isAdmin=adminInput, project= projectInput, username= usernameInput)

                        while True:
                            if check_username(usernameInput):
                                usernameInput = input("This username is already in use, please enter a new one: ")
                            else:
                                create_person(nameInput, adminInput, projectInput, usernameInput)
                                break
                        
                    elif selection == 3: #Updates an already existing entry
                        #Identifying the entry to be updated
                        person_to_update = input("Please enter username of the person to be updated: ")
                        username_to_update = {"username": person_to_update}
                    
                        #Printing the entry's current values for clarity
                        print(person_collection.find_one(username_to_update, {"_id": 0}))
                    
                        #Taking the soon-to-be-updated values for the entry
                        updatedName = input("Please enter a new name (Leave blank if you wish to keep it): ")
                        updatedAdmin = input("Please enter the new admin permissions, yes or no (Leave blank if you wish to keep it): ")
                        updatedProject = input("Please enter a new project name (Leave blank if you wish to keep it): ")
                        updatedUsername = input("Please enter a new username (Leave blank if you wish to keep it): ")

                        update_person(username_to_update, updatedName, updatedAdmin, updatedProject, updatedUsername)

                    elif selection == 4: #Deletes an existing entry
                        #Identifying the entry to be deleted
                        person_to_delete = input("Please enter the username of the person to be deleted: ")
                        username_to_delete = {"username": person_to_delete}
                        
                        delete_person(username_to_delete, person_to_delete)

                    
                    elif selection == 5:
                        json_file_path = input("Enter the JSON file path: ")
                        file = File_reader()
                        file.others_upload(person_collection, json_file_path)

                    elif selection == 6:
                        break

                    else:
                        print("Please enter a valid command")

                

        elif option == 2:
            with open("project_service.py") as f2:
                exec(f2.read())
        elif option == 3:
            with open("device_service.py") as f3:
                exec(f3.read())
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
