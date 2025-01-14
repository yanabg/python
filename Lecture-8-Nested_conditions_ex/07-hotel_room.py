month = input()
nights = int(input())
price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if 7 < nights <= 14:
        price_studio *= 0.95
    elif nights > 14:
        price_studio *= 0.70
        price_apartment *= 0.90
if month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if nights > 14:
        price_studio *= 0.80
        price_apartment *= 0.90
if month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77
    if nights > 14:
        price_apartment *= 0.90

studio_cost = price_studio * nights
apartment_cost = price_apartment * nights
print(f"Apartment: {apartment_cost:.2f} lv.")
print(f"Studio: {studio_cost:.2f} lv.")
