str1, str2 = input().split()
total = 0
if len(str1) >= len(str2):
    for char1 in range(len(str2)):
        total += ord(str2[char1]) * ord(str1[char1])
    for ch in range(len(str1) - 1, len(str2) - 1, -1):
        total += ord(str1[ch])

if len(str2) > len(str1):
    for char1 in range(len(str1)):
        total += ord(str2[char1]) * ord(str1[char1])
    for ch in range(len(str2) - 1, len(str1) - 1, -1):
        total += ord(str2[ch])
print(total)