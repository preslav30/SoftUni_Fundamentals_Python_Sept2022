contests = {}
total_points = {}
while True:
    data = input()
    if data == "no more time":
        break
    data = data.split(" -> ")
    contest = data[1]
    username = data[0]
    points = int(data[2])
    if contest not in contests.keys():
        contests[contest] = []
    if username in contests[contest]:
        total_points[username][1] += points
        if points > contests[contest][1]:
            contests[contest][1] = points
    else:
        total_points[username] = [contest, points]
        contests[contest].append({username: points})

print(contests)
# for contest, un_points in contests.items():
#     print(f"")