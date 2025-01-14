deposit_amount = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())/100

amount = deposit_amount + deposit_term * ((deposit_amount * annual_interest_rate)/12)

print(amount)
