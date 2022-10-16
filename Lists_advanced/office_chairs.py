def office(rooms):
    chairs_count = 0
    people_count = 0
    rooms_needing_chairs = {}

    for room in range(1, rooms + 1):
        chairs_per_room_plus_visitors = input().split()
        chairs = len(chairs_per_room_plus_visitors[0])
        people = int(chairs_per_room_plus_visitors[1])
        if people > chairs:
            rooms_needing_chairs.update({room: people - chairs})
        chairs_count += chairs
        people_count += people
    if people_count > chairs_count:
        for r, ch in rooms_needing_chairs.items():
            print(f"{ch} more chairs needed in room {r}")
    else:
        print(f"Game On, {chairs_count - people_count} free chairs left")


number_of_rooms = int(input())
office(number_of_rooms)
