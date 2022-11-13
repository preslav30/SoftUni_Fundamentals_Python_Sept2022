banned = input().split(", ")
text = input()
for i in banned:
    text = text.replace(i, len(i) * "*")
print(text)