contests = {}
user_points = {}  # {'Peter': {'Algo': 400, 'DS': 150}, 'George': {'Algo': 300}, 'Simo': {'Algo': 200}, 'Mariya': {'DS': 600}}
total_points = {}
while True:
    data = input()
    if data == "no more time":
        break
    data = data.split(" -> ")
    contest = data[1]
    username = data[0]  # {'OOP': {'Peter': 350, 'George': 250, 'George': 300, 'Prakash': 300}}
    points = int(data[2])
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

contests = {key: dict(sorted(val.items(), key=lambda x: (x[1], x[0]), reverse=True)) for key, val in contests.items()}
for contest, un_points in contests.items():
    print(f"{contest}: {len(contests[contest])} participants")
    count = 1
    for u, p in contests[contest].items():
        print(f"{count}. {u} <::> {p}")
        count += 1
print("Individual standings:")
count = 1
for un, cn_ps in user_points.items():
    total_points[un] = sum(cn_ps.values())
total_points = dict(sorted(total_points.items(), key=lambda x: (x[1], x[0]), reverse=True))
for k, v in total_points.items():
    print(f"{count}. {k} -> {v}")
    count += 1