computers = int(input())

total_sales = 0
total_score = 0

for _ in range(computers):
    number = int(input())
    rating = number % 10 # get last digit to define the rating
    possible_sales = number // 10 # integer division by 10 to get possible sales (hundreds ans tens of the number represent the possible sales

    #calculate actual sales, based on the ratings:
    if rating == 2:
        actual_sales = 0
    elif rating == 3:
        actual_sales = 0.50 * possible_sales
    elif rating == 4:
        actual_sales = 0.70 * possible_sales
    elif rating == 5:
        actual_sales = 0.85 * possible_sales
    elif rating == 6:
        actual_sales = possible_sales

    total_sales += actual_sales
    total_score += rating

average_rating = total_score / computers

print(f'{total_sales:.2f}')
print(f'{average_rating:.2f}')