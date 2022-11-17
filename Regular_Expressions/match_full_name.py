import re

names = input()
regex = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
matches = re.findall(regex, names)
print(", ".join(matches))
