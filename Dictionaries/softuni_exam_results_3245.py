# {
# username1: {language1: points1, language2: points2},
# username2: [language3: points3,
#             language4: points4]
# }
languages = {}
my_dict = {}
while True:
    command = input()
    if command == "exam finished":
        break
    if len(command.split("-")) < 3:
        del my_dict[command.split("-")[0]]
    else:
        username, language, points = command.split("-")

        if language not in languages.keys():
            languages[language] = 0
        if username in my_dict.keys():
            if language in my_dict[username]:
                if int(points) > int(my_dict[username][language]):
                    my_dict[username][language] = int(points)
            else:
                my_dict[username][language] = int(points)
        else:
            my_dict[username] = {language: int(points)}
        languages[language] += 1
print("Results:")
for user, nested_dict in my_dict.items():
    for language, pointss in nested_dict.items():
        print(f"{user} | {pointss}")

print(f"Submissions:")
for lang, p in languages.items():
    print(f"{lang} - {p}")

