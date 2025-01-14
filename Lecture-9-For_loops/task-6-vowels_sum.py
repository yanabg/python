word = input()

vowels_sum = 0

for letter in word:
    if letter == 'a':
        vowels_sum += 1
    elif letter == 'o':
        vowels_sum += 4
    elif letter == 'i':
        vowels_sum += 3
    elif letter == 'u':
        vowels_sum += 5
    elif letter == 'e':
        vowels_sum += 2

print(vowels_sum)