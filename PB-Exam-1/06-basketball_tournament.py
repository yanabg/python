# Initiate counters:
total_games = 0
won_games = 0
lost_games = 0

while True:
    # Read tournament name :
    tournament = input()
    if tournament == "End of tournaments":
        break

    # Read games number in current tournament
    games_number = int(input())

    # For each game we read the points for each team
    for game_number in range(1, games_number + 1):
        points_scored_desi = int(input())
        points_scored_others = int(input())

        # Increase the counter for counting all games played
        total_games += 1

        if points_scored_desi > points_scored_others: # Desi's team won
            won_games += 1
            difference = points_scored_desi - points_scored_others
            print(f'Game {game_number} of tournament {tournament}: win with {difference} points.')
        else: # Desi's team does not win
            lost_games += 1
            difference = points_scored_others - points_scored_desi
            print(f'Game {game_number} of tournament {tournament}: lost with {difference} points.')

# calculate % wins and % losses:
percent_won = (won_games / total_games) * 100
percent_lost = (lost_games / total_games) * 100

# Print %-s
print(f'{percent_won:.2f}% matches win')
print(f'{percent_lost:.2f}% matches lost')

