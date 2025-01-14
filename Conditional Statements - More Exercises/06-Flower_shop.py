from math import ceil, floor

PRICE_MAGNOLIA = 3.25
PRICE_ZJUMBJUL = 4
PRICE_ROSE = 3.5
PRICE_KAKTUS = 8
TAX_RATE = 0.05

magnolia_count = int(input())
zjumbjul_count = int(input())
rose_count = int(input())
kaktus_count = int(input())
gift_price = float(input())

total_income_from_flowers = (
        magnolia_count * PRICE_MAGNOLIA +
        zjumbjul_count * PRICE_ZJUMBJUL +
        rose_count * PRICE_ROSE +
        kaktus_count * PRICE_KAKTUS
)
# print(f"total income is: {total_income_from_flowers}")

taxes = total_income_from_flowers * TAX_RATE
profit = total_income_from_flowers - taxes

# print(f"taxes are: {taxes:.2f}")
# print(f"profit is : {profit:.2f}")
# print(f"gift costs: {gift_price}")



if profit >= gift_price:
    excess_amount = floor(profit - gift_price)
    print(f"She is left with {excess_amount} leva.")
else:
    insufficient_amount = ceil(abs(profit - gift_price))
    print(f"She will have to borrow {insufficient_amount} leva.")
