fuel_type = str(input()).lower()
fuel_liters = float(input())

if fuel_type in ["gas", "diesel", "gasoline"]:
    if fuel_liters >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")
else:
    print(f"Invalid fuel!")
