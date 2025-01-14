# read input for days & hours
days = int(input())
hours = int(input())
# create total-amount counter
total_amount = 0

# loop over each day
for day in range(1, days + 1):
    total_day_amount = 0

    # Loop over each hour of the day
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_fee = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking_fee = 1.25
        else:
            parking_fee = 1

        total_day_amount += parking_fee

    # print current day total amount:
    print(f"Day: {day} - {total_day_amount:.2f} leva")

    # add day's total to total_amount
    total_amount += total_day_amount

# print total_amount (the total for all days):
print(f"Total: {total_amount:.2f} leva")
