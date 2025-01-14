tournaments_count = int(input())
initial_points = int(input())

total_points = initial_points
won = 0

for _ in range(tournaments_count):
    end_position = input()

    if end_position == "W":
        total_points += 2000
        won += 1
    elif end_position == "F":
        total_points += 1200
    elif end_position == "SF":
        total_points += 720

average_points = (total_points - initial_points) / tournaments_count
percentage_won = (won / tournaments_count) * 100

print(f'Final points: {total_points}')
print(f'Average points: {int(average_points)}')
print(f'{percentage_won:.2f}%')


