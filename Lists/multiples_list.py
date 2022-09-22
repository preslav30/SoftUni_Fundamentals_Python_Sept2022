def multiples(factor, count):
    my_list = []
    for i in range(1, count + 1):
        num = i * factor
        if num < 0:
            continue
        else:
            my_list.append(num)

    return my_list


print(multiples(factor=int(input()), count=int(input())))