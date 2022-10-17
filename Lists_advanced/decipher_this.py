# second and last letter are switched
# the first letter is replaced by its character code (e.g., 72 means H)

# input 72olle 103doo 100ya
# result Hello good day


def get_digits(the_input):
    digits = [d for d in the_input if d.isdigit()]
    digits_removed = [ch for ch in the_input if ch.isalpha()]
    nums_str = "".join(digits)
    nums = int(nums_str)
    letter = chr(nums)
    digits_removed[0], digits_removed[-1] = digits_removed[-1], digits_removed[0]
    digits_removed.insert(0, letter)
    final = "".join(str(x) for x in digits_removed)
    return final


def sentence(s):
    sente = list(map(get_digits, s))
    new_str = ""
    for i in sente:
        new_str += i + " "
    return new_str


sent = input().split()
print(sentence(sent))
