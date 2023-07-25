import json


#enables to read and upload json file into the MongoDB
def file_upload(filepath, dict):
    if filepath:
        with open(filepath) as json_file:
            data = json.load(json_file)
            return data[dict]
    else:
        print("This file does not exist!")