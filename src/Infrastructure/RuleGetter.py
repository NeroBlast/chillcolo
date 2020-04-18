import json
import random
import os
from Infrastructure import JsonTranscoder
from Infrastructure import RuleWrapper
from Infrastructure import PlayerManager

class RuleGetter():
    nb_normal = 0
    nb_round = 0
    nb_sanctions = 0
    nb_virus = 0

    MAX_ROUNDS = 25

    normalProb = 55
    roundProb = 30
    sanctionsProb = 14
    virusProb = 5

    def __init__(self,normal,round,sanctions,virus):

        probTot = self.normalProb + self.roundProb + self.sanctionsProb + self.virusProb
        self.normalProb = (self.normalProb / probTot) * 100
        self.roundProb = self.normalProb + (self.roundProb /probTot) * 100
        self.sanctionsProb = self.roundProb + (self.sanctionsProb /probTot) * 100
        self.virusProb = self.sanctionsProb + (self.virusProb / probTot) * 100

        self.manager = PlayerManager.PlayerManager()
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
            # print(self.nb_normal)
            # print(self.nb_round)
            # print(self.nb_sanctions)
            # print(self.nb_virus)
        except:
            print("File containing number of rules not found")
            exit()


    def getRandomRule(self,joueurs):
        rdm_type = random.randrange(0,100)
        typee =""
        idMax = 0
        if rdm_type < normalProb :
            typee = "normal"
            idMax = self.nb_normal

        elif rdm_type < roundProb :
            typee = "round"
            idMax = self.nb_round

        elif rdm_type < sanctionsProb :
            typee = "sanctions"
            idMax = self.nb_sanctions

        else:
            typee = "virus"
            idMax = self.nb_virus

        while True:
            rdm_rule = random.randrange(1,101)
            raw_rule = transcoder.getJsonRule(rdm_rule,typee)
            nb_players_req = raw_rule["nbj"]
            if len(manager.getPlayers())>= nb_players_req:
                break

        players_selected = self.manager.pickPlayers(nb_players_req)
        
        rule = wrapper.stringyfy(raw_rule,players_selected)
        return rule
