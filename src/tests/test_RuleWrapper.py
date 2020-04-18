from Infrastructure import RuleWrapper
from Infrastructure import JsonTranscoder

transcoder = JsonTranscoder.JsonTranscoder()
wrapper = RuleWrapper.RuleWrapper()

jsonrule = transcoder.getJsonRule(1,"normal")
wrapper.stringyfy(jsonrule,["Vincent"])