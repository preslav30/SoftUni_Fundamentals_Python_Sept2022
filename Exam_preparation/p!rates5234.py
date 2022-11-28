
cities = {}
while True:
    data = input()
    if data == "Sail":
        break
    data = data.split("||")
    city = data[0]
    population = int(data[1])
    gold = int(data[2])
    if city in cities.keys():
        cities[city][0] += population
        cities[city][1] += gold
    else:
        cities[city] = [population, gold]
while True:
    data = input()
    if data == "End":
        break
    data = data.split("=>")
    command = data[0]
    town = data[1]
    if command == "Plunder":
        people = int(data[2])
        gold = int(data[3])
        cities[town][0] -= people
        cities[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    elif command == "Prosper":
        gold = int(data[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        cities[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, population_money in cities.items():
        print(f"{city} -> Population: {cities[city][0]} citizens, Gold: {cities[city][1]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
