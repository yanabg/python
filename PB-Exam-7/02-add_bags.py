price_above_20_kg = float(input())
luggage_kg = float(input())
days_to_trip = int(input())
luggage_count = int(input())

price_increase_weight = 0
final_price = 0

# luggage weight fees:
if luggage_kg < 10:
    price_increase_weight = price_above_20_kg * 0.2
elif 10 <= luggage_kg <= 20:
    price_increase_weight = price_above_20_kg * 0.5
else:
    price_increase_weight = price_above_20_kg

# print(f'price_increase_weight is: {price_increase_weight}')

# price increase for days left to trip:
if days_to_trip < 7:
    price_increase_weight *= 1.4
elif 7 <= days_to_trip <= 30:
    price_increase_weight *= 1.15
elif days_to_trip > 30:
    price_increase_weight *= 1.10

final_price = price_increase_weight * luggage_count

print(f'The total price of bags is: {final_price:.2f} lv.')
