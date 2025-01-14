price_1_sqm = 7.61
discounted_price_sqm = price_1_sqm * 0.82
discount = 0.18
sqm_needed = float(input())

total_price_before_discount = price_1_sqm * sqm_needed
discount_amount = discount * total_price_before_discount

end_price: float = sqm_needed * discounted_price_sqm
discounted_amount: float = total_price_before_discount - discount_amount

print(f"The final price is: {end_price} lv.")
print(f"The discount is: {discount_amount} lv.")

