text = input()
new_raw_password = text

while True:
    data = input()
    if data == "Done":
        break
    data = data.split()
    command = data[0]
    if command == "TakeOdd":
        current_pass = ""
        for i in range(len(new_raw_password)):
            if i % 2 != 0:
                current_pass += new_raw_password[i]
        new_raw_password = current_pass
        print(new_raw_password)
    elif command == "Cut":
        index, length = data[1], data[2]
        index = int(index)
        length = int(length)
        new_raw_password = new_raw_password.replace(new_raw_password[index:index + length], "", 1)
        print(new_raw_password)
    elif command == "Substitute":
        substring, substitute = data[1], data[2]
        if substring in new_raw_password:
            new_raw_password = new_raw_password.replace(substring, substitute)
            print(new_raw_password)
        else:
            print("Nothing to replace!")
print(f"Your password is: {new_raw_password}")
