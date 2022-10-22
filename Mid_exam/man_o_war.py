pirate_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
max_health = int(input())
count = 0
while True:
    command = input()
    if command == "Retire":
        break
    command = command.split()
    action = command[0]
    if action == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index <= len(warship_status) - 1:
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                quit()
        else:
            continue
    elif action == "Defend":
        start = int(command[1])
        end = int(command[2])
        damage = int(command[3])
        if 0 <= start <= end <= len(pirate_status) - 1:
            for i in range(start, end + 1):
                pirate_status[i] -= damage
                if pirate_status[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    quit()
        else:
            continue
    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index <= len(pirate_status) - 1:
            if pirate_status[index] + health >= max_health:
                pirate_status[index] = max_health
            else:
                pirate_status[index] += health
        else:
            continue
    elif action == "Status":
        for section in range(len(pirate_status)):
            if pirate_status[section] < max_health * 0.2:
                count += 1
        print(f"{count} sections need repair.")

pirate_sum = sum(pirate_status)
warship_sum = sum(warship_status)
print(f"Pirate ship status: {pirate_sum}\nWarship status: {warship_sum}")

