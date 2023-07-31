
import json
from pymongo import MongoClient
from db.db_manager import connect_collection
import os
from models.person import Person
import types


collection = connect_collection("person_collection")


def check_username(username):
    existing_user = collection.count_documents({"username": username})

    if existing_user > 0:
        return True
    else:
        return False


def read_all_people():
    mongoList = collection.find({}, {"_id": 0})
    for person in mongoList:
        print(person)


def read_individual_person(filter, choice):
    mongoList = collection.find({filter: choice}, {"_id": 0})
    for person in mongoList:
        print(person)


def create_person(name_input, admin_input, project_input, username_input):
    new_person = {
        "name": name_input,
        "isAdmin": admin_input,
        "project": project_input,
        "username": username_input,
    }
    collection.insert_one(new_person)

    print(
        "New Person added to database\n %s"
        % collection.find_one({"username": username_input}, {"_id": 0})
    )


def update_person(
    original_username,
    updated_name,
    updated_admin,
    updated_project,
    updated_username,
):
    for userN in collection.find(original_username):
        if updated_name != "":
            collection.update_one(original_username, {"$set": {"name": updated_name}})
        if updated_admin != "":
            collection.update_one(
                original_username, {"$set": {"isAdmin": updated_admin}}
            )
        if updated_project != "":
            collection.update_one(
                original_username, {"$set": {"project": updated_project}}
            )
        if updated_username != "":
            collection.update_one(
                original_username, {"$set": {"username": updated_username}}
            )

    if updated_username == original_username or updated_username == "":
        print(
            "Person updated\n %s" % collection.find_one(original_username, {"_id": 0})
        )
    else:
        print(
            "Person updated\n %s"
            % collection.find_one({"username": updated_username}, {"_id": 0})
        )


def delete_person(user_to_delete, person_to_delete):
    # Little security question
    answer = input(
        "Are you sure you want to delete the following person?\n %s\n"
        % collection.find_one({"username": person_to_delete}, {"_id": 0})
    )

    if answer.lower() == "yes":
        print(
            "Following person is deleted from the database\n %s"
            % collection.find_one({"username": person_to_delete}, {"_id": 0})
        )
        collection.delete_one(user_to_delete)
    else:
        print("Deletion process is cancelled")


# CREATE READ UPDATE DELETE
