
from pymongo import MongoClient
from bson import ObjectId
import json
import os

#import db.db_manager
from services.project_service import createProject,menu,readProject,updateProject,deleteProject,fileOperation
from db.db_manager import connect_collection 
from common.file_reader import file_upload
from models.project import Project

#project_model = Project()


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
                #file_reader.others_upload(project_collection, filepath) # function call
                data = file_upload(filepath)
                fileOperation(connect_collection("project"), data, filepath)
                #TODO instertler buraya

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
                                  
                    #TODO device
                    project_model = Project(name=name,description=desc,project=project)
                    createProject(connect_collection("project"), project_model.name, project_model.description, project_model.project)   
                elif selection == 2:
                    readProject(connect_collection("project"))
                elif selection == 3:
                    updated_project = str(input("Enter the unique object ID of the information you want to update: "))
                    uid = ObjectId(updated_project)
                    name = str(input("\nEnter name: "))
                    desc = str(input("\nEnter description: "))
                    project = str(input("\nEnter project: "))
                    project_model = Project(name=name,description=desc,project=project)
                    updateProject(connect_collection("project"), uid, project_model.name, project_model.description, project_model.project)
                elif selection == 4:
                    deleted_project = str(input("Enter the unique object ID you want to delete: "))
                    uid = ObjectId(deleted_project)
                    deleteProject(connect_collection("project"), uid)
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
