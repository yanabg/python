most_powerful_word = ""
max_strength = 0
vowels = 'aeiouyAEIOUY'

while True:
    word = input()
    if word == "End of words":
        break
    # Calculate the sum of ASCII values of all characters in the word
    word_strength = 0
    for char in word:
        word_strength += ord(char)

    # Check if the first character is a vowel
    if word[0] in vowels:
        word_strength *= len(word)
    else:
        word_strength //= len(word) # integer division

    # update the most_powerful_word if current word strenght is greater
    if word_strength > max_strength:
        max_strength = word_strength
        most_powerful_word = word

print(f'The most powerful word is {most_powerful_word} - {max_strength}')

