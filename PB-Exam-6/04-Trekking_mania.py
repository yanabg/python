groups_num = int(input())

count_musala = 0
count_mont_blanc = 0
count_kilimanjaro = 0
count_k2 = 0
count_everest = 0

total_people = 0

for num in range(groups_num):
    group_size = int(input())
    total_people += group_size

    if group_size <= 5:
        count_musala += group_size
    elif 6 <= group_size <= 12:
        count_mont_blanc += group_size
    elif 13 <= group_size <= 25:
        count_kilimanjaro += group_size
    elif 25 <= group_size <= 40:
        count_k2 += group_size
    elif group_size >= 41:
        count_everest += group_size

percent_musala = (count_musala / total_people) * 100
percent_mont_blanc = (count_mont_blanc / total_people) * 100
percent_kilimanjaro = (count_kilimanjaro / total_people) * 100
percent_k2 = (count_k2 / total_people) * 100
percent_everest = (count_everest / total_people) * 100

print(f'{percent_musala:.2f}%')
print(f'{percent_mont_blanc:.2f}%')
print(f'{percent_kilimanjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')