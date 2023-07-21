
from bson import ObjectId
from services.project_service import createProject,menu,readProject,updateProject,deleteProject
from common.file_reader import file_upload
from models.project import Project



def main():
    print("------Welcome to 'DockerTogether' App------\n")
    print("Please select one of the option:\n" 
          "1. Person\n" 
          "2. Project\n"
          "3. Device\n"
          "4. Exit\n")
    option = int(input())
    if option == 4:
        print("Good Bye!\n")
        exit(0)
        
    while(option != 4):
        if option == 1:
            print("Invalid")
                
        elif option == 2:
 
            menu() #function call
            selection = int(input())

            if selection == 5:
                print("Good Bye!\n")
                exit(0)

            while selection != 5:
                if selection == 0:
                    filepath = input("Enter the JSON file path: ")
                    data = file_upload(filepath)
                    for i in data:
                        value = Project(**i)
                        createProject(value.name, value.description,value.device)
                    
                elif selection == 1:
                    name = str(input("\nEnter name: "))
                    description = str(input("\nEnter description: "))
                    device = str(input("\nEnter device: "))
                                  
                    
                    project_model = Project(name=name,description=description,device=device)
                    createProject(project_model.name, project_model.description, project_model.device)   
                elif selection == 2:
                    readProject()
                elif selection == 3:
                    updated_project = str(input("Enter the unique object ID of the information you want to update: "))
                    uid = ObjectId(updated_project)
                    name = str(input("\nEnter name: "))
                    description = str(input("\nEnter description: "))
                    device = str(input("\nEnter device: "))
                    project_model = Project(name=name, description=description, device=device)
                    updateProject(uid, project_model.name, project_model.description, project_model.device)
                elif selection == 4:
                    deleted_project = str(input("Enter the unique object ID you want to delete: "))
                    uid = ObjectId(deleted_project)
                    deleteProject(uid)
                else:
                    print("Good Bye!\n")
                    exit(0)
                menu()
                selection = int(input())


        elif option == 3:
            print("Invalid")
        else:
            print("Good Bye!\n")
            exit(0)


        print("\n------------------------------------")
        print("\nPlease select one of the option:\n" 
            "1. Person\n" 
            "2. Project\n"
            "3. Device\n"
            "4. Exit\n")
        option = int(input())


main()
