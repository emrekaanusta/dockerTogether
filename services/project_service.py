from db.db_manager import connect_collection 

collection = connect_collection("project")


# menu is created for selecting CRUD operation
def menu():
    print("\nSelect one of the CRUD operation: \n"
          "0. Load Json file\n"
          "1. Create a new project\n"
          "2. Read projects\n"
          "3. Update project\n"
          "4. Delete project\n"
          "5. Exit\n"
          "Enter selection: ")

#TODO isimledirme yap, none kısımları çıkarabiliriz
#creating new collection
""" def createProject(name, description, device):
    if name == "" or device == "":
        print("Name and Device cannot be NULL")
        raise ValueError("Name and Device cannot be NULL")
    elif description == "":
        collection.insert_one({"name": name, "description": "", "device": device})
        
    else:
        collection.insert_one({"name": name, "description": description, "device": device}) """


#creating new collection
def create_project(name, description, device):
    collection.insert_one({"name": name, "description": description, "device": device})


#reading available collection from database
def read_project():
    for p in collection.find():
        print(p)
#TODO read_all_proj funct, read_project_name/device/..func

#this function enables user to updating project collection
def update_project(uid, name, description, device):
    for id in collection.find({"_id": uid}):  # search datas relates selected ObjectId
        if name != "":
            collection.update_many({"_id": uid},{"$set": {"name": name}})
        if description != "":
            collection.update_one({"_id": uid}, {"$set": {"description": description}})
        if device != "":
            collection.update_one({"_id": uid}, {"$set": {"device": device}})

#deleting specific collection with using unique project id
def delete_project(uid):
    collection.delete_many({"_id": uid})