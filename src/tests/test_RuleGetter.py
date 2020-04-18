from Infrastructure import RuleWrapper
from Infrastructure import JsonTranscoder
from Infrastructure import PlayerManager
from Infrastructure import RuleGetter

lstplayers = ["Vincent","Charlie","David","Aurelian","Raphael","Math1","Matth2","Francois","Terrence"]
transcoder = JsonTranscoder.JsonTranscoder()
wrapper = RuleWrapper.RuleWrapper()
getter =RuleGetter.RuleGetter(lstplayers)

rule = getter.getRandomRule()
print (rule)