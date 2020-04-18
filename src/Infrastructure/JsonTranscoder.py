import json
import os 

class JsonTranscoder():
    
    # def __init__(self):

    def getJsonRule(self,id,type):
        cwd = os.getcwd()

        try:
            json_file = open("Infrastructure/regles/" + type +"/" + str(id) +".json")
            data = json.load(json_file)
            return data

        except:
            print("rule n°"+ str(id) + " of type :"+ type+"  not found")
