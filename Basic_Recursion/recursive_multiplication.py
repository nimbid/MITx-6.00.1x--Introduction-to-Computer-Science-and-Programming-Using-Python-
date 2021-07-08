def multiply(a,b):
    product = 0
    if b == 1:
        return a
    else:
        return a + multiply(a,b-1)

a = int(input("Enter number to multiply: "))
b = int(input("Enter the number with which you want to multiply "+str(a)+": "))
print("Product: "+ str(multiply(a, b)))
