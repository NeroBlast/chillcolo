from Infrastructure import RuleWrapper
from Infrastructure import JsonTranscoder
from Infrastructure import PlayerManager

lstplayers = ["Vincent","Charlie","PE","David","Aurelian","Connard"]
manager = PlayerManager.PlayerManager(lstplayer)
transcoder = JsonTranscoder.JsonTranscoder()
wrapper = RuleWrapper.RuleWrapper()


jsonrule = transcoder.getJsonRule(2,"virus")
rule = wrapper.stringyfy(jsonrule,["Vincent"])
print(rule)