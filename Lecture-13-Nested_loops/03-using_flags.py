flag = False

for hour in range(0, 24):
    for minute in range(0, 60):
        if hour == 5:
            flag = True
            break
        print(f'{hour}:{minute}')
    if flag:
        break