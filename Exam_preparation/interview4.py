words = "cat, horse, sweater, schoolbus, shark, cat, cat, horse, shark, shark, shark"
words = words.split(", ")

# occurrences = dict((i, words.count(i)) for i in words)
# for word, occurrence in occurrences.items():
#     print(f"{word} |" + "*" * occurrence)


occurrences = {}
for i in words:
    occurrences[i] = words.count(i)
for word, occurrence in occurrences.items():
    print(f"{word} |" + "*" * occurrence) 
