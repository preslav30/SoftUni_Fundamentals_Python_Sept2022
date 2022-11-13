usernames = input().split(", ")
for i in usernames:
    is_not = False
    if 3 <= len(i) <= 16:
        for j in i:
            if (not j.isalnum() and j != "-" and j != "_") or " " in i:
                is_not = True
                break


    else:
        continue
    if not is_not:
        print(i)



