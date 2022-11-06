count = int(input())
syn = {}
for i in range(count):
    word = input()
    synonym = input()
    if word in syn.keys():
        syn[word] += f", {synonym}"
    else:
        syn[word] = synonym

for key, value in syn.items():
    print(f"{key} - {value}")



