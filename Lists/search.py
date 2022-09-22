def search(lines, word):
    str_list = []
    for line in range(1, lines + 1):
        my_str = input()
        str_list.append(my_str)
    for s in str_list:
        if word not in s:
            str_list.remove(s)
        