players = {}   # {player: {position: skill, position: skill, position: skill} }
total_points = {}
while True:
    data = input()
    if data == "Season end":
        break
    if " -> " in data:
        data = data.split(" -> ")
        player = data[0]
        position = data[1]
        skill = int(data[2])
        if player not in players.keys():
            players[player] = {position: skill}
        else:
            if position not in players[player].keys():
                players[player][position] = skill
            if skill > players[player][position]:
                players[player][position] = skill
    elif " vs " in data:
        data = data.split(" vs ")
        player1 = data[0]
        player2 = data[1]
        if player1 in players and player2 in players:
            match_found = False
            p1_sum = sum(players[player1].values())
            p2_sum = sum(players[player2].values())
            for pos1 in players[player1].keys():
                for pos2 in players[player2].keys():
                    if pos1 == pos2:
                        match_found = True
                        if p1_sum > p2_sum:
                            del players[player2]
                        elif p2_sum > p1_sum:
                            del players[player1]
                        break
                if match_found:
                    break
for k, v in players.items():
    total_points[k] = sum(v.values())
total_points = dict(sorted(total_points.items(), key=lambda x: x[1], reverse=True))
players = {key: dict(sorted(val.items(), key=lambda x: x[1], reverse=True)) for key, val in players.items()}
for player, tot in total_points.items():
    print(f"{player}: {tot} skill")
    for pos, skill in players[player].items():
        print(f"- {pos} <::> {skill}")
