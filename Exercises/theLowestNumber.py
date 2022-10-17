myList = [13,56,43,4,5,4,5,4,3,4,5,67,87,89,9,7,54,3,32,4,5,7,7,5,34,5, -4, -23, -1]

lowest = 'init'

for i in myList:
    if lowest == 'init':
        lowest = i
    else:
        lowest = i if i < lowest else lowest

print(lowest)