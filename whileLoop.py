i = 0

while i < 100:
    i += 1
    if i % 8 == 0:
        print("BUZZ")
        continue
    if i % 79 == 0:
        print("Bye")
        break
    print(i)