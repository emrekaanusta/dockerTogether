from services.person_service import (
    create_person,
    read_all_people,
    read_individual_person,
    update_person,
    delete_person,
    check_username,
)
from models.person import Person
from db.db_manager import connect_collection
import json
import os
from common.file_reader import file_upload


def main():
    print("------Welcome to 'DockerTogether' App------\n")
    print(
        "Please select one of the option:\n"
        "1. Person\n"
        "2. Project\n"
        "3. Device\n"
        "4. Exit\n"
    )
    option = int(input())
    if option > 3:
        print("Good Bye!\n")
        exit(0)

    while option != 4:
        if option == 1:
            while True:  # Does not exit the code until you give command to exit
                selection = int(
                    input(
                        "\nWhat would you like to do with Person database?\n1 Read\n2 Write\n3 Update\n4 Delete\n5 Add Document\n6 Exit\n"
                    )
                )

                if selection == 1:  # Printing everything in people collection
                    read_option = int(input("1- Read All\n2- Read Filtered\n"))
                    if read_option == 1:
                        read_all_people()
                    elif read_option == 2:
                        filter_option = input(
                            "Which filter? Name, isAdmin, Project or Username\n"
                        )
                        if filter_option.lower() == "isadmin":
                            applied_filter = int(input("Please enter your admin: "))
                        else:
                            applied_filter = input("Please enter your filter: ")
                        read_individual_person(filter_option, applied_filter)

                elif selection == 2:  # Adding a new entry to the collection PERSON
                    # Taking user input for the fields of the new entry
                    nameInput = input("Name: ")
                    adminInput = int(input("Is this an admin? "))
                    projectInput = input("Project: ")
                    usernameInput = input("Username: ")

                    person_model = Person(
                        name=nameInput,
                        isAdmin=adminInput,
                        project=projectInput,
                        username=usernameInput,
                    )

                    while True:
                        if check_username(usernameInput):
                            usernameInput = input(
                                "This username is already in use, please enter a new one: "
                            )
                            person_model.username = usernameInput
                        else:
                            create_person(
                                person_model.name,
                                person_model.isAdmin,
                                person_model.project,
                                person_model.username,
                            )
                            break

                elif selection == 3:  # Updates an already existing entry
                    # Identifying the entry to be updated
                    person_to_update = input(
                        "Please enter username of the person to be updated: "
                    )
                    username_to_update = {"username": person_to_update}

                    # Printing the entry's current values for clarity
                    print(
                        connect_collection("person").find_one(
                            username_to_update, {"_id": 0}
                        )
                    )

                    # Taking the soon-to-be-updated values for the entry
                    updatedName = input(
                        "Please enter a new name (Leave blank if you wish to keep it): "
                    )
                    updatedAdmin = int(
                        input(
                            "Please enter the new admin permissions, yes or no (Leave blank if you wish to keep it): "
                        )
                    )
                    updatedProject = input(
                        "Please enter a new project name (Leave blank if you wish to keep it): "
                    )
                    updatedUsername = input(
                        "Please enter a new username (Leave blank if you wish to keep it): "
                    )

                    person_model = Person(
                        name=updatedName,
                        isAdmin=updatedAdmin,
                        project=updatedProject,
                        username=updatedUsername,
                    )
                    update_person(
                        username_to_update,
                        person_model.name,
                        person_model.isAdmin,
                        person_model.project,
                        person_model.username,
                    )

                elif selection == 4:  # Deletes an existing entry
                    # Identifying the entry to be deleted
                    person_to_delete = input(
                        "Please enter the username of the person to be deleted: "
                    )
                    username_to_delete = {"username": person_to_delete}

                    delete_person(username_to_delete, person_to_delete)

                elif selection == 5:
                    json_file_path = input("Enter the JSON file path: ")
                    data = file_upload(json_file_path, "person_dict")
                    # person_file_operation(connect_collection("person"), data)
                    for i in data:
                        value = Person(**i)
                        create_person(
                            value.name, value.isAdmin, value.project, value.username
                        )
                elif selection == 6:
                    break

                else:
                    print("Please enter a valid command")

        elif option == 2:
            with open("project_service.py") as f2:
                exec(f2.read())
        elif option == 3:
            with open("device_service.py") as f3:
                exec(f3.read())
        else:
            print("Good Bye!\n")
            exit(0)

        print("\n------------------------------------")
        print(
            "\nPlease select one of the option:\n"
            "1. Person\n"
            "2. Project\n"
            "3. Device\n"
            "4. Exit\n"
        )
        option = int(input())


main()
