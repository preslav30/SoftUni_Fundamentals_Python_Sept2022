phonebook = {}
while True:
    command = input().split("-")
    if len(command) == 1:
        searches = int("".join(command))
        break
    name = command[0]
    number = command[1]
    phonebook[name] = number

for i in range(searches):
    search = input()
    if search in phonebook.keys():
        print(f"{search} -> {phonebook[search]}")

    else:
        print(f"Contact {search} does not exist.")

