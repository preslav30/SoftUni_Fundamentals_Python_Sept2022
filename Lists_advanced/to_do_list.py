def to_do(command):
    notes = [None for num in range(1, 11)]
    while command != "End":
        importance = int(command[0])
        notes[importance - 1] = importance




the_command = input().split("-")
print(to_do(the_command))