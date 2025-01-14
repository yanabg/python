eggs_player_one = int(input())
eggs_player_two = int(input())

player_one_wins = 0
player_two_wins = 0
# total_eggs_player_one = 0
# total_eggs_player_two = 0

while True:
    command = input()
    if command == "one":
        eggs_player_two -= 1
        player_one_wins += 1
    elif command == "two":
        eggs_player_one -= 1
        player_two_wins += 1
    elif command == "End":
        print(f'Player one has {eggs_player_one} eggs left.')
        print(f'Player two has {eggs_player_two} eggs left.')
        break
    if eggs_player_one <= 0 < eggs_player_two:
        print(f'Player one is out of eggs. Player two has {eggs_player_two} eggs left.')
    #    print(f'Player two is out of eggs. Player one has {eggs_player_one} eggs left.')
        break
    elif eggs_player_two <= 0 < eggs_player_one:
        print(f'Player two is out of eggs. Player one has {eggs_player_one} eggs left.')
    #    print(f'Player one is out of eggs. Player two has {eggs_player_two} eggs left.')
        break
    elif eggs_player_one <= 0 and eggs_player_two <= 0:
        print(f'Player one is out of eggs. Player two is out of eggs.')
    #    print(f'Player two is out of eggs. Player one is out of eggs.')
        break