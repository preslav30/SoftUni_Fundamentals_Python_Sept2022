text = input()
digits = ""
letters = ""
others = ""
for i in text:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        others += i


print(f"{digits}\n{letters}\n{others}")
