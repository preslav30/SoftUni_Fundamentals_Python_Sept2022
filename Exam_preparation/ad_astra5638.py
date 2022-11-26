import re


text = input()
pattern = r"(\#|\|)([A-Za-z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
result = re.findall(pattern, text)
calories = 0
food = ""
for match in result:
    calories += int(match[3])
    food += f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}\n"

print(f"You have food to last you for: {calories // 2000} days!")
print(food)
