myWord = input("Type a word: ")

wordLista = ['hello', 'world', 'from', 'python', 'here', 'xbox', 'playstation', 'nintendo']

if wordLista.count(myWord):
    print("CONGRATS <<"+myWord+">> is in the list")
else:
    print("BUUUUUU!!!!! <<"+myWord+">> is not in the list")