users = ['Mike', 'Rachel', 'Louis', 'Harvey', 'Jessica', 'Daniel']
rated = ['****', '****', '****', '*****', '****', '**']
for user in users:
    print(user)    

print("----------------------------")

singleUser = 'Harvey Specter'
for c in singleUser:
    print(c)

print("----------------------------")

for user in users:
    if user == 'Albert':
        continue
    print(user)

print("----------------------------")

for user in users:
    if user == 'Jessica':
        break
    print(user)

print("----------------------------")

for user in users:
    for rate in rated:
        print(user + ' has ' + rate)
        if user == user:
            break
        