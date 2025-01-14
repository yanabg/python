coins_1 = int(input())
coins_2 = int(input())
banknotes_5 = int(input())
target_amount = int(input())

combinations_count = 0

for one in range(coins_1 + 1):
    for two in range(coins_2 + 1):
        for note in range(banknotes_5 + 1):
            total = one * 1 + two * 2 + note * 5
            if total == target_amount:
                combinations_count += 1
                print(f'{one} * 1 lv. + {two} * 2 lv. + {note} * 5 lv. = {target_amount} lv.')

if combinations_count == 0:
    print("No valid combinations")
