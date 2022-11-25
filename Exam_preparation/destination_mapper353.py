import re

locations = input()
locations_list = []
travel_points = 0
pattern = r"((?P<name>\=|\/)([][A-Z]{1}[A-Za-z]{2,})(?P=name))"
result = re.finditer(pattern, locations)

for match in result:
    travel_points += len(match.group(3))
    locations_list.append(match.group(3))

print(f"Destinations: {', '.join(locations_list)}")
print(f"Travel Points: {travel_points}")
