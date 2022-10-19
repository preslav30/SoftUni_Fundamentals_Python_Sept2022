list_values = list(map(int, input().split()))
initial_command = input()

while initial_command != "end":
    command_list = initial_command.split()
    command = command_list[0]
    if len(command_list) == 3:
        index1 = int(command_list[1])
        index2 = int(command_list[2])
    if command == "swap":
        list_values[index1], list_values[index2] = list_values[index2], list_values[index1]
    elif command == "multiply":
        list_values[index1] = list_values[index1] * list_values[index2]
    elif command == "decrease":
        for ind in range(len(list_values)):
            list_values[ind] -= 1
    initial_command = input()

for el in range(len(list_values)):
    list_values[el] = str(list_values[el])
result = ", ".join(list_values)
print(result)