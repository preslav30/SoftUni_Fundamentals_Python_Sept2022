contests = {}
user_points = {}            # {username: {contest: points, contest: points}, username: {contest: points}}
while True:
    data = input()
    if data == "no more time":
        break
    data = data.split(" -> ")
    contest = data[1]
    username = data[0]        # {'OOP': {'Peter': 350, 'George': 250, 'George': 300, 'Prakash': 300}}
    points = int(data[2])     # {'OOP': [{'Peter': 350}, {'George': 250}, {'George': 300}, {'Prakash': 300}]}
    if contest not in contests.keys():
        contests[contest] = {}

    if username not in user_points.keys():
        user_points[username] = {}
    if contest not in user_points[username].keys():
        user_points[username][contest] = points
    else:
        if points > user_points[username][contest]:
            user_points[username][contest] = points
    if username in contests[contest].keys():
        if points > contests[contest][username]:
            contests[contest][username] = points
    else:
        contests[contest][username] = points
print(contests)
print(user_points)
# for contest, un_points in contests.items():
#     print(f"")