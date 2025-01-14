
budget = float(input())
season = input().capitalize()

price = 0
place = None
destination = None

if budget <= 100:
    destination = "Bulgaria"
    price = budget * 0.3
    if season == "Summer":
        place = "Camp"
    elif season == "Winter":
        price = budget * 0.7
        place = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    price = budget * 0.4
    if season == "Summer":
        place = "Camp"
    elif season == "Winter":
        price = budget * 0.8
        place = "Hotel"
else:
    destination = "Europe"
    place = "Hotel"
    price = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")