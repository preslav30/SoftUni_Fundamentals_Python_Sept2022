def number_beggars(str_of_ints, beggars_count):
    new_list = []
    dict_sums = {}
    for num in str_of_ints.split(", "):
        new_list.append(int(num))

    for beggar in range(1, beggars_count + 1):
        suma = 0
        old_index = 0
        if beggars_count >= len(new_list):
            if beggar > len(new_list):
                suma = 0
            else:
                suma = new_list[beggar - 1]

        else:
            for index in range(len(new_list)):
                if beggar == 1 and (index == 0 or index == old_index + beggars_count):
                    old_index = index
                    suma += int(new_list[index])
                elif beggar > 1 and (index == beggar - 1 or index == old_index + beggars_count):
                    old_index = index
                    suma += int(new_list[index])
        dict_sums[beggar] = []
        dict_sums[beggar].append(suma)
        newlist = sum(list(dict_sums.values()), [])
    print(newlist)


number_beggars(str_of_ints=input(), beggars_count=int(input()))
