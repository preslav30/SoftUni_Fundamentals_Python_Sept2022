initial_loot = input().split("|")
commands = input()
stolen = []
empty = False
while commands != "Yohoho!":
    commands = commands.split()
    action = commands[0]
    if action == "Loot":
        for item in range(1, len(commands)):
            if commands[item] in initial_loot:
                continue
            else:
                initial_loot.insert(0, commands[item])
    elif action == "Drop":
        index = int(commands[1])
        if 0 <= index <= len(initial_loot) - 1:
            removed = initial_loot[index]
            initial_loot.pop(index)
            initial_loot.append(removed)
        else:
            commands = input()
            continue
    elif action == "Steal":
        count = int(commands[1])
        if len(initial_loot) <= count:
            print(", ".join(initial_loot))
            print("Failed treasure hunt.")
            quit()
        else:
            stolen = initial_loot[-count:]
            del initial_loot[-count:]
            # for i in range(1, count + 1):
            #     stolen.append(initial_loot[-1])
            #     initial_loot.pop(-1)
        # stolen.reverse()
        print(", ".join(stolen))
    if len(initial_loot) <= 0:
        empty = True

    commands = input()

if not empty:
    avg_gain = sum([len(avg) for avg in initial_loot]) / len(initial_loot)
    print(f"Average treasure gain: {avg_gain:.2f} pirate credits.")
