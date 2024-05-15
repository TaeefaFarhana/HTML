import re
pattern = "My name is Taeefa and my another name is Farhana"

result = re.findall("^My.*a$",pattern)
result1 = re.search("^My.*a$",pattern)
result2 = re.split("^\s.*a$",pattern)
#result3 = re.sub("s","9",pattern,2)
result3 = re.sub("s","T",pattern)

print(result)
print(result1)
print(result2)
print(result3)
