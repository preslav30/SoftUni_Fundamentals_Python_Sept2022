def to_do(command):
    notes = [0 for num in range(1, 11)]
    while command != "End":
        command = command.split("-")
        note_position = int(command[0]) - 1
        note = command[1]
        notes.pop(note_position)
        notes.insert(note_position, note)
        command = input()
    notes = list(filter(lambda non_zero: non_zero != 0, notes))
    return notes


the_command = input()
print(to_do(the_command))
