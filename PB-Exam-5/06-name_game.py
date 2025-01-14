winner = ""
max_points = 0

while True:
    player_name = input()

    if player_name == "Stop":
        break
    player_points = 0
    name_length = len(player_name)

    for letter in range(name_length):
        number = int(input())
        if ord(player_name[letter]) == number:
            player_points += 10
        else:
            player_points += 2

    if player_points > max_points:
        max_points = player_points
        winner = player_name
    elif player_points == max_points:
        winner = player_name # update winner to the current player as the 2nd player with the same points should win

print(f'The winner is {winner} with {max_points} points!')
