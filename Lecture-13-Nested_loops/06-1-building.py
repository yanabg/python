floors = int(input())
rooms = int(input())
room_name = ''

for floor in range(floors, 0, -1):
    for room in range(rooms):
        if floor == floors:
            room_name = f'L{floor}{room}'

        elif floor % 2 == 0:
            room_name = f'O{floor}{room}'

        elif floor % 2 != 0:
            room_name = f'A{floor}{room}'

        print(room_name, end=" ")

    print()