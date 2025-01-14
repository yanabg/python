budget = float(input())
series_num = int(input())

total_cost = 0

for _ in range(series_num):
    name = input()
    price = float(input())

    if name == "Thrones":
        price *= 0.50
    elif name == "Lucifer":
        price *= 0.60
    elif name == "Protector":
        price *= 0.70
    elif name == "TotalDrama":
        price *= 0.80
    elif name == "Area":
        price *= 0.90

    total_cost += price

if budget >= total_cost:
    print(f'You bought all the series and left with {budget - total_cost:.2f} lv.')
else:
    print(f'You need {total_cost - budget:.2f} lv. more to buy the series!')


