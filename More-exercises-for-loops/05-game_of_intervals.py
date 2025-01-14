moves_num = int(input())

count_0_to_9 = 0
count_10_to_19 = 0
count_20_to_29 = 0
count_30_to_39 = 0
count_40_to_50 = 0
count_invalid = 0
total_points = 0

for _ in range(moves_num):
    num = int(input())

    if 0 <= num <= 9:
        count_0_to_9 += 1
        total_points += num * 0.2

    elif 10 <= num <= 19:
        count_10_to_19 += 1
        total_points += num * 0.3

    elif 20 <= num <= 29:
        count_20_to_29 += 1
        total_points += num * 0.4
    elif 30 <= num <= 39:
        count_30_to_39 += 1
        total_points += 50

    elif 40 <= num <= 50:
        count_40_to_50 += 1
        total_points += 100
    else:
        count_invalid += 1
        total_points /= 2

percent_0_to_9 = (count_0_to_9 / moves_num) * 100
percent_10_to_19 = (count_10_to_19 / moves_num) * 100
percent_20_to_29 = (count_20_to_29 / moves_num) * 100
percent_30_to_39 = (count_30_to_39 / moves_num) * 100
percent_40_to_50 = (count_40_to_50 / moves_num) * 100
percent_invalid = (count_invalid / moves_num) * 100

print(f"{total_points:.2f}")
print(f"From 0 to 9: {percent_0_to_9:.2f}%")
print(f"From 10 to 19: {percent_10_to_19:.2f}%")
print(f"From 20 to 29: {percent_20_to_29:.2f}%")
print(f"From 30 to 39: {percent_30_to_39:.2f}%")
print(f"From 40 to 50: {percent_40_to_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
