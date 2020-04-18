from Infrastructure import JsonTranscoder
import json

transcoder = JsonTranscoder.JsonTranscoder()
rule = transcoder.getJsonRule(1,"normal")
print(rule)