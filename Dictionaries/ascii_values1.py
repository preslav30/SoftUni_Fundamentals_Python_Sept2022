chars = input().split(", ")
chars_dictionary = {key: ord(key) for key in chars}
print(chars_dictionary)