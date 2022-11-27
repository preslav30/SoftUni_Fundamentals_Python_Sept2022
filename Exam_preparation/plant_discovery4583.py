n = int(input())
plants = {}
for i in range(1, n + 1):
    plant1, rarity = input().split("<->")
    rarity = int(rarity)
    plants[plant1] = [rarity]
while True:
    command = input().split(": ")
    action = command[0]
    if action == "Exhibition":
        break
    elif action == "Rate":
        plant, rating = command[1].split(" - ")
        rating = int(rating)
        if plant not in plants.keys():
            print("error")
            continue
        else:
            plants[plant].append(rating)
    elif action == "Update":
        plant, new_rarity = command[1].split(" - ")
        if plant not in plants.keys():
            print("error")
            continue
        else:
            plants[plant][0] = int(new_rarity)
    elif action == "Reset":
        plant = command[1]
        if plant not in plants.keys():
            print("error")
            continue
        else:
            plants[plant] = [plants[plant][0]]
print(f"Plants for the exhibition:")
for plant1, rarity in plants.items():
    if len(plants[plant1]) == 1:
        print(f"- {plant1}; Rarity: {rarity[0]}; Rating: 0.00")
    else:
        print(f"- {plant1}; Rarity: {rarity[0]}; Rating: {sum(rarity[1:]) / len(rarity[1:]):.2f}")
