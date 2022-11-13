contest_original = {}
username_points = {}
max_points = 0
while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    contest_original[contest] = password

while True:
    command1 = input()
    if command1 == "end of submissions":
        break
    contest1, password1, username, points = command1.split("=>")
    points = int(points)
    if contest1 in contest_original.keys() and password1 == contest_original[contest1]:
        # if username in username_points.keys() and any(contest1 in nested_dict for nested_dict in username_points[username].items()):
        if username in username_points.keys() and contest1 in username_points[username].keys():
            if points > username_points[username][contest1]:
                username_points[username][contest1] = points
        elif username not in username_points.keys():
            username_points[username] = {contest1: points}

        elif username in username_points.keys() and contest1 not in username_points[username].keys():  # username_points = {username: {contest: points}, {contest, points}}
            username_points[username][contest1] = points

for each_user, contest_and_points in username_points.items():
    total = 0
    for each_contest, each_score in contest_and_points.items():
        total += each_score
        if total > max_points:
            max_points = total
            max_user = each_user
print(f"Best candidate is {max_user} with total {max_points} points.\nRanking:")

for student, nested_dict in sorted(username_points.items()):
    print(f"{student}")
    reverse_sorted = dict(sorted(nested_dict.items(), key=lambda x: x[1], reverse=True))
    for contests, pointss in reverse_sorted.items():
        print(f"#  {contests} -> {pointss}")
