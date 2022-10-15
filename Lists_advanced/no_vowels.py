def vowels(txt):
    vowels_list = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
    txt_filtered = [char for char in txt if char not in vowels_list]
    return txt_filtered


text = input().split()
print(vowels(text))
