movie = input()
package = input()
tickets_num = int(input())

price = 0

if movie == "John Wick":
    if package == "Drink":
        price = 12
    elif package == "Popcorn":
        price = 15
    elif package == "Menu":
        price = 19
elif movie == "Star Wars":
    if package == "Drink":
        price = 18
    elif package == "Popcorn":
        price = 25
    elif package == "Menu":
        price = 30
elif movie == "Jumanji":
    if package == "Drink":
        price = 9
    elif package == "Popcorn":
        price = 11
    elif package == "Menu":
        price = 14


if movie == "Star Wars" and tickets_num >= 4:
    price *= 0.70

if movie == "Jumanji" and tickets_num == 2:
    price *= 0.85

end_price = tickets_num * price

print(f'Your bill is {end_price:.2f} leva.')