queue = int(input())
the_input = list(map(int, input().split()))
filled_spaces_list = []
taken_spaces = 0
for wagon_spaces in range(len(the_input)):
    while the_input[wagon_spaces] < 4:
        the_input[wagon_spaces] += 1
        queue -= 1
        taken_spaces += 1
        if queue == 0 or the_input[wagon_spaces] == 4:
            break
    else:
        continue
    if queue == 0:
        break

if the_input[-1] < 4:
    spaces_are_available = True
else:
    spaces_are_available = False

for i in range(len(the_input)):
    the_input[i] = str(the_input[i])
filled_spaces_str = " ".join(the_input)

if queue == 0 and spaces_are_available:
    print(f"The lift has empty spots!\n{filled_spaces_str}")
elif queue > 0 and not spaces_are_available:
    print(f"There isn't enough space! {queue} people in a queue!\n{filled_spaces_str}")
elif queue == 0 and not spaces_are_available:
    print(filled_spaces_str)
