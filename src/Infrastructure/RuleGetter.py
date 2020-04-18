import json
import random
from Infrastructure import JsonTranscoder
from Infrastructure import RuleWrapper

class RuleGetter():
    nb_normal = 0
    nb_round = 0
    nb_sanctions = 0
    nb_virus = 0


    def __init__(self):
        self.wrapper = RuleWrapper.RuleWrapper()
        self.transcoder = JsonTranscoder.JsonTranscoder()
        self.rulesDone = []
        try:
            json_file = open("Infrastructure/regles/rulesnb.json")
            data = json.load(json_file)
            print(data)
            for rule in data:
                if rule == "normal":
                    self.nb_normal = data["normal"]
                elif rule == "round":
                    self.nb_round = data["round"]
                elif rule == "sanctions":
                    self.nb_sanctions = data["sanctions"]
                elif rule == "virus":
                    self.nb_virus = data["virus"]    
            print(self.nb_normal)
            print(self.nb_round)
            print(self.nb_sanctions)
            print(self.nb_virus)
        except:
            print("File containing number of rules not found")
            exit()


    def getRandomRule(self,joueurs):
        return 0