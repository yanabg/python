BITCOIN_TO_BGN = 1168
CNY_TO_USD = 0.15
USD_TO_BGN = 1.76
EUR_TO_BGN = 1.95

bitcoin_count = int(input())
yuan_count = float(input())
commission_percent = float(input())

# calc the total in BGN:
total_bgn = bitcoin_count * BITCOIN_TO_BGN
total_bgn += yuan_count * CNY_TO_USD * USD_TO_BGN

# calc commission:
commission = total_bgn * (commission_percent / 100)

# calc final amount int EUR:
final_bgn = total_bgn - commission
final_eur = final_bgn / EUR_TO_BGN

print(f'{final_eur:.2f}')
