def check(element):
    for el in element:
        if el[::-1] == el:
            print(True)
        else:
            print(False)


the_lst = input().split(", ")
check(the_lst)