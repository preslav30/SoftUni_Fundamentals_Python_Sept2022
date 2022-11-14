text = input()
emoticons = []
for ch in range(len(text)):
    if text[ch] == ":":
        emoticons.append(text[ch] + (text[ch + 1]))
for i in emoticons:
    print(i)