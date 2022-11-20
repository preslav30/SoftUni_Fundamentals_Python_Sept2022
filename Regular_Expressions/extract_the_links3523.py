import re

text_list = []
results = []
text = input()
while text:
    text_list.append(text)
    text = input()
pattern = r"(www\.[A-Za-z\d\-]+(\.[a-z]+)+)"
for sentence in text_list:
    matches = re.search(pattern, sentence)
    if matches:
        results.append(matches.group())
for i in results:
    print(i)
