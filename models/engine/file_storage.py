#!/usr/bin/python3
import json

class FileStorage():

    __file_path = './file.json'
    __objects = {}
    

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[type(obj).__name__+"."+obj.id] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            print("**********************************")
            print(FileStorage.__objects)
            print("**********************************")
            json.dump(FileStorage.__objects, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except:
            pass