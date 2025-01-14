male_num = int(input())
female_num = int(input())
tables_max_num = int(input())

for male in range(1, male_num+1):
    for female in range(1, female_num + 1):
        if tables_max_num == 0:
            break
        print(f'({male} <-> {female})', end=" ")
        tables_max_num -= 1
        if male == male_num and female == female_num:
            break