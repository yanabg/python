c, o, n = False, False, False
word = ""

while True: # Loop runs indefinitely until the user inputs "End"
    letter = input()
    if letter == "End":
        break

    # processing letter ->
    if letter not in "con" and letter.isalpha():
        word += letter
        continue

    # Handling Special Letters 'c', 'o', and 'n':
    if c and letter == "c":
        word += "c"
    elif o and letter == "o":
        word += "o"
    elif n and letter == "n":
        word += "n"

    if not c and letter == "c":
        c = True
    elif not o and letter == "o":
        o = True
    elif not n and letter == "n":
        n = True

    # Checking Completion and Resetting:
    if c and o and n:
        print(word, end=" ")
        word = ""
        c = False
        o = False
        n = False
