
from pymongo import MongoClient
from bson import ObjectId
import json
import os


from db.db_manager import connect_collection 
from models.project import Project

#project_model = Project()

'''
database = Database()
database.connect_database()
projects = database.project_collection
'''




def fileOperation(project_collection, data, filepath):

    for item in data:
        if not project_collection.find_one(item):
            project_collection.insert_one(item)  

        print("\nFile has been successfully uploaded to the database after the checking of duplicates!")
       


'''

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
            database.projects.insert_many(data)
        else:
            database.projects.insert_one(data)

        print("Data has been written to MongoDB.")
'''
        

# menu is created for selecting CRUD operation
def menu():
    print("\nSelect one of the CRUD operation: \n"
          "1. Create a new project\n"
          "2. Read projects\n"
          "3. Update project\n"
          "4. Delete project\n"
          "5. Exit\n"
          "Enter selection: ")


#creating new collection
def createProject(project_collection, name, desc, project):
    if name == "" or project == "":
        print("Name and Project cannot be NULL")
        raise ValueError("Name and Project cannot be NULL")
    elif desc == "":
        #new_project = Project(name,"", project)
        project_collection.insert_one({"name": name, "desc": "", "project": project})
        
    else:
        project_collection.insert_one({"name": name, "desc": desc, "project": project})


#reading available collection from database
def readProject(project_collection):
    for p in project_collection.find():
        print(p)


#this function enables user to updating project collection
def updateProject(project_collection, uid, name, desc, project):
    for id in project_collection.find({"_id": uid}):  # search datas relates selected ObjectId
        if name != "":
            project_collection.update_many({"_id": uid},{"$set": {"name": name}})
        if desc != "":
            project_collection.update_one({"_id": uid}, {"$set": {"desc": desc}})
        if project != "":
            project_collection.update_one({"_id": uid}, {"$set": {"project": project}})

#deleting specific collection with using unique project id
def deleteProject(project_collection, uid):
    project_collection.delete_many({"_id": uid})


'''
if __name__ == "__main__":
    
    

    # connecting MongoDB instance
    #client = MongoClient("localhost", 27017)

    #  If the 'projectdb' doesn't exist, it is created. Otherwise, it is used.
    #db = client.projectdb

    # If 'project' collection doesn't exist, it will be created. Otherwise, it is used.
    #projects = db.projects




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
'''


#TODO file okumayı güncelle, insert.many kalsın sadece, boş string yerine NULL/object tanımla/oop
#TODO models folder/project file + device.py + person.py optional-required olarak tnaımla oop olarak bakanilriz