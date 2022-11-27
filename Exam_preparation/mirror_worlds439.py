import re


text = input()
mirrors = []
counter = 0
pattern = r"(\#|\@)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
result = re.findall(pattern, text)
for tup in result:
    if tup[1] == tup[2][::-1]:
        mirrors.append(f"{tup[1]} <=> {tup[2]}")
    counter += 1
if counter == 0:
    print("No word pairs found!")
    print(f"No mirror words!")
else:
    print(f"{counter} word pairs found!")
    if mirrors:
        print("The mirror words are:")
        print(', '.join(mirrors))
    else:
        print(f"No mirror words!")
