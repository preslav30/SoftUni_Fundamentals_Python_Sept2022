text = input()
new_text = ""
for ch in text:
    new_ch = chr(ord(ch) + 3)
    new_text += new_ch
print(new_text)