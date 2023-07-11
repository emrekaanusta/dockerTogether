import json
from pymongo import MongoClient


#CREATE READ UPDATE DELETE

#Connection to client
client = MongoClient("localhost", 27017)

#Creating database in the client
db = client["nokiaProject"]

people = db["people"]

'''
#LOADING JSON FILE
with open('people.json') as file:
    file_data = json.load(file)

people.insert_many(file_data)
'''

#Find all documents and exclude their ObjectId
x = people.find({},{"_id":0})


while True: #Does not exit the code until you give command to exit

    selection = int(input("\nWhat would you like to do with Person database? \n 1 to read \n 2 to write \n 3 to update \n 4 to delete\n 5 to exit\n"))

    if selection == 1: #Printing everything in people collection
        
        for person in x:
            print(person)

    elif selection == 2: #Adding a new entry to the collection

        #Taking user input for the fields of the new entry
        nameInput = str(input("Name: "))
        adminInput = float(input("Is this and admin? 0 for 'No', 1 for 'Yes' "))
        projectInput = str(input("Project: "))
        idInput = int(input("User ID: "))
    
        #Inserting the new entry to the collection
        db.people.insert_one({"name": nameInput, "isAdmin": adminInput, "project": projectInput, "id": idInput})

        print("New Person added to database\n %s" % db.people.find_one({"id": idInput}, {"_id": 0}))
        
    elif selection == 3: #Updates an already existing entry
        #Identifying the entry to be updated
        person_to_update = int(input("Please enter the ID of the person to be updated: "))
        filter1 = {"id": person_to_update}
    
        #Printing the entry's current values for clarity
        print(db.people.find_one({"id": person_to_update}, {"_id": 0}))
    
        #Taking the soon-to-be-updated values for the entry
        updated_name = str(input("Please enter a new name (Enter the current one if you wish to keep it): "))
        updated_admin = float(input("Please enter the new admin permissions (Enter the current one if you wish to keep it): "))
        updated_project = str(input("Please enter a new project name (Enter the current one if you wish to keep it): "))
        updated_id = int(input("Please enter a new ID number (Enter the current one if you wish to keep it): "))
        new_values = {"$set":{"name": updated_name, "isAdmin": updated_admin, "project": updated_project, "id": updated_id}}

        #Actually making the update
        db.people.update_one(filter1, new_values)

        print("Person updated\n %s" % db.people.find_one({"id": updated_id}, {"_id": 0}))
        

    elif selection == 4: #Deletes an existing entry
        #Identifying the entry to be deleted
        person_to_delete = int(input("Please enter the ID of the person to be deleted: "))
        filter2 = {"id": person_to_delete}

        #Little security question
        delete_answer = str(input("Are you sure you want to delete the following person?\n %s\n" % db.people.find_one({"id": person_to_delete}, {"_id": 0})))


        if delete_answer.lower() == "yes":
            print("Following person is deleted from the database\n %s" % db.people.find_one({"id": person_to_delete}, {"_id": 0}))
            db.people.delete_one(filter2)
        else:
            print("Deletion process is cancelled")
            continue
    else:
        break

