initial_health = 100
initial_bitcoins = 0
best_room = 1
commands = input().split("|")
game_over = False
for i in range(len(commands)):
    room = commands[i].split()
    command = room[0]
    if command == "potion":
        health = int(room[1])
        best_room += 1
        if initial_health + health > 100:
            healed_by = 100 - initial_health
            initial_health = 100

            print(f"You healed for {healed_by} hp.")
        else:
            initial_health += health
            print(f"You healed for {health} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        bitcoins = int(room[1])
        print(f"You found {bitcoins} bitcoins.")
        initial_bitcoins += bitcoins
        best_room += 1
    else:
        monster = command
        attack = int(room[1])
        initial_health -= attack
        if initial_health > 0:
            print(f"You slayed {monster}.")
            best_room += 1
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {best_room}")
            game_over = True
            break
if not game_over:
    print(f"You've made it!\nBitcoins: {initial_bitcoins}\nHealth: {initial_health}")
