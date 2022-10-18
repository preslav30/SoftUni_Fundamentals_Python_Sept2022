sequence_of_elements = input().split()
command = input()
moves = 0
while command != "end":
    command = command.split()
    index1 = int(command[0])
    index2 = int(command[1])
    moves += 1
    element_to_add = f"-{moves}a"
    if index1 == index2 or index1 > len(sequence_of_elements) - 1 or index2 > len(
            sequence_of_elements) - 1 or index1 < 0 or index2 < 0:
        sequence_of_elements = sequence_of_elements[0:len(sequence_of_elements) // 2] + [
            element_to_add] + [element_to_add] + sequence_of_elements[len(sequence_of_elements) // 2:]
        print(f"Invalid input! Adding additional elements to the board")
    elif sequence_of_elements[index1] == sequence_of_elements[index2]:
        to_be_removed1 = sequence_of_elements[index1]
        to_be_removed2 = sequence_of_elements[index2]
        sequence_of_elements.remove(to_be_removed1)
        sequence_of_elements.remove(to_be_removed2)
        print(f"Congrats! You have found matching elements - {to_be_removed1}!")
        if len(sequence_of_elements) == 0:
            print(f"You have won in {moves} turns!")
            break
    elif sequence_of_elements[index1] != sequence_of_elements[index2]:
        print("Try again!")

    command = input()
    if command == "end":
        print(f"Sorry you lose :(")
        print(f"{' '.join(sequence_of_elements)}")
