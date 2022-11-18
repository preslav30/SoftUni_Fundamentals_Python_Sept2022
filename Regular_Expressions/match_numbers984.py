import re

num = input()
regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
result = re.finditer(regex, num)
for match in result:
    print(match.group(), end=" ")
