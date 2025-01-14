OIL_PRICE_PER_LITER = 2.10
GUIDE_PRICE = 100
SATURDAY_DISCOUNT = 0.10
SUNDAY_DISCOUNT = 0.20

budget = float(input())
oil_liters_needed = float(input())
day = input()

final_costs = 0

oil_cost = oil_liters_needed * OIL_PRICE_PER_LITER
total_cost_before_discounts = oil_cost + GUIDE_PRICE

# print(f'oil cost: {oil_cost}')
# print(f'cost before disc: {total_cost_before_discounts}')

if day == "Saturday":
    final_costs = total_cost_before_discounts * (1 - SATURDAY_DISCOUNT)
elif day == "Sunday":
    final_costs = total_cost_before_discounts * (1 - SUNDAY_DISCOUNT)

if final_costs <= budget:
    print(f'Safari time! Money left: {budget - final_costs:.2f} lv.')
elif final_costs > budget:
    print(f'Not enough money! Money needed: {final_costs - budget:.2f} lv.')