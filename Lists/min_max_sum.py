def minimum(sequence):
    min_num = min(the_sequence)
    return min_num


def maximum(sequence):
    max_num = max(the_sequence)
    return max_num


def suma(sequence):
    sumata = sum(the_sequence)
    return sumata

def min_max_sum(sequence):
    print(f"The minimum number is {minimum(sequence)}\nThe maximum number is {maximum(sequence)}\nThe sum number is: {suma(sequence)}")


the_sequence = list(map(int, input().split()))
print(min_max_sum(the_sequence))

