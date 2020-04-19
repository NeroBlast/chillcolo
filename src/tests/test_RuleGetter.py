from Infrastructure import RuleWrapper
from Infrastructure import JsonTranscoder
from Infrastructure import PlayerManager
from Infrastructure import RuleGetter

lstplayers = ["Vincent","Charlie","David","Aurelian","Raphael","Mathias","Matthieu","Francois","Terrence","BTP","PE"]
transcoder = JsonTranscoder.JsonTranscoder()
wrapper = RuleWrapper.RuleWrapper()
getter =RuleGetter.RuleGetter(lstplayers)

rule = getter.getRandomRule()
print (rule)