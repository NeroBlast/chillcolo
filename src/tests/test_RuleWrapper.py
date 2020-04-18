from Infrastructure import RuleWrapper
from Infrastructure import JsonTranscoder

transcoder = JsonTranscoder.JsonTranscoder()
wrapper = RuleWrapper.RuleWrapper()

jsonrule = transcoder.getJsonRule(3,"round")
rule = wrapper.stringyfy(jsonrule,["Vincent","Charlie","David","PE","Aure"])
print(rule)