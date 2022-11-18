import re

lst = []
text = input()
while text:
    lst.append(text)
    text = input()
lst = " ".join(lst)
pattern = r"\d+"
result = re.finditer(pattern, lst)
for match in result:
    print(match.group(), end=" ")
