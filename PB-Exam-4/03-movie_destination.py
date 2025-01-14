budget = float(input())
destination = input()
season = input()
days_num = int(input())

if season == "Winter":
    if destination == "Dubai":
        price = 45000 * 0.70
    elif destination == "Sofia":
        price = 17000 * 1.25
    elif destination == "London":
        price = 24000
elif season == "Summer":
    if destination == "Dubai":
        price = 40000 * 0.70
    elif destination == "Sofia":
        price = 12500 * 1.25
    elif destination == "London":
        price = 20250

total_cost = days_num * price

if budget >= total_cost:
    print(f'The budget for the movie is enough! We have {budget - total_cost:.2f} leva left!')
else:
    print(f'The director needs {total_cost - budget:.2f} leva more!')
