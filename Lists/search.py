def search(lines, word):
    str_list = []
    for line in range(1, lines + 1):
        my_str = input()
        str_list.append(my_str)
    print(str_list)
    for index in range(len(str_list) - 1, -1, -1):
        if word not in str_list[index]:
            str_list.remove(str_list[index])
    print(str_list)


search(lines=int(input()), word=input())