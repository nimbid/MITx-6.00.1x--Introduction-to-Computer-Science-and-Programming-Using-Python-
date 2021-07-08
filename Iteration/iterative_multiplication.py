def multiply(a, b):
    product = 0
    while b > 0:
        product += a
        b -= 1
    return product

a = int(input("Enter number to multiply: "))
b = int(input("Enter the number with which you want to multiply "+str(a)+": "))
print("Product: "+ str(multiply(a, b)))
