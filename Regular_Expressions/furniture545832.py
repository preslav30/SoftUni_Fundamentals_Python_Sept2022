import re

names = []
total_price = 0
pattern = r">>(([A-Za-z]+)<<(\d+\.?\d*)!(\d+))"
while True:
    command = input()
    if command == "Purchase":
        break
    matches = re.search(pattern, command)
    if matches is not None:
        names.append(matches.group(2))  # second group
        total_price += float(matches.group(3)) * float(matches.group(4))
print("Bought furniture:")
for item in names:
    print(item)
print(f"Total money spend: {total_price:.2f}")

