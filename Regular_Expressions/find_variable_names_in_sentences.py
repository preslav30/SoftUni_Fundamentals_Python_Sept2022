import re

text = input()
regex = r"\b_([A-Za-z0-9]+)\b"
result = re.findall(regex, text)
print(",".join(result))
