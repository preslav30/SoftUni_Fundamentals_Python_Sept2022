items = input().split(", ")

command = input()
while command != "Craft!":
    command = command.split(" - ")
    action = command[0]
    item = command[1]
    if action == "Collect":
        if item in items:
            command = input()
            continue
        else:
            items.append(item)
    elif action == "Drop":
        if item in items:
            items.remove(item)
        else:
            command = input()
            continue
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in items:
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, new_item)
        else:
            command = input()
            continue
    elif action == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)
        else:
            command = input()
            continue
    command = input()
items = ", ".join(items)
print(items)
