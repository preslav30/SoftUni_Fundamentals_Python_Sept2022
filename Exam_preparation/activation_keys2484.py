activation_key = input()

while True:
    data = input().split(">>>")
    if data[0] == "Generate":
        print(f"Your activation key is: {activation_key}")
        break
    command = data[0]
    if command == "Contains":
        substr = data[1]
        if substr in activation_key:
            print(f"{activation_key} contains {substr}")
        else:
            print(f"Substring not found!")

    elif command == "Flip":
        upper_lower = data[1]
        start = int(data[2])
        end = int(data[3])
        if upper_lower == "Upper":
            activation_key = activation_key.replace(activation_key[start:end], activation_key[start:end].upper())
        if upper_lower == "Lower":
            activation_key = activation_key.replace(activation_key[start:end], activation_key[start:end].lower())
        print(activation_key)

    elif command == "Slice":
        start = int(data[1])
        end = int(data[2])
        activation_key = activation_key.replace(activation_key[start:end], "")
        print(activation_key)
