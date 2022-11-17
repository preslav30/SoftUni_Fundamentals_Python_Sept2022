import re

new_matches = {}
date = input()
regex = r"\d{2}\/[A-Z][a-z]{2}\/\d{4}|\d{2}\.[A-Z][a-z]{2}\.\d{4}|\d{2}\-[A-Z][a-z]{2}\-\d{4}"
matches = re.findall(regex, date)
for i in range(len(matches)):
    symbol = matches[i][2]
    match = matches[i].split(symbol)
    new_matches[i] = match
for match in new_matches.values():
    print(f"Day: {match[0]}, Month: {match[1]}, Year: {match[2]}")