VIDEO_CARD_PRICE = 250

PROCESSORS_PERCENTAGE = 0.35
MEMORY_PERCENTAGE = 0.10

budget = float(input())

graphic_cards_count = int(input())
processor_count = int(input())
memory_count = int(input())

graphic_cards_price = graphic_cards_count * VIDEO_CARD_PRICE
processor_price = processor_count * graphic_cards_price * PROCESSORS_PERCENTAGE
memory_price = memory_count * graphic_cards_price * MEMORY_PERCENTAGE

total_price = graphic_cards_price + processor_price + memory_price

if graphic_cards_count > processor_count:
    total_price -= total_price * 0.15

if total_price <= budget:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
