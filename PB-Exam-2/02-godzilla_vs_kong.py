budget = float(input())
statists = int(input())
price_costume_per_statist = float(input())

decors_price = budget * 0.10
costumes_price = statists * price_costume_per_statist

if statists > 150:
    costumes_price *= 0.90

total_film_cost = decors_price + costumes_price

if total_film_cost > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {total_film_cost - budget:.2f} leva more.')
else:
    print(f'"Action!')
    print(f'Wingard starts filming with {budget - total_film_cost:.2f} leva left.')



