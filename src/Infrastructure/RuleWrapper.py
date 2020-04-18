import random

class RuleWrapper:

    def stringyfy(self,rawrule,lstPlayer):
        min = rawrule["min"]
        max = rawrule["max"]
        
        rule = rawrule["enonce"]
        while len(lstPlayer) != 0:
            randomPlayer = random.choice(lstPlayer)
            lstPlayer.remove(randomPlayer)
            rule = rule.replace('$', randomPlayer ,1)
        while '#' in rule:
            gorgees = random.randrange(min,max)
            rule = rule.replace('#', str(gorgees), 1)
        return rule