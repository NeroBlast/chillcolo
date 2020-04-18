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
    roundProb = 0
    sanctionsProb = 0
    virusProb = 0

    def __init__(self,all_players):

        probTot = self.normalProb + self.roundProb + self.sanctionsProb + self.virusProb
        self.normalProb = (self.normalProb / probTot) * 100
        self.roundProb = self.normalProb + (self.roundProb /probTot) * 100
        self.sanctionsProb = self.roundProb + (self.sanctionsProb /probTot) * 100
        self.virusProb = self.sanctionsProb + (self.virusProb / probTot) * 100

        self.manager = PlayerManager.PlayerManager(all_players)
        
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
    
    def get_rule(type,id):
        joueurs = self.manager.pickPlayers()
        rule = self.wrapper.stringyfy(raw_rule,joueurs)
        return rule

    def getRandomRule(self):
        
        rdm_type = random.randrange(0,100)
        typee =""
        idMax = 0
        if rdm_type < self.normalProb :
            typee = "normal"
            idMax = self.nb_normal

        elif rdm_type < self.roundProb :
            typee = "round"
            idMax = self.nb_round

        elif rdm_type < self.sanctionsProb :
            typee = "sanctions"
            idMax = self.nb_sanctions

        else:
            typee = "virus"
            idMax = self.nb_virus

        while True:
            print("eeeeeeeeeeee" + str(idMax))
            rdm_rule = random.randrange(1,idMax)
            
            raw_rule = self.transcoder.getJsonRule(rdm_rule,typee)
            print(rdm_rule)
            print(typee)
            #print(raw_rule)
            nb_players_req = raw_rule["nbj"]
            joueurs = self.manager.pickPlayers(nb_players_req)
            print("player rec = "+ str(nb_players_req))
            print("players = "+ str(len(joueurs)))
            if len(joueurs)>= nb_players_req:
                break
        print(raw_rule)
        rule = self.wrapper.stringyfy(raw_rule,joueurs)
        return rule
