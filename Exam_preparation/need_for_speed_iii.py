cars_dict = {}
number_of_cars = int(input())
for i in range(1, number_of_cars + 1):
    car, mileage, fuel = input().split("|")
    mileage, fuel = int(mileage), int(fuel)
    cars_dict[car] = [mileage, fuel]
while True:
    data = input()
    if data == "Stop":
        break
    data = data.split(" : ")
    command = data[0]
    car = data[1]

    if command == "Drive":
        distance = int(data[2])
        fuel = int(data[3])
        if fuel <= cars_dict[car][1]:
            cars_dict[car][1] -= fuel
            cars_dict[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car][0] >= 100000:
                del cars_dict[car]
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")

    elif command == "Refuel":
        fuel = int(data[2])
        if cars_dict[car][1] + fuel > 75:
            fuel = 75 - cars_dict[car][1]
            cars_dict[car][1] = 75

        else:
            cars_dict[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")
    elif command == "Revert":
        km = int(data[2])
        cars_dict[car][0] -= km

        if cars_dict[car][0] < 10000:
            cars_dict[car][0] = 10000
            continue
        else:
            print(f"{car} mileage decreased by {km} kilometers")
for car, details in cars_dict.items():
    print(f"{car} -> Mileage: {cars_dict[car][0]} kms, Fuel in the tank: {cars_dict[car][1]} lt.")