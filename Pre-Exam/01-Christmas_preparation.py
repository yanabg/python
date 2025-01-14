PAPER_PRICE_PER_ITEM = 5.80
CLOTH_PRICE_PER_ITEM = 7.20
GLUE_PRICE_PER_ITEM = 1.20

paper_roll_count = int(input())
clot_roll_count = int(input())
glue_liters = float(input())
discount = int(input())

paper_price = paper_roll_count * PAPER_PRICE_PER_ITEM
cloth_price = clot_roll_count * CLOTH_PRICE_PER_ITEM
glue_price = glue_liters * GLUE_PRICE_PER_ITEM

total_price_before_discount = paper_price + cloth_price + glue_price

total_price_after_discount = total_price_before_discount * (1-discount/100)

print(f'{total_price_after_discount:.3f}')