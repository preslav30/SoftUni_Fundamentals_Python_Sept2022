words = input().split()
dct = {}
for word in words:
    lower = word.lower()
    if lower not in dct:
        dct[lower] = 0
    dct[lower] += 1
for key, value in dct.items():
    if value % 2 != 0:
        print(key, end=" ")