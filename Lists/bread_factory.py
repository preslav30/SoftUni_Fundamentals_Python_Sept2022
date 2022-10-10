def bread_factory(events):
    energy = 100
    coins = 100
    handled_all_events = True
    for event in events:
        event = event.split("-")  # ['rest', '2']
        if event[0] == "rest":
            current_energy = energy
            energy += int(event[1])
            if energy >= 100:
                energy = 100
            gained_energy = energy - current_energy

            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
        elif event[0] == "order":
            if energy >= 30:
                energy -= 30
                coins += int(event[1])
                print(f"You earned {int(event[1])} coins.")
            else:
                energy += 50
                print(f"You had to rest!")
        else:
            if coins >= int(event[1]):
                coins -= int(event[1])
                print(f"You bought {event[0]}.")
            else:
                print(f"Closed! Cannot afford {event[0]}.")
                handled_all_events = False
                break
    if handled_all_events:
        print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")


the_events = input().split("|")


bread_factory(the_events)
