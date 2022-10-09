def easter_gifts(gifts_received):
    command = input()
    while command != "No Money":
        command = command.split()
        if "OutOfStock" in command:
            if command[1] in gifts_received:
                for element in gifts_received:
                    if element == command[1]:
                        index = gifts_received.index(element)
                        gifts_received[index] = None
        elif "Required" in command:
            if 0 < int(command[2]) < (len(gifts_received)):
                gifts_received[int(command[2])] = command[1]
        elif "JustInCase" in command:
            gifts_received[-1] = command[1]
        command = input()

    for gift in gifts_received:
        if gift == None:
            continue
        else:
            print(gift, end=" ")


easter_gifts(gifts_received=input().split())
