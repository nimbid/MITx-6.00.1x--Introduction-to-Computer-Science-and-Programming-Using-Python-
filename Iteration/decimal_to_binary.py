num = int(input("Type in a number to be converted to binary: "))
if num < 0:
    is_negative = True
    num = abs(num)
else:
    is_negative = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2)+result
    print(result)
    num = num // 2
if is_negative is True:
    result  = '-' + result
print(result)
