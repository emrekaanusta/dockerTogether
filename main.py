import json
from pymongo import MongoClient 
from db.db_manager import database
client = MongoClient('mongodb://localhost:27017/')
db = client['nokia_project']
collection = db['device_database']


def main():
    print("------Welcome to 'DockerTogether' App------\n")
    print("Please select one of the option:\n" 
          "1. Person\n" 
          "2. Project\n"
          "3. Device\n"
          "4. Exit\n")
    option = int(input())
    if option > 3:
        print("Good Bye!\n")
        exit(0)
        
    while(option != 3):
        if option == 1:
            with open("Person.py") as f1:
                exec(f1.read())
        elif option == 2:
            with open("project.py") as f2:
                exec(f2.read())
        elif option == 3:
            with open("device.py") as f3:
                exec(f3.read())
        else:
            print("Good Bye!\n")
            exit(0)


main()
