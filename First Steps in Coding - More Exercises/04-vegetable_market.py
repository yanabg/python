EUR = 1.94
vegetables_price_per_kg_bgn = float(input())
fruits_price_per_kg_bgn = float(input())

total_vegetables_kg = int(input())
total_fruits_kg = int(input())

total_bgn = total_vegetables_kg * vegetables_price_per_kg_bgn + total_fruits_kg * fruits_price_per_kg_bgn
total_income_in_eur = total_bgn / EUR

print(f"{total_income_in_eur:.2f}")
