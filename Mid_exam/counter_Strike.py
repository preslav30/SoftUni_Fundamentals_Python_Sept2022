energy = int(input())
distance = input()
wins = 0
game_over = False
while distance != "End of battle":
    distance = int(distance)
    if distance > energy:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        quit()
    else:
        energy -= distance
        wins += 1
        if wins % 3 == 0:
            energy += wins
    distance = input()
    if distance == "End of battle":
        game_over = True
if game_over:
    print(f"Won battles: {wins}. Energy left: {energy}")
