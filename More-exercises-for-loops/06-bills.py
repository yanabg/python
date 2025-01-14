WATER = 20
INET = 15

months = int(input())

electricity_cost = 0

for _ in range(months):
    electricity_bill = float(input())
    electricity_cost += electricity_bill

water_cost = months * WATER
inet_cost = months * INET
other_costs = 1.20 * (electricity_cost +\
                          water_cost +\
                          inet_cost)
average = (other_costs + electricity_cost + water_cost + inet_cost) / months

print(f'Electricity: {electricity_cost:.2f} lv')
print(f'Water: {water_cost:.2f} lv')
print(f'Internet: {inet_cost:.2f} lv')
print(f'Other: {other_costs:.2f} lv')
print(f'Average: {average:.2f} lv')