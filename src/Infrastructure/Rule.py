
class Rule:
    id = 0
    variante = 0

    def __init__(self,typee,id,variante):
        self.type = typee
        self.id = id
        self.variante = variante
    
    def getId(self):
        return self.id
    
    def getVariante(self):
        return self.variante


    def equals(self,rule):
        if(not(isinstance(rule,Rule))):
            print("Wrong type objects")
            exit()
        elif(self.id != rule.getId):
            return False
        elif(self.variante != rule.getVariante):
            return False
        return True

def ruleExists(listOfRules,rule):
    for regle in listOfRules:
        if rule.equals(regle):
            return True
    return False
    
def ruleOccuredAminAmount(dictRules,regle):
    min = 99
    minOfRule = 0
    for rule in dictRules:
        if rule.equals(regle):
            minOfRule = dictRules[rule]
            if minOfRule>min:
                return False
        elif min < dictRules[rule]:
            min = dictRules[rule]
    if(min<minOfRule):
        return False
    return True