count = 0

while count < 5:
    print(f'Count is: {count}')
    count +=1

    if count == 3:
        print(f'Breaking the loop')
        break

else:
    print(f'Count is no longer less than 5')