targets_sequence = list(map(int, input().split()))
indexes = input()
shots = 0
while indexes != "End":

    index = int(indexes)
    if index > len(targets_sequence) - 1:
        indexes = input()
        continue
    if targets_sequence[index] == -1:
        indexes = input()
        continue
    current_target = targets_sequence[index]
    targets_sequence[index] = -1
    shots += 1
    for i in range(len(targets_sequence)):
        if targets_sequence[i] == -1:
            continue
        if targets_sequence[i] > current_target:
            targets_sequence[i] -= current_target
        elif targets_sequence[i] <= current_target:
            targets_sequence[i] += current_target
    indexes = input()

targets_str = [str(x) for x in targets_sequence]
targets_str = " ".join(targets_str)
print(f"Shot targets: {shots} -> {targets_str}")
