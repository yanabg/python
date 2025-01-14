city = input()
sales_volume = float(input())

if city == "Sofia":
    if 0 <= sales_volume <= 500:
        commission = 0.05
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    elif 500 < sales_volume <= 1000:
        commission = 0.07
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    elif 1000 < sales_volume <= 10000:
        commission = 0.08
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    elif 10000 < sales_volume:
        commission = 0.12
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    else:
        print("error")

elif city == "Varna":
    if 0 <= sales_volume <= 500:
        commission = 0.045
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    elif 500 < sales_volume <= 1000:
        commission = 0.075
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    elif 1000 < sales_volume <= 10000:
        commission = 0.10
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    elif 10000 < sales_volume:
        commission = 0.13
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    else:
        print("error")

elif city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        commission = 0.055
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    elif 500 < sales_volume <= 1000:
        commission = 0.08
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    elif 1000 < sales_volume <= 10000:
        commission = 0.12
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    elif 10000 < sales_volume:
        commission = 0.145
        commission_amount = sales_volume * commission
        print(f"{commission_amount:.2f}")
    else:
        print("error")
else:
    print("error")
