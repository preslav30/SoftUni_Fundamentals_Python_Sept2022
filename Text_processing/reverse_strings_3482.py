while True:
    command = input()
    if command == "end":
        break
    reversed = command[::-1]
    print(f"{command} = {reversed}")