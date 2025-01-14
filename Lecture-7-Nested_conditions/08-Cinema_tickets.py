day = input().lower()

if day in ["monday", "tuesday", "friday"]:
    price = 12
    print(price)

elif day in ["wednesday", "thursday"]:
    price = 14
    print(price)

elif day in ["saturday", "sunday"]:
    price = 16
    print(price)

