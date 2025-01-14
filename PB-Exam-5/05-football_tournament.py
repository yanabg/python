team_name = input()
played_games = int(input())

current_points = 0
total_points = 0
wins = 0
losses = 0
equal = 0

for _ in range(played_games):
    game_result = input()

    if game_result == "W":
        current_points = 3
        total_points += current_points
        wins += 1
    elif game_result == "D":
        current_points = 1
        total_points += current_points
        equal += 1
    elif game_result == "L":
        current_points = 0
        losses += 1

if played_games == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    win_rate = (wins / played_games) * 100
    print(f'{team_name} has won {total_points} points during this season.')
    print(f'Total stats:')
    print(f'## W: {wins}')
    print(f'## D: {equal}')
    print(f'## L: {losses}')
    print(f'Win rate: {win_rate:.2f}%')
