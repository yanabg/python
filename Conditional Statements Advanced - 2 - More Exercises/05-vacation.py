budget = float(input())
season = input()

accommodation_type = None
destination = None
price = 0

if budget <= 1000:
    accommodation_type = "Camp"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        destination = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation_type = "Hut"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        destination = "Morocco"
        price = budget * 0.60
elif budget > 3000:
    accommodation_type = "Hotel"
    price = budget * 0.90
    if season == "Summer":
        destination = "Alaska"
    elif season == "Winter":
        destination = "Morocco"

print(f'{destination} - {accommodation_type} - {price:.2f}')