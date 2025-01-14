trumpets_num = int(input())

max_score = 0
best_baker = None

for _ in range(trumpets_num):
    baker_name = input()
    total_points = 0

    while True:
        score = input()
        if score == "Stop":
            break
        total_points += int(score)

    print(f'{baker_name} has {total_points} points.')

    if total_points > max_score:
        max_score = total_points
        best_baker = baker_name
        print(f'{baker_name} is the new number 1!')

print(f'{best_baker} won competition with {max_score} points!')


