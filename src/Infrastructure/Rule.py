
class Rule:
    id = 0
    variante = 0

    def __init__(self,typee,id,variante):
        self.type = typee
        self.id = id
        self.variante = variante
        self.value=(typee,(id,variante))

    def getValue(self):
        return self.value


    def getId(self):
        return self.id
    
    def getVariante(self):
        return self.variante

    #compare to a key entry for a dict
    def equals(self,rule):
        if self.getValue() == rule:
            return True
        return False

def ruleExists(listOfRules,rule):
    for regle in listOfRules:
        if rule.equals(regle):
            return True
    return False

def ruleAlereadyDone(dictRules,regle):
    for rule in dictRules:
        if regle.getValue() == rule:
            return True
    return False

def ruleOccuredAminAmount(dictRules,regle):
    min = 99
    minOfRule = 0
    for rule in dictRules:
        if regle.equals(rule):
            minOfRule = dictRules[rule]
            if minOfRule>min:
                return False
        elif min < dictRules[rule]:
            min = dictRules[rule]
    if(min<minOfRule):
        return False
    return True