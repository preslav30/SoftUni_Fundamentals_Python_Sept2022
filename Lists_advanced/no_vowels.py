def vowels(txt):
    vowels_list = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
    txt_filtered = list(filter(lambda char: char not in vowels_list, txt))
    return "".join(txt_filtered)


text = input()
print(vowels(text))
