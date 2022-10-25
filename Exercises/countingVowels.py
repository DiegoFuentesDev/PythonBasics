def countingVowels(word):
    vowels = 0
    for letter in word:
        lowerLetter = letter.lower()
        if lowerLetter == 'a' or lowerLetter == 'e' or lowerLetter == 'i' or lowerLetter == 'o' or lowerLetter == 'u':
            vowels += 1
    return print(str(vowels) + ' vowels')

word = str(input('Type a word: '))

countingVowels(word)