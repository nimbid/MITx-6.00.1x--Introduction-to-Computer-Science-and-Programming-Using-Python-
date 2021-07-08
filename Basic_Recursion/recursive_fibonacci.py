def fibonacci(n):
    '''
    assumes n is an int >= 0
    return fibonnaci for n
    '''
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
n = int(input("What number do you want the Fibonacci of? "))
print("Fibonacci series position "+str(n)+" has "+str(fibonacci(n)))
