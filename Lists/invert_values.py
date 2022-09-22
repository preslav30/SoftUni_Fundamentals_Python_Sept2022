def invert(my_str):
    list_in = my_str.split(" ")
    list_out = []
    for num in list_in:
        num = -int(num)
        list_out.append(num)
    return list_out


print(invert(my_str=input()))
