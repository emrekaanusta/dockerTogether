from pymongo import MongoClient
from bson import ObjectId
import json
from os import path


#file operations are done such as checking file path, opening file and loading/inserting data from JSON to MongoDB
def fileOperation():
    # check if file is exists
    if path.isfile('p.json') is False:
        raise Exception("File is not found!")

    # loading or opening JSON file
    with open('p.json') as file:
        file_data = json.load(file)

    # Check whether data is more than 1 or not, then inserting loaded data to collection in MongoDB.
    if isinstance(file_data, list):
        db.projects.insert_many(file_data)
    else:
        db.projects.insert_one(file_data)


#menu is created for selecting CRUD operation
def menu():

    print("Select one of the CRUD operation: \n"
          "1. Create a new project\n"
          "2. Read projects\n"
          "3. Update project\n"
          "4. Delete project\n"
          "5. Exit\n"
          "Enter selection: ")
    selection = int(input())

    if selection == 5:
        print("Good Bye!\n")
        exit(0)

    while selection != 5:
        if selection == 1:
            id = int(input("\nEnter id: "))
            name = str(input("\nEnter name: "))
            desc = str(input("\nEnter description: "))
            project = str(input("\nEnter project: "))

            db.projects.insert_one({"id": id, "name": name, "desc": desc, "project": project})

        elif selection == 2:
            for p in projects.find():
                print(p)

        elif selection == 3:
            for p in projects.find():  #list all the datas from database
                print(p)

            #get unique id as an string, then convert it to ObjectId data type
            updated_id = str(input("Enter the unique object ID of the information you want to update: "))
            uid = ObjectId(updated_id)

            for i in projects.find({"_id": uid}): #search datas relates selected ObjectId
                updated_value = str(input("Which information do you want to update (Id, Name, Desc, Project) or press 'E' to complete the update operation, please enter one of them: "))
                if updated_value == 'Id' or updated_value == "id":
                    new_value = int(input("Enter new id:" ))
                    db.projects.update_one({"_id": uid}, {"$set": {"id": new_value}})
                elif updated_value == "Name" or updated_value == "name":
                    new_value = str(input("Enter new name: "))
                    db.projects.update_one({"_id": uid}, {"$set": {"name": new_value}})
                elif updated_value == "Desc" or updated_value == "desc":
                    new_value = str(input("Enter new description: "))
                    db.projects.update_one({"_id": uid}, {"$set": {"desc": new_value}})
                elif updated_value == "Project" or updated_value == "project":
                    new_value = str(input("Enter new project: "))
                    db.projects.update_one({"_id": uid}, {"$set": {"project": new_value}})
                elif updated_value == 'E':
                    print("Update operation is completed.\n")
                    exit(0)
                else:
                    print("Entered option is invalid. Please try again!\n")

        elif selection == 4:
            for p in projects.find():
                print(p)
            deleted_value = int(input("Enter the value you want to delete: "))
            result = db.projects.delete_many({"id": deleted_value})

        else:
            print("Good Bye!")
            exit(1)

        print("Select one of the CRUD operation: \n"
              "1. Create a new project\n"
              "2. Read projects\n"
              "3. Update project\n"
              "4. Delete project\n"
              "5. Exit\n"
              "Enter selection: ")
        selection = int(input())


if __name__ == "__main__":
    # connecting MongoDB instance
    client = MongoClient("localhost", 27017)

    #  If the 'projectdb' doesn't exist, it is created. Otherwise, it is used.
    db = client.projectdb

    # If 'project' collection doesn't exist, it will be created. Otherwise, it is used.
    projects = db.projects

    # take a JSON file path and create null list
    # filename = 'C:\Users\User\Desktop\dockerDeneme\dockerExample1\dockerTogether\p.json '
    listObj = []

    #control the collection whether is null or not. If there is no collection, function is called. I write it to avoid dumping
    query = db.projects.find()
    if (len(list(query))) == 0:
        fileOperation()  # function call

    menu() #function call

