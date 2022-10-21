target_values = list(map(int, input().split()))
commands = input()

while commands != "End":
    commands = commands.split()
    command = commands[0]
    index = int(commands[1])
    if command == "Shoot":
        if index > len(target_values) - 1 or index < 0:
            commands = input()
            continue
        power = int(commands[2])
        target_values[index] -= power
        if target_values[index] <= 0:
            target_values.pop(index)
    elif command == "Add":
        if index > len(target_values) - 1 or index < 0:
            print(f"Invalid placement!")
            commands = input()
            continue
        value = int(commands[2])
        target_values.insert(index, value)
    elif command == "Strike":
        radius = int(commands[2])
        if index > len(target_values) - 1 or index < 0:
            commands = input()
            continue
        if index - radius < 0 or index + radius > len(target_values) - 1:
            print("Strike missed!")
            commands = input()
            continue
        for i in range(index + radius, index - radius - 1, -1):
            target_values.pop(i)
    commands = input()

for s in range(len(target_values)):
    target_values[s] = str(target_values[s])
target_values = "|".join(target_values)

print(target_values)


