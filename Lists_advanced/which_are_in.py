def which_are_in(seq1, seq2):
    appeared = []
    for sub1 in seq1:
        for sub2 in seq2:
            if sub1 in sub2:
                appeared.append(sub1)
                break
    return appeared


sequence1 = input().split(", ")
sequence2 = input().split(", ")
print(which_are_in(sequence1, sequence2))
