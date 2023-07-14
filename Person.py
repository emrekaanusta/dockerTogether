import json
from pymongo import MongoClient

def check_username(username):

    existing_user = people.count_documents({"username": username})

    if existing_user > 0:
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
    #Inserting the new entry to the collection
    db.people.insert_one(new_person)

    print("New Person added to database\n %s" % db.people.find_one({"username": username_input}, {"_id": 0}))

def update_person(username_to_updatef, updated_name, updated_admin, updated_project, updated_username):

    if updated_admin.lower() == "yes":
        updated_admin_int = 1
    else:
        updated_admin_int = 0

    for userN in people.find(username_to_updatef):
        
        if updated_name != "":
            db.people.update_one(username_to_updatef, {"$set": {"name": updated_name}})
        if updated_admin != "":
            db.people.update_one(username_to_updatef, {"$set": {"isAdmin": updated_admin_int}})
        if updated_project != "":
            db.people.update_one(username_to_updatef, {"$set": {"project": updated_project}})
        if updated_username != "":
            db.people.update_one(username_to_updatef, {"$set": {"username": updated_username}})
    
    if updated_name == username_to_updatef or updated_name == "":
        print("Person updated\n %s" % db.people.find_one(username_to_updatef, {"_id": 0}))
    else:
        print("Person updated\n %s" % db.people.find_one({"username": updated_username}, {"_id": 0}))
            
def delete_person(user_to_delete, person_to_delete):
        
        #Little security question
        answer = input("Are you sure you want to delete the following person?\n %s\n" % db.people.find_one({"username": person_to_delete}, {"_id": 0}))

        if answer.lower() == "yes":
            print("Following person is deleted from the database\n %s" % db.people.find_one({"username": person_to_delete}, {"_id": 0}))
            db.people.delete_one(user_to_delete)
        else:
            print("Deletion process is cancelled")

#CREATE READ UPDATE DELETE

if __name__ == "__main__":
    #Connection to client
    client = MongoClient("localhost", 27017)

    #Creating database in the client
    db = client["nokiaProject"]

    people = db["people"]

#dosya varsa yüklemesin
#LOADING JSON FILE
#with open('people.json') as file:
#    file_data = json.load(file)
#people.insert_many(file_data)

#fonksiyonları teker teker böl
while True: #Does not exit the code until you give command to exit

    selection = input("\nWhat would you like to do with Person database?\n Read\n Write\n Add Document\n Update\n Delete\n Exit\n ")

    if selection.lower() == "read": #Printing everything in people collection
        
        read_person_list()
        

    elif selection.lower() == "write": #Adding a new entry to the collection PERSON 
        
        #Taking user input for the fields of the new entry
        nameInput = input("Name: ")
        adminInput = input("Is this an admin? Yes or No ")
        projectInput = input("Project: ")
        usernameInput = input("Username: ")

        while True:
            if check_username(usernameInput):
                usernameInput = input("This username is already in use, please enter a new one: ")
            else:
                create_person(nameInput, adminInput, projectInput, usernameInput)
                break
        
    elif selection.lower() == "update": #Updates an already existing entry
        #Identifying the entry to be updated
        person_to_update = input("Please enter username of the person to be updated: ")
        username_to_update = {"username": person_to_update}
    
        #Printing the entry's current values for clarity
        print(db.people.find_one(username_to_update, {"_id": 0}))
    
        #Taking the soon-to-be-updated values for the entry
        updatedName = input("Please enter a new name (Leave blank if you wish to keep it): ")
        updatedAdmin = input("Please enter the new admin permissions, yes or no (Leave blank if you wish to keep it): ")
        updatedProject = input("Please enter a new project name (Leave blank if you wish to keep it): ")
        updatedUsername = input("Please enter a new username (Leave blank if you wish to keep it): ")

        update_person(username_to_update, updatedName, updatedAdmin, updatedProject, updatedUsername)

    elif selection.lower() == "delete": #Deletes an existing entry
        #Identifying the entry to be deleted
        person_to_delete = input("Please enter the username of the person to be deleted: ")
        username_to_delete = {"username": person_to_delete}
        
        delete_person(username_to_delete, person_to_delete)

    elif selection.lower() == "exit":
        break

    elif selection.lower() == "add document" or selection.lower() == "add doc" or selection.lower() == "add":
        json_file_path = input("Enter the JSON file path: ")

        # Load the data from the JSON file
        with open(json_file_path) as file:
            data = json.load(file)

        people.insert_many(data)

        print("Data has been written to MongoDB.")

    else:
        print("Please enter a valid command")

