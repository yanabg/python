city = input().lower()
sales_volume = float(input())
commissions = 0
ERROR_CONDITION = False

if city == "sofia":
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.05
    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.07
    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.08
    elif sales_volume > 10000:
        commissions = sales_volume * 0.12
    else:
        ERROR_CONDITION = True
elif city == "plovdiv":
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.055
    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.08
    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.12
    elif sales_volume > 10000:
        commissions = sales_volume * 0.145
    else:
        ERROR_CONDITION = True
elif city == "varna":
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.045
    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.075
    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.10
    elif sales_volume > 10000:
        commissions = sales_volume * 0.13
    else:
        ERROR_CONDITION = True
else:
    ERROR_CONDITION = True

if not ERROR_CONDITION:
    print(f"{commissions:.2f}")
else:
    print("error")