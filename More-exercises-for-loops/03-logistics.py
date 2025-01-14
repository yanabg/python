# Reading the number of loads
num_loads = int(input())

# Initializing variables to store the total weight and cost for each vehicle
total_weight = 0
minibus_weight = 0
truck_weight = 0
train_weight = 0

minibus_cost = 200
truck_cost = 175
train_cost = 120

total_cost = 0

# Reading the weight of each load and calculating the corresponding costs
for _ in range(num_loads):
    load_weight = int(input())
    total_weight += load_weight

    if load_weight <= 3:
        minibus_weight += load_weight
        total_cost += load_weight * minibus_cost
    elif load_weight <= 11:
        truck_weight += load_weight
        total_cost += load_weight * truck_cost
    else:
        train_weight += load_weight
        total_cost += load_weight * train_cost

# Calculating the average cost per ton
average_cost_per_ton = total_cost / total_weight

# Calculating the percentage of loads transported by each vehicle
minibus_percentage = (minibus_weight / total_weight) * 100
truck_percentage = (truck_weight / total_weight) * 100
train_percentage = (train_weight / total_weight) * 100

# Printing the results
print(f"{average_cost_per_ton:.2f}")
print(f"{minibus_percentage:.2f}%")
print(f"{truck_percentage:.2f}%")
print(f"{train_percentage:.2f}%")
