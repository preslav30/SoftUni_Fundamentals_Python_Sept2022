n = int(input())
heroes = {}
for i in range(n):
    hero, hit_points, mana = input().split()
    hit_points = int(hit_points)
    mana = int(mana)
    heroes[hero] = [hit_points, mana]

while True:
    data = input()
    if data == "End":
        break
    data = data.split(" - ")
    command = data[0]
    hero = data[1]
    if command == "CastSpell":
        mp_needed = int(data[2])
        spell = data[3]
        if heroes[hero][1] >= mp_needed:
            heroes[hero][1] -= mp_needed
            print(f"{hero} has successfully cast {spell} and now has {heroes[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")

    elif command == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        heroes[hero][0] -= damage
        if heroes[hero][0] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!")
        else:
            del heroes[hero]
            print(f"{hero} has been killed by {attacker}!")

    elif command == "Recharge":
        recharge_amount = int(data[2])
        if heroes[hero][1] + recharge_amount > 200:
            recharge_amount = 200 - heroes[hero][1]
            heroes[hero][1] = 200
        else:
            heroes[hero][1] += recharge_amount
        print(f"{hero} recharged for {recharge_amount} MP!")

    elif command == "Heal":
        heal_amount = int(data[2])
        if heroes[hero][0] + heal_amount > 100:
            heal_amount = 100 - heroes[hero][0]
            heroes[hero][0] = 100
        else:
            heroes[hero][0] += heal_amount
        print(f"{hero} healed for {heal_amount} HP!")

for hero, stats in heroes.items():
    print(f"{hero}\n  HP: {heroes[hero][0]}\n  MP: {heroes[hero][1]}")
