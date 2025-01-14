MAX_SCORE = 20

country = input()
tool = input()

hardness = 0
performance = 0

if tool == "ribbon":
    if country == "Russia":
        hardness = 9.100
        performance = 9.400
    elif country == "Bulgaria":
        hardness = 9.600
        performance = 9.400
    elif country == "Italy":
        hardness = 9.200
        performance = 9.500
elif tool == "hoop":
    if country == "Russia":
        hardness = 9.300
        performance = 9.800
    elif country == "Bulgaria":
        hardness = 9.550
        performance = 9.750
    elif country == "Italy":
        hardness = 9.450
        performance = 9.350
elif tool == "rope":
    if country == "Russia":
        hardness = 9.600
        performance = 9.000
    elif country == "Bulgaria":
        hardness = 9.500
        performance = 9.400
    elif country == "Italy":
        hardness = 9.700
        performance = 9.150

total_score = hardness + performance
shortfall_percentage = ((MAX_SCORE - total_score) / MAX_SCORE) * 100

print(f"The team of {country} get {total_score:.3f} on {tool}.")
print(f"{shortfall_percentage:.2f}%")