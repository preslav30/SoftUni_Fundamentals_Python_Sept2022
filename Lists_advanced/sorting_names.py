def sorting(my_str):
    by_name = sorted(my_str)
    by_length = sorted(by_name, key=len, reverse=True)
    return by_length


the_str = input().split(", ")
print(sorting(the_str))

