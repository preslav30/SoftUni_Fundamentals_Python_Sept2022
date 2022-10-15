def trains(wagons):
    zeros_list = [0 for char in range(wagons)]
    command = input()
    while command != "End":
        command = command.split()
        if "add" in command:
            zeros_list[-1] += int(command[1])

        elif "insert" in command:
            zeros_list[int(command[1])] += int(command[2])

        elif "leave" in command:
            zeros_list[int(command[1])] -= int(command[2])

        command = input()
    return zeros_list


num = int(input())
print(trains(num))
