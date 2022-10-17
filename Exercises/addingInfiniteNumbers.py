def adding(stop):
    listNumbers = []
    while True:
        value = input("Type a number to being added, to stop type 'stop': ")
        if value == 'stop':
            break
        else:
            try:
                value = int(value)
                listNumbers.append(value)
            except:
                print('Invalid data')
                exit()
        sum = 0
        for number in listNumbers:
            sum += number
    print('The sumatory is: ' + str(sum))

print("Calculator")
adding(True)