
class Rule:
    id = 0
    variante = 0

    def __init__(self,typee,id,variante):
        self.type = typee
        self.id = id
        self.variante = variante
    
    def getId():
        return self.id
    
    def getVariante():
        return self.variante


    def equals(rule):
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