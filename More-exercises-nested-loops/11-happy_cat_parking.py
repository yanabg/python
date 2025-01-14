days = int(input())
hours = int(input())

total_amount = 0

for day in range(1, days + 1):
    total_daily_amount = 0

    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_fee = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking_fee = 1.25
        else:
            parking_fee = 1

        total_daily_amount += parking_fee

    print(f'Day: {day} - {total_daily_amount:.2f} leva')

    total_amount += total_daily_amount

print(f'Total: {total_amount:.2f} leva')
