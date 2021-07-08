def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
        
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD of "+str(a)+" and "+str(b)+" is "+str(gcdRecur(a,b)))
