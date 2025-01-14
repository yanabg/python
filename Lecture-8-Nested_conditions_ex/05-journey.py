import random


budget = float(input())
season = input().capitalize()

costs = 0
destination = ""

vacation_type = ["Camp", "Hotel"]
# vacation = random.choice(vacation_type)

if budget <= 100:
    if season == "Summer":
        destination = "Bulgaria"
        vacation_type = "Camp"
        costs = budget * 0.30
    elif season == "Winter":
        destination = "Bulgaria"
        vacation_type = "Hotel"
        costs = budget * 0.7
elif 100 < budget <= 1000:
    if season == "Summer":
        destination = "Balkans"
        vacation_type = "Camp"
        costs = budget * 0.40
    elif season == "Winter":
        destination = "Balkans"
        vacation_type = "Hotel"
        costs = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    vacation_type = "Hotel"
    costs = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {costs:.2f}")