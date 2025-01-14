tournament_days = int(input())

total_amount = 0
wins = 0
losses = 0

for _ in range(tournament_days):
    daily_amount = 0
    daily_wins = 0
    daily_losses = 0

    while True:
        sport = input()
        if sport == "Finish":
            break
        result = input()
        if result == "win":
            daily_wins += 1
            daily_amount += 20
        elif result == "lose":
            daily_losses += 1

    if daily_wins > daily_losses:
        daily_amount *= 1.10
        wins += 1
    else:
        losses += 1

    total_amount += daily_amount

if wins > losses:
    total_amount *= 1.20
    print(f'You won the tournament! Total raised money: {total_amount:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_amount:.2f}')









