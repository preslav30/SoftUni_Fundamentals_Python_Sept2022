import re

coolness = {}
text = input()
pattern = r"(\*\*|\:\:)([A-Z]{1}[a-z]{2,})(\1)"
result = re.findall(pattern, text)
cool_threshold = 1

for i in text:
    if i.isdigit():
        cool_threshold *= int(i)

for initial_tuple in result:
    letters = initial_tuple[1]
    coolness[initial_tuple] = 0
    for letter in letters:
        coolness[initial_tuple] += ord(letter)
print(f"Cool threshold: {cool_threshold}")
print(f"{len(coolness)} emojis found in the text. The cool ones are:")
for key, value in coolness.items():
    if value >= cool_threshold:
        print("".join(key))
