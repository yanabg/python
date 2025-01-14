a = 1

while a <= 10:
    a +=1
    if a % 2 != 0: # odd number
        continue

    if a == 8:
        break

    print(a)

#    a +=1 # this step must be before the if, otherwise again infinite loop