from math import ceil

people_num = int(input())
entrance_fee = float(input())
price_per_lounge = float(input())
price_per_umbrella = float(input())

cost_entrance_fee = people_num * entrance_fee

people_wishing_lounge = ceil(people_num * 0.75)
cost_for_lounges = people_wishing_lounge * price_per_lounge

umbrellas_needed = ceil(people_num * 0.50)
cost_for_umbrellas = umbrellas_needed * price_per_umbrella

end_price = cost_entrance_fee +\
            cost_for_lounges +\
            cost_for_umbrellas
print(f'{end_price:.2f} lv.')

