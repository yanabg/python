
total_games = 0
won_games = 0
lost_games = 0

while True:
    tournament = input()

    if tournament == "End of tournaments":
        break

    games_num = int(input())

    for game_number in range(1, games_num + 1):
        score_team_Desi = int(input())
        score_team_others = int(input())

        total_games += 1

        if score_team_Desi > score_team_others: # Desi wins
            won_games += 1
            difference = score_team_Desi - score_team_others
            print(f'Game {game_number} of tournament {tournament}: win with {difference} points.')
        else:
            lost_games += 1
            difference = score_team_others - score_team_Desi
            print(f'Game {game_number} of tournament {tournament}: lost with {difference} points.')

percent_won = (won_games / total_games) * 100
percent_lost = (lost_games / total_games) * 100

# Print %-s
print(f'{percent_won:.2f}% matches win')
print(f'{percent_lost:.2f}% matches lost')