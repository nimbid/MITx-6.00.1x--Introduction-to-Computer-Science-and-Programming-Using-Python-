def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = min(a,b)
    while (a % gcd != 0 or b % gcd != 0):
        gcd -= 1
        if gcd == 1:
            break
    return gcd

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD of "+str(a)+" and "+str(b)+" is "+str(gcdIter(a,b)))
