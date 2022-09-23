def football(sequence):
    a_count = 0
    b_count = 0

    a = sequence.split()  # ['A-1', 'A-5', 'A-10', 'B-2']
    b = set(a)

    for i in b:
        if "A" in i:
            a_count += 1
            if a_count > 4:
                break
        elif "B" in i:
            b_count += 1
            if b_count > 4:
                break
    diff_a = 11 - a_count
    diff_b = 11 - b_count
    print(f"Team A - {diff_a}; Team B - {diff_b}")
    if diff_a < 7 or diff_b < 7:
        print("Game was terminated")


football(sequence=input())  # A-1 A-5 A-10 B-2
