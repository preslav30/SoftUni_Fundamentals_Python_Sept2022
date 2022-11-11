number_of_commands = int(input())
dict_of_users = {}
for commands in range(number_of_commands):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        license_plate = command[2]
        if username in dict_of_users.keys():
            print(f"ERROR: already registered with plate number {dict_of_users[username]}")

        else:
            dict_of_users[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    else:
        if username not in dict_of_users.keys():
            print(f"ERROR: user {username} not found")

        else:
            del dict_of_users[username]
            print(f"{username} unregistered successfully")

for usernames, license_plate_number in dict_of_users.items():
    print(f"{usernames} => {license_plate_number}")


