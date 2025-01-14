guests_count = int(input())
price_person = float(input())
budget = float(input())

# Calculate cake price (10% of the budget)
cake_price = budget * 0.10

# Apply discounts based on number of guests
if 10 <= guests_count <= 15:
    price_person *= 0.85
elif 15 < guests_count <= 20:
    price_person *= 0.80
elif guests_count > 20:
    price_person *= 0.75

# Calculate total cost
cost = guests_count * price_person + cake_price

# Compare cost with budget and print result
if budget >= cost:
    print(f"It is party time! {budget - cost:.2f} leva left.")
else:
    print(f"No party! {cost - budget:.2f} leva needed.")
