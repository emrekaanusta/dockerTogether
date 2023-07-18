
from pymongo import MongoClient
from bson import ObjectId
import json
import os

#import db.db_manager
from services.project_service import fileOperation,createProject,menu,readProject,updateProject,deleteProject
from db.db_manager import Database 

from models.project import projectService
project_model = projectService()


#TODO len al arraya koy


database = Database()
database.connect_database()
project_collection = database.project_collection


def main():
    print("------Welcome to 'DockerTogether' App------\n")
    print("Please select one of the option:\n" 
          "1. Person\n" 
          "2. Project\n"
          "3. Device\n"
          "4. Exit\n")
    option = int(input())
    if option == 4:
        print("Good Bye!\n")
        exit(0)
        
    while(option != 4):
        if option == 1:
            with open("Person.py") as f1:
                exec(f1.read())
                
        elif option == 2:
            
            # Zero is used for load datas from json file to mongoDB, it is optional
            zero_option = int(input("Please enter 0 in order to adding datas from JSON file to MongoDB:  "))
            if zero_option == 0:
                filepath = input("Enter the JSON file path: ")
                fileOperation(filepath) # function call


            menu() #function call
            selection = int(input())

            if selection == 5:
                print("Good Bye!\n")
                exit(0)

            while selection != 5:
                if selection == 1:
                    name = str(input("\nEnter name: "))
                    desc = str(input("\nEnter description: "))
                    project = str(input("\nEnter project: "))
                    p = projectService(name=name, description=desc, project=project)
                    createProject(name, desc, project)                    
                elif selection == 2:
                    readProject()
                elif selection == 3:
                    updated_project = str(input("Enter the unique object ID of the information you want to update: "))
                    uid = ObjectId(updated_project)
                    name = str(input("\nEnter name: "))
                    desc = str(input("\nEnter description: "))
                    project = str(input("\nEnter project: "))
                    updateProject(uid, name, desc, project)
                elif selection == 4:
                    deleted_project = str(input("Enter the unique object ID you want to delete: "))
                    uid = ObjectId(deleted_project)
                    deleteProject(uid)
                else:
                    print("Good Bye!\n")
                    exit(0)
                menu()
                selection = int(input())


        elif option == 3:
            with open("device.py") as f3:
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
