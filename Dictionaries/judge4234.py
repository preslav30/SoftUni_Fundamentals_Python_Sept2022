while True:
    data = input()
    if data == "no more time":
        break
    data = data.split(" -> ")
    contest = data[0]
    username = data[1]
    points = int(data[2])
    