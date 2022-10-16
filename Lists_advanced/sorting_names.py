def sorting(my_str):
    sorted_list = sorted(my_str, key=len, reverse=True)
    return sorted_list


the_str = input().split(", ")
print(sorting(the_str))

