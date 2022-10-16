def new_version(old_version):
    first = old_version[0]
    second = old_version[1]
    third = old_version[2]

    if third < 9:
        third += 1
    else:
        third = 0
        if second < 9:
            second += 1
        else:
            second = 0
            first += 1

    return f"{first}.{second}.{third}"


version = list(map(int, input().split(".")))
print(new_version(version))
