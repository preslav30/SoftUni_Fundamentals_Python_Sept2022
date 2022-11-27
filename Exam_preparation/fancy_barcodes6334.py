import re

n = int(input())
for i in range(n):
    text = input()
    pattern = r"@#+[A-Z]{1}[a-zA-Z\d]{4,}[A-Z]{1}@#+"
    result = re.findall(pattern, text)
    if not result:
        print("Invalid barcode")
    for j in result:
        digits = ""
        for k in j:
            if k.isdigit():
                digits += k
        if not digits:
            print("Product group: 00")
        else:
            print(f"Product group: {digits}")


