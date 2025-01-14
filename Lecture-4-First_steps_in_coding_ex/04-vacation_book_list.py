book_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

total_time_to_read_the_book = book_pages / pages_per_hour
needed_hours_per_day = round(total_time_to_read_the_book / number_of_days)

print(needed_hours_per_day)
