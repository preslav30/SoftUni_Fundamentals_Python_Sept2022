def survival(list_of_integers, count_of_numbers_to_remove):
    all_int = list(map(int, list_of_integers))
    for number in range(1, count_of_numbers_to_remove + 1):
        min_num = min(all_int)
        all_int.remove(min_num)
    all_str = map(str, all_int)

    return ", ".join(all_str)



print(survival(list_of_integers=input().split(), count_of_numbers_to_remove=int(input())))