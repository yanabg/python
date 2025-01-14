company_name = input()
adult_tickets = int(input())
kids_tickets = int(input())
ticket_price_adult = float(input())
service_fee = float(input())

ticket_price_kid = (0.30 * ticket_price_adult) + service_fee
ticket_price_adult = ticket_price_adult + service_fee

total_price_tickets = adult_tickets * ticket_price_adult + kids_tickets * ticket_price_kid

profit = 0.20 * total_price_tickets

print(f'The profit of your agency from {company_name} tickets is {profit:.2f} lv.')