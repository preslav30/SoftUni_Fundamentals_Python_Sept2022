def get_digits(the_input):
    # digits = [d for d in the_input if d.isdigit()]
    the_input = the_input.split()
    digits = []
    for d in the_input:
        if d.isigit():
            digits.append(d)
    digits_removed = [ch for ch in the_input if ch.isalpha()]
    nums_str = "".join(digits)
    nums = int(nums_str)
    letter = chr(nums)
    digits_removed[0], digits_removed[-1] = digits_removed[-1], digits_removed[0]
    digits_removed.insert(0, letter)
    final = "".join(str(x) for x in digits_removed)
    return final


sent = input()
print(get_digits(sent))
