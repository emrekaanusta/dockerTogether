import json
from pymongo import MongoClient
from db.db_manager import connect_collection
import os
from models.person import Person

'''
database = Database()
database.connect_database()
people = database.people_collection
'''

def person_file_operation(person_collection, data):
    #print(len(data["people"]))
    
    for i in range(len(data["people"])):
        if not person_collection.find_one(data["people"][i]):
                    person_collection.insert_one(data["people"][i])  

    print("\nFile has been successfully uploaded to the database after the checking of duplicates!")

        

def check_username(person_collection, username):

    existing_user = person_collection.count_documents({"username": username})

    if existing_user < 0:
        return True
    else:
        return False

def read_person_list(person_collection):
    mongoList = person_collection.find({},{"_id":0})
    for person in mongoList:
            print(person)

def create_person(person_collection, name_input, admin_input, project_input, username_input):
    if admin_input.lower() == "yes":
        admin_input_int = 1
    else:
        admin_input_int = 0    
    person_string = '{"name": "%s", "isAdmin": %d, "project": "%s", "username": "%s"}' % (name_input,admin_input_int,project_input,username_input)
    new_person = json.loads(person_string)
    new_person_Object = Person(name= name_input, isAdmin= admin_input, project= project_input, username= username_input)
    #Inserting the new entry to the collection
    person_collection.insert_one(new_person)

    print("New Person added to database\n %s" % person_collection.find_one({"username": username_input}, {"_id": 0}))

def update_person(person_collection, username_to_updatef, updated_name, updated_admin, updated_project, updated_username):

    if updated_admin.lower() == "yes":
        updated_admin_int = 1
    else:
        updated_admin_int = 0

    for userN in person_collection.find(username_to_updatef):
        
        if updated_name != "":
            person_collection.update_one(username_to_updatef, {"$set": {"name": updated_name}})
        if updated_admin != "":
            person_collection.update_one(username_to_updatef, {"$set": {"isAdmin": updated_admin_int}})
        if updated_project != "":
            person_collection.update_one(username_to_updatef, {"$set": {"project": updated_project}})
        if updated_username != "":
            person_collection.update_one(username_to_updatef, {"$set": {"username": updated_username}})
    
    if updated_name == username_to_updatef or updated_name == "":
        print("Person updated\n %s" % person_collection.find_one(username_to_updatef, {"_id": 0}))
    else:
        print("Person updated\n %s" % person_collection.find_one({"username": updated_username}, {"_id": 0}))
            
def delete_person(person_collection, user_to_delete, person_to_delete):
        
        #Little security question
        answer = input("Are you sure you want to delete the following person?\n %s\n" % person_collection.find_one({"username": person_to_delete}, {"_id": 0}))

        if answer.lower() == "yes":
            print("Following person is deleted from the database\n %s" % person_collection.find_one({"username": person_to_delete}, {"_id": 0}))
            person_collection.delete_one(user_to_delete)
        else:
            print("Deletion process is cancelled")

#CREATE READ UPDATE DELETE


    
    