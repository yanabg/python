player_one, player_two = input(), input()

points_player_one = 0
points_player_two = 0

game_end = False

while not game_end:
    command = input()
    if command == "End of game":
        print(f'{player_one} has {points_player_one} points')
        print(f'{player_two} has {points_player_two} points')
        game_end = True
    else:
        card_player_one = int(command)
        card_player_two = int(input())

    if card_player_one > card_player_two:
        points_player_one += card_player_one - card_player_two
    elif card_player_two > card_player_one:
        points_player_two += card_player_two - card_player_one
    else:
        print("Number wars!")
        card_player_one = int(input())
        card_player_two = int(input())
        if card_player_one > card_player_two:
            print(f'{player_one} is winner with {points_player_one} points')
        else:
            print(f'{player_two} is winner with {points_player_two} points')
        game_end = True
