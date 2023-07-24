import json


def file_upload(file_path):
    if file_path:
        with open(file_path) as json_file:
            data = json.load(json_file)
            return data["device_dict"]
    else:
        print("This file does not exist!")
