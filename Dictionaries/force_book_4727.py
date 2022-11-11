force_and_users = {}

while True:
    user_removed = False
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        force_side, force_user = command.split(" | ")
        if any(force_user in val for val in force_and_users.values()):
            continue
        elif force_side in force_and_users.keys() and force_user not in force_and_users.values():
            force_and_users[force_side].append(force_user)
        elif force_side not in force_and_users.keys() and force_user not in force_and_users.values():
            force_and_users[force_side] = [force_user]
    else:
        force_user, force_side = command.split(" -> ")
        for side, user in force_and_users.items():
            if force_user in user and side != force_side:
                force_and_users[force_side].append(force_user)
                user.remove(force_user)
                user_removed = True

        if user_removed:
            print(f"{force_user} joins the {force_side} side!")
            continue
        if force_user not in force_and_users.values() and force_side in force_and_users.keys():
            force_and_users[force_side].append(force_user)
        elif force_user not in force_and_users.values() and force_side not in force_and_users.keys():
            force_and_users[force_side] = [force_user]
        print(f"{force_user} joins the {force_side} side!")

for sides, users in force_and_users.items():
    if len(users) == 0:
        continue
    else:
        print(f"Side: {sides}, Members: {len(users)}")
    for each_user in users:
        print(f"! {each_user}")


