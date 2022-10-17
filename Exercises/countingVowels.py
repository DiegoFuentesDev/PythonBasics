def countingVowels(word):
    vowels = 0
    for letter in word:
        if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' or letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            vowels += 1
    return print(str(vowels) + ' vowels')

word = str(input('Type a word: '))

countingVowels(word)