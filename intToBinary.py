n=int (input ("Enter a number: "))
binary= []
while(n>0):
    division=n%2
    binary.append(division)
    n=n//2
binary.reverse()
print("Binary Equivalent is: ")
for i in binary:
    print(i,end="")