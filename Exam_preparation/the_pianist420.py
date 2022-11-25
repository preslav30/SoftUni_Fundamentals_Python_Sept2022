number_of_pieces = int(input())
piece_composer_key = {}

for i in range(number_of_pieces):
    piece, composer, key = input().split("|")
    piece_composer_key[piece] = [composer, key]


while True:
    command = input()
    if command == "Stop":
        break
    command = command.split("|")
    action = command[0]
    piece_from_command = command[1]
    if action == "Add":
        composer_from_command = command[2]
        key_from_command = command[3]
        if piece_from_command in piece_composer_key.keys():
            print(f"{piece_from_command} is already in the collection!")
            continue
        piece_composer_key[piece_from_command] = [composer_from_command, key_from_command]
        print(f"{piece_from_command} by {composer_from_command} in {key_from_command} added to the collection!")
    elif action == "Remove":
        if piece_from_command in piece_composer_key.keys():
            del piece_composer_key[piece_from_command]
            print(f"Successfully removed {piece_from_command}!")
            continue
        print(f"Invalid operation! {piece_from_command} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = command[2]
        if piece_from_command in piece_composer_key.keys():
            piece_composer_key[piece_from_command][1] = new_key
            print(f"Changed the key of {piece_from_command} to {new_key}!")
        else:
            print(f"Invalid operation! {piece_from_command} does not exist in the collection.")
# final_dict = dict(sorted(piece_composer_key.items()))
for key, value in piece_composer_key.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
