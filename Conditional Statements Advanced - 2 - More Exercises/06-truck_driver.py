season = input()
kilometers = float(input())

price_km = 0
total_earnings = 0

if kilometers <= 5000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.75
    elif season == "Summer":
        price_km = 0.90
    elif season == "Winter":
        price_km = 1.05
elif 5000 < kilometers <= 10000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.95
    elif season == "Summer":
        price_km = 1.10
    elif season == "Winter":
        price_km = 1.25
elif 10000 < kilometers <= 20000:
    price_km = 1.45

total_earnings = kilometers * price_km * 4
total_earnings_after_taxes = total_earnings * 0.9

print(f'{total_earnings_after_taxes:.2f}')