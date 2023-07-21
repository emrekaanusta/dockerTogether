import json


#enables to read and upload json file into the MongoDB for person and project
def file_upload(filepath):
    if filepath:
        with open(filepath) as json_file:
            data = json.load(json_file)

            return data["project_dict"]
    else:
        print("This file does not exist!")