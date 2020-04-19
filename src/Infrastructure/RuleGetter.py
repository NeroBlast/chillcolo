import json
import random
import os
from Infrastructure import JsonTranscoder
from Infrastructure import RuleWrapper
from Infrastructure import PlayerManager
from Infrastructure import Rule

class RuleGetter():
    nb_normal = 0
    nb_round = 0
    nb_sanctions = 0
    nb_virus = 0

    MAX_ROUNDS = 25

    normalProb = 60
    roundProb = 40
    sanctionsProb = 10
    virusProb = 20

    def __init__(self,all_players):

        

        self.manager = PlayerManager.PlayerManager(all_players)
        print(self.manager.getPlayers())
        self.wrapper = RuleWrapper.RuleWrapper()
        self.transcoder = JsonTranscoder.JsonTranscoder()
        self.rulesDone = {}
        try:
            json_file = open("Infrastructure/regles/rulesnb.json")
            data = json.load(json_file)
            #print(data)
            for rule in data:
                if rule == "normal":
                    self.nb_normal = data["normal"]
                elif rule == "round":
                    self.nb_round = data["round"]
                elif rule == "sanctions":
                    self.nb_sanctions = data["sanctions"]
                elif rule == "virus":
                    self.nb_virus = data["virus"]    
            
        except:
            print("File containing number of rules not found")
            exit()

        probTot = 0

        if(self.nb_normal == 0):
            self.normalProb = 0
        else:
            probTot +=self.normalProb

        if(self.nb_round == 0):
            self.roundProb = self.normalProb
        else:
            probTot +=self.roundProb
            self.roundProb += self.normalProb

        if(self.nb_sanctions == 0):
            self.sanctionsProb = self.roundProb
        else:
            probTot +=self.sanctionsProb
            self.sanctionsProb += self.roundProb

        if(self.nb_virus == 0):
            self.virusProb = self.sanctionsProb 
        else:
            probTot +=self.virusProb
            self.virusProb = self.virusProb + self.sanctionsProb
        
        print("prob tot :" + str(probTot))


        self.normalProb = (self.normalProb / probTot) * 100
        self.roundProb = (self.roundProb /probTot) * 100
        self.sanctionsProb =  (self.sanctionsProb /probTot) * 100
        self.virusProb = (self.virusProb / probTot) * 100


    def get_rule(self,type,id):
        joueurs = self.manager.pickPlayers()
        rule = self.wrapper.stringyfy(raw_rule,joueurs)
        return rule

    def getRandomRule(self):

        while True:
            rdm_type = random.randrange(0,100)
            # print(str(rdm_type))
            # print(str(self.normalProb))
            # print(str(self.roundProb))
            # print(str(self.sanctionsProb))
            # print(str(self.virusProb))
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
                #print("eeeeeeeeeeee" + str(idMax))
                rdm_rule = random.randrange(1,idMax + 1)
                
                raw_rule = self.transcoder.getJsonRule(rdm_rule,typee)
                
                
                # print(raw_rule)
                nb_players_req = raw_rule["nbj"]
                
                joueurs = self.manager.pickPlayers(nb_players_req)
                if len(joueurs)>= nb_players_req:
                    break
            #print(raw_rule)
            variante = self.wrapper.getVariante(typee,rdm_rule)
            print("type : " + typee)
            print("regle : " + str(rdm_rule))
            print("variante : " + str(variante))
            rule = self.wrapper.stringyfy(raw_rule,joueurs,variante)
            curRule = Rule.Rule(typee,rdm_rule,variante)
            #print(self.rulesDone)
            
            if(Rule.ruleOccuredAminAmount(self.rulesDone,curRule)):
                if(not(curRule.getValue() in self.rulesDone)):
                    self.rulesDone[curRule.getValue()]=1
                else:
                    self.rulesDone[curRule.getValue()]+=1
                break
            else:
                print("Doublon evité")
        return rule
