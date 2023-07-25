from db.db_manager import connect_collection 

collection = connect_collection("project_collection")


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


#creating new collection
def create_project(Project):
    collection.insert_one({"name":Project.name, "description":Project.description, "device":Project.device})


#reading available collection from database
def read_project():
    for p in collection.find():
        print(p)




#this function enables user to updating project collection
def update_project(uid, Project):
    for id in collection.find({"_id": uid}):  # search datas relates selected ObjectId
        if Project.name != "":
            collection.update_many({"_id": uid},{"$set": {"name": Project.name}})
        if Project.description != "":
            collection.update_one({"_id": uid}, {"$set": {"description": Project.description}})
        if Project.device != "":
            collection.update_one({"_id": uid}, {"$set": {"device": Project.device}})
            

#deleting specific collection with using unique project id
def delete_project(uid):
    collection.delete_many({"_id": uid})