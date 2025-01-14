movie = input()
days_num = int(input())
ticket_num = int(input())
price_per_ticket = float(input())
percent_for_cinema = int(input())

tickets_price_per_day = ticket_num * price_per_ticket
tickets_price_for_the_period = tickets_price_per_day * days_num
cinema_fee = tickets_price_for_the_period * (percent_for_cinema / 100)

income_from_movie = tickets_price_for_the_period - cinema_fee

print(f'The profit from the movie {movie} is {income_from_movie:.2f} lv.')