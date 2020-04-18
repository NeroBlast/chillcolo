import random

class RuleWrapper:
    
    def stringyfy(self,rawrule,lstPlayer):
        min = rawrule["min"]
        max = rawrule["max"]
        gorgees = random.randrange(min,max)
        rule = rawrule["enonce"]
        while len(lstPlayer) != 0:
            randomPlayer = random.choice(lstPlayer)
            lstPlayer.remove(randomPlayer)
            print(randomPlayer)
            rule = rule.replace('$', randomPlayer ,1)
        rule = rule.replace('#', str(gorgees), 1)
        
        return rule