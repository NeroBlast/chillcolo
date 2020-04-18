import random

class RuleWrapper:
    def stringyfy(self,rawrule,lstPlayer):
        print(rawrule["enonce"])
        print(lstPlayer)
        rule = rawrule["enonce"]
        while len(lstPlayer) != 0:
            randomPlayer = random.choice(lstPlayer)
            lstPlayer.remove(randomPlayer)
            print(randomPlayer)
            rule.replace("$", randomPlayer ,1)
        print(rule)