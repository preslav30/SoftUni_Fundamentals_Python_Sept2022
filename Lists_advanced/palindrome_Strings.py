def palindrome_count(my_str):
    pals = list(filter(lambda pal: pal == pal[::-1], my_str))
    return pals


def palindrome_occurrence(my_str, pal):
    count = my_str.count(pal)
    return count


words = input().split()
palin = input()

print(palindrome_count(words))
print(f"Found palindrome {palindrome_occurrence(words, palin)} times")
