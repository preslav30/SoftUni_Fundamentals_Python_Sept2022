def fire(fires, water):
    total_effort = 0
    total_fire = 0
    put_out = []
    for each_fire in fires:  # ['High = 89', 'Low = 28', 'Medium = 77', 'Low = 23']
        each_fire = each_fire.split(" = ")  # ['High', '89']
        level = int(each_fire[1])
        if 81 <= level <= 125 and each_fire[0] == "High":
            if water < level:
                continue
            else:
                water -= level
                effort = 0.25 * level
                total_effort += effort
                total_fire += level
                put_out.append(level)
        elif 51 <= level <= 80 and each_fire[0] == "Medium":
            if water < level:
                continue
            else:
                water -= level
                effort = 0.25 * level
                total_effort += effort
                total_fire += level
                put_out.append(level)
        elif 1 <= level <= 50 and each_fire[0] == "Low":
            if water < level:
                continue
            else:
                water -= level
                effort = 0.25 * level
                total_effort += effort
                total_fire += level
                put_out.append(level)
        else:
            continue
    print(f"Cells: ")
    for item in put_out:
        print(f" - {item}")
    print(f"Effort: {total_effort:.2f}")
    print(f"Total Fire: {total_fire}")


fire(fires=input().split("#"), water=int(input()))