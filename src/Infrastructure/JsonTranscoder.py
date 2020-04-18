import json
import os 

class JsonTranscoder():
    
    # def __init__(self):

    def getJsonRule(self,id,type):
        cwd = os.getcwd()
        print(cwd)

        try:
            with open("Infrastructure/regles/" + type +"/" + str(id) +".json") as json_file:
                data = json.load(json_file)
                print(data)
        except:
            print("rule n°"+ str(id) + " of type :"+ type+"  not found")
