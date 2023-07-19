import json

def file_upload(file_path):
        if file_path:
            with open(file_path) as json_file:
                data = json.load(json_file)
                return data
        else:
            print("This file does not exist!")

file_upload("/root/dockerTogether/json/device.json")
