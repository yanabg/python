FACEBOOK = 150
INSTAGRAM = 100
REDDIT = 50

open_tabs_count = int(input())
salary = int(input())

for i in range(open_tabs_count):
    website = input()
    if website == "Facebook":
        salary -= FACEBOOK
    elif website == "Instagram":
        salary -= INSTAGRAM
    elif website == "Reddit":
        salary -= REDDIT

    if salary <= 0:
        print(f'You have lost your salary.')
        break
else:
    print(f'{int(salary)}')