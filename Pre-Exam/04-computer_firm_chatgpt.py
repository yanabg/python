# Read the number of computer models
n = int(input())

total_sales = 0.0
total_rating = 0

for _ in range(n):
    number = int(input())
    rating = number % 10
    possible_sales = number // 10

    if rating == 2:
        actual_sales = 0
    elif rating == 3:
        actual_sales = 0.5 * possible_sales
    elif rating == 4:
        actual_sales = 0.7 * possible_sales
    elif rating == 5:
        actual_sales = 0.85 * possible_sales
    elif rating == 6:
        actual_sales = 1.0 * possible_sales

    total_sales += actual_sales
    total_rating += rating

# Calculate the average rating
average_rating = total_rating / n

# Print the results
print(f"{total_sales:.2f}")
print(f"{average_rating:.2f}")
