#The <<divide and conquer>> technique consists of decomposing the problem into a set of smaller subproblems. These subproblems are then solved and the solutions are combined to obtain the solution to the original problem.

index = 0

def potencia(x,n):
    global index
    index += 1
    print(index)
    if(n == 0):
        return 1
    else: 
        if(n == 1):
            return x
        else:
            if(n % 2 == 0):
                return potencia(x*x, n//2) 
            else:
                return potencia(x*x, n//2) * x    


numero = 0
x = int(input(f"Escriba la base {numero}: "))
n = int(input(f"Escriba el exponente {numero}: "))

print(potencia(x,n))