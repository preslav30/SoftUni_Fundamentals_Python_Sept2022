my_str = input()
str_dict = {}
for ch in my_str:
    if ch == " ":
        continue
    else:
        if ch in str_dict:
            str_dict[ch] += 1
        else:
            str_dict[ch] = 1
for key, value in str_dict.items():
    print(f"{key} -> {value}")
