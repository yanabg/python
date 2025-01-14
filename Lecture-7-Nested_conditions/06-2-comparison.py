number = int(input())

if number > 5:
    if number < 10:
        if number % 2 == 0:
            print("even")
        else:
            print("odd")
    else:
        print("number is out of range")
else:
    print("number is out of range")