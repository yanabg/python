budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_extra_costs = int(input())

if nights > 7:
    price_per_night *= 0.95

total_cost_for_bed = nights * price_per_night
additional_costs = budget * (percent_extra_costs / 100)
total_cost = total_cost_for_bed + additional_costs

# print(total_cost_for_bed)
# print(additional_costs)
# print(total_cost)

if budget >= total_cost:
    print(f'Ivanovi will be left with {budget - total_cost:.2f} leva after vacation.')
else:
    print(f'{total_cost - budget:.2f} leva needed.')