def sorting(sequence):
    lst = sorted([int(num) for num in sequence])
    return lst

the_sequence = input().split()
print(sorting(the_sequence))