import json
from pymongo import MongoClient
from db.db_manager import Database
import os
from models.person import PersonService

database = Database()
database.connect_database()
people = database.people_collection

def person_file_operation(filepath):

    if filepath:
        with open(filepath) as json_file:
            data = json.load(json_file)

            for item in data:
                if not people.find_one(item):
                    people.insert_one(item)  

            print("\nFile has been successfully uploaded to the database after the checking of duplicates!")

    else:
        print("This file does not exist!")

def check_username(username):

    existing_user = people.count_documents({"username": username})

    if existing_user < 0:
        return True
    else:
        return False

def read_person_list():
    mongoList = people.find({},{"_id":0})
    for person in mongoList:
            print(person)

def create_person(name_input, admin_input, project_input, username_input):
    if admin_input.lower() == "yes":
        admin_input_int = 1
    else:
        admin_input_int = 0    
    person_string = '{"name": "%s", "isAdmin": %d, "project": "%s", "username": "%s"}' % (name_input,admin_input_int,project_input,username_input)
    new_person = json.loads(person_string)
    new_person_Object = PersonService(name= name_input, isAdmin= admin_input, project= project_input, username= username_input)
    #Inserting the new entry to the collection
    people.insert_one(new_person)

    print("New Person added to database\n %s" % people.find_one({"username": username_input}, {"_id": 0}))

def update_person(username_to_updatef, updated_name, updated_admin, updated_project, updated_username):

    if updated_admin.lower() == "yes":
        updated_admin_int = 1
    else:
        updated_admin_int = 0

    for userN in people.find(username_to_updatef):
        
        if updated_name != "":
            people.update_one(username_to_updatef, {"$set": {"name": updated_name}})
        if updated_admin != "":
            people.update_one(username_to_updatef, {"$set": {"isAdmin": updated_admin_int}})
        if updated_project != "":
            people.update_one(username_to_updatef, {"$set": {"project": updated_project}})
        if updated_username != "":
            people.update_one(username_to_updatef, {"$set": {"username": updated_username}})
    
    if updated_name == username_to_updatef or updated_name == "":
        print("Person updated\n %s" % people.find_one(username_to_updatef, {"_id": 0}))
    else:
        print("Person updated\n %s" % people.find_one({"username": updated_username}, {"_id": 0}))
            
def delete_person(user_to_delete, person_to_delete):
        
        #Little security question
        answer = input("Are you sure you want to delete the following person?\n %s\n" % people.find_one({"username": person_to_delete}, {"_id": 0}))

        if answer.lower() == "yes":
            print("Following person is deleted from the database\n %s" % people.find_one({"username": person_to_delete}, {"_id": 0}))
            people.delete_one(user_to_delete)
        else:
            print("Deletion process is cancelled")

#CREATE READ UPDATE DELETE


    
    