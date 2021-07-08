def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base,exp-1)

def check_int_or_float(num):
    try:
        # Convert it into integer
        val = int(num)
        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(num)
            return False
        except ValueError:
            return False

def main():
    is_valid_base =  False
    is_valid_exp = False
    base = input("Enter base: ")
    if check_int_or_float(base) == True:
        base = int(base)
        is_valid_base = True
    elif check_int_or_float(base) == False:
        base = float(base)
        is_valid_base =  True
    else:
        print("Base needs to be an int or float.")
    exp = input("Enter exponent: ")
    if check_int_or_float(exp) == True:
        exp = int(exp)
        if exp < 0:
            print("Exponent needs to be an integer greater than or equal to zero.")
        else:
            is_valid_exp = True
    if is_valid_exp == True and is_valid_base == True:
        print("Power: "+ str(recurPower(base, exp)))

if __name__=="__main__":
    main()
