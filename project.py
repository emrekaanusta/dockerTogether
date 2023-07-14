
from pymongo import MongoClient
from bson import ObjectId
import json
import os


# file operations are done such as checking file path, opening file and loading/inserting data from JSON to MongoDB
def fileOperation(filepath):

    # check if file is exists
    if not os.path.isfile(filepath):
        raise FileNotFoundError("File was not found or is a directory")

    # loading or opening JSON file
    with open(filepath) as file:
        data = json.load(file)

        # Check whether data is more than 1 or not, then inserting loaded data to collection in MongoDB.
        if isinstance(data, list):
            db.projects.insert_many(data)
        else:
            db.projects.insert_one(data)

        print("Data has been written to MongoDB.")

# menu is created for selecting CRUD operation
def menu():
    print("Select one of the CRUD operation: \n"
          "1. Create a new project\n"
          "2. Read projects\n"
          "3. Update project\n"
          "4. Delete project\n"
          "5. Exit\n"
          "Enter selection: ")


#creating new collection
def createProject(name, desc, project):
    if name is None or project is None:
        print("Name and Project cannot be NULL")
        return __name__()
    elif desc == "":
        db.projects.insert_one({"name": name, "desc": "", "project": project})
    else:
        db.projects.insert_one({"name": name, "desc": desc, "project": project})


#reading available collection from database
def readProject():
    for p in projects.find():
        print(p)


#this function enables user to updating project collection
def updateProject(uid, name, desc, project):
    for id in projects.find({"_id": uid}):  # search datas relates selected ObjectId
        if name != "":
            db.projects.update_many({"_id": uid},{"$set": {"name": name}})
        if desc != "":
            db.projects.update_one({"_id": uid}, {"$set": {"desc": desc}})
        if project != "":
            db.projects.update_one({"_id": uid}, {"$set": {"project": project}})

#deleting specific collection with using unique project id
def deleteProject(uid):
    db.projects.delete_many({"_id": uid})


if __name__ == "__main__":
    
    # connecting MongoDB instance
    client = MongoClient("localhost", 27017)

    #  If the 'projectdb' doesn't exist, it is created. Otherwise, it is used.
    db = client.projectdb

    # If 'project' collection doesn't exist, it will be created. Otherwise, it is used.
    projects = db.projects

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
