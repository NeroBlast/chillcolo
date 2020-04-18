import json
import os 

class JsonTranscoder():
    
    # def __init__(self):

    def getJsonRule(self,id,type):
        cwd = os.getcwd()
        print(cwd)

        try:
            json_file = open("Infrastructure/regles/" + type +"/" + str(id) +".json")
            data = json.load(json_file)
            print(data)
            return data
            
        except:
            print("rule n°"+ str(id) + " of type :"+ type+"  not found")
