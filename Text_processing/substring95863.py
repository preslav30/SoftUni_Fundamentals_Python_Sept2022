first_str = input()
sec_str = input()
for i in sec_str:
    sec_str = sec_str.replace(first_str, "")
print(sec_str)
