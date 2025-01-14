capacity = int(input())
fans_num = int(input())
fans_a, fans_b, fans_v, fans_g = 0, 0, 0, 0
visiting_fans = 0

for _ in range(fans_num):
    sector = input()
    if sector == "A":
        fans_a += 1
        visiting_fans += 1
    elif sector == "B":
        fans_b += 1
        visiting_fans += 1
    elif sector == "V":
        fans_v += 1
        visiting_fans += 1
    elif sector == "G":
        fans_g += 1
        visiting_fans += 1

    if visiting_fans > capacity:
        break

sector_a_percent = fans_a / fans_num * 100
sector_b_percent = fans_b / fans_num * 100
sector_v_percent = fans_v / fans_num * 100
sector_g_percent = fans_g / fans_num * 100
all_percent = fans_num / capacity * 100

print(f'{sector_a_percent:.2f}%')
print(f'{sector_b_percent:.2f}%')
print(f'{sector_v_percent:.2f}%')
print(f'{sector_g_percent:.2f}%')
print(f'{all_percent:.2f}%')

# test input 76 10 A V V V G B A V B B
# test input 93 16 A V G G B B G B A B B B A B B A
# test input 1000 12 A A V V A G A A V G V A