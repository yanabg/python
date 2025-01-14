n = int(input())

total_sum = 0

# Loop to read each integer and add it to the total_sum
for _ in range(n):
    number = int(input())
    total_sum += number

# Calculate the average
average = total_sum / n

print(f"{average:.2f}")
