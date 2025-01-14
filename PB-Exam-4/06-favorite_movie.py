import sys

best_movie = None
best_score = -sys.maxsize - 1
count = 0

while count < 7:
    title = input()
    if title == "STOP":
        break

    length = len(title)
    score = 0

    for char in title:
        if 'a' <= char <= 'z': # check if the character is lowercase letter
            score += ord(char) - 2 * length
        elif 'A' <= char <= 'Z': # check if character is uppercase
            score += ord(char) - length
        else:
            score += ord(char)

    if score > best_score:
        best_score = score
        best_movie = title

    count += 1

    if count == 7:
        print(f'The limit is reached.')
        break
print(f'The best movie for you is {best_movie} with {best_score} ASCII sum.')