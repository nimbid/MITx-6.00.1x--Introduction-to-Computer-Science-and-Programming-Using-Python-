def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter number to find factorial of: "))
print("Factorial: "+ str(factorial(n)))
