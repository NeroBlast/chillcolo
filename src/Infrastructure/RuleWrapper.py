import random
import json
import os

class RuleWrapper:

    def stringyfy(self,rawrule,lstPlayer):
        min = rawrule["min"]
        max = rawrule["max"]
        id = rawrule["id"]
        typee = rawrule["type"]
        rule = rawrule["enonce"]

        while len(lstPlayer) != 0:
            randomPlayer = random.choice(lstPlayer)
            lstPlayer.remove(randomPlayer)
            rule = rule.replace('$', randomPlayer ,1)
        while '#' in rule:
            gorgees = random.randrange(min,max)
            rule = rule.replace('#', str(gorgees), 1)

        variantepath = "Infrastructure/regles/" + typee + "/variantes/"+ str(id)+ ".json"
        if os.path.exists(variantepath):
            json_file = open(variantepath)
            data = json.load(json_file)
            nbvariantes = data["nb"]
            variante_rdm = random.randrange(1,nbvariantes+1)
            variante_text = data[str(variante_rdm)]
            rule = rule.replace('&',variante_text,1)

        return rule