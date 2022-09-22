def statistics(lines):
    pos = []
    neg = []
    count_positives = 0
    for line in range(1, lines + 1):
        my_int = int(input())
        if my_int < 0:
            neg.append(my_int)
        else:
            pos.append(my_int)
            count_positives += 1
    sum_of_negatives = sum(neg)
    print(pos)
    print(neg)
    print(f"Count of positives: {count_positives}\nSum of negatives: {sum_of_negatives}")


statistics(lines=int(input()))