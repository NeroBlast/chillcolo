from Infrastructure import RuleWrapper
from Infrastructure import JsonTranscoder
from Infrastructure import PlayerManager
from Infrastructure import RuleGetter

lstplayers = ["Vincent","Charlie","PE","David","Aurelian","Connard"]
transcoder = JsonTranscoder.JsonTranscoder()
wrapper = RuleWrapper.RuleWrapper()
getter =RuleGetter.RuleGetter(lstplayers)



rule = getter.getRandomRule()
print (rule)