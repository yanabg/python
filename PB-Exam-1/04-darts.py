player_name = input()

points = 301
successful_shots = 0
unsuccessful_shots = 0

while points > 0:
    field = input()
    if field == "Retire":
        print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')
        break
    points_scored = int(input())

    if field == "Single":
        score = points_scored
    elif field == "Double":
        score = points_scored * 2
    elif field == "Triple":
        score = points_scored * 3

    if score <= points:
        points -= score
        successful_shots += 1
    else:
        unsuccessful_shots += 1

if points == 0:
    print(f"{player_name} won the leg with {successful_shots} shots.")