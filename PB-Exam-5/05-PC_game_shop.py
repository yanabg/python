sold_games = int(input())

counter_hearthstone = 0
counter_fornite = 0
counter_overwatch = 0
counter_others = 0

for _ in range(sold_games):
    game_title = input()

    if game_title == "Hearthstone":
        counter_hearthstone += 1
    elif game_title == "Fornite":
        counter_fornite += 1
    elif game_title == "Overwatch":
        counter_overwatch += 1
    else:
        counter_others += 1

print(f'Hearthstone - {(counter_hearthstone / sold_games) * 100:.2f}%')
print(f'Fornite - {(counter_fornite / sold_games) * 100:.2f}%')
print(f'Overwatch - {(counter_overwatch / sold_games) * 100:.2f}%')
print(f'Others - {(counter_others / sold_games) * 100:.2f}%')

