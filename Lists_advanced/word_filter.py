def word_filter(text):
    filtered = list(filter(lambda word: len(word) % 2 == 0, text))
    return filtered


txt = input().split()
print(word_filter(txt))
