import re

text = input()
word = input()
pattern = r"\b" + word + r"\b"
result = re.findall(pattern, text, re.IGNORECASE)
print(len(result))
