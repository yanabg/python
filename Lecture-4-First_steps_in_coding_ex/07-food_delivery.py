chicken_menu = 10.35
fish_menu = 12.40
veggie_menu = 8.15
delivery_price = 2.50

num_chicken = int(input())
num_fish = int(input())
num_veggie = int(input())

price_menus = num_chicken * chicken_menu + num_fish * fish_menu + num_veggie * veggie_menu
price_with_cake = 1.2 * price_menus

total_cost = price_with_cake + delivery_price

print(total_cost)