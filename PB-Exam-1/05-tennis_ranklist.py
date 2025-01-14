from math import floor

tournament_count = int(input())
initial_points = int(input())

total_points = initial_points
points_earned = 0
won = 0

for _ in range(tournament_count):
    end_position = input()

    if end_position == "W":
        points_earned += 2000
        won += 1
    elif end_position == "F":
        points_earned += 1200
    elif end_position == "SF":
        points_earned += 720

total_points += points_earned
average_points = points_earned / tournament_count
percent_won = (won / tournament_count) * 100

print(f'Final points: {total_points}')
print(f'Average points: {floor(average_points)}')
print(f'{percent_won:.2f}%')





