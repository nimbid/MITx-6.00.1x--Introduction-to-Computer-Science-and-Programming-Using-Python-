# Using binary search.
# Handles all positive numbers.

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

x =  input('Enter to number to find the square root of: ')
if check_int_or_float(x) == True:
    x = int(x)
elif check_int_or_float(x) == False:
    x = float(x)
epsilon = 0.01
num_guesses = 0
# For positive numbers less than 1, i.e., positive fractions.
if x < 1 and x > 0:
    low = x
    high = 1.0
    ans = (high+low)/2.0
    while abs(ans**2 - x) >= epsilon:
        print('low = '+str(low)+' high = '+str(high)+' ans = '+str(ans))
        num_guesses += 1
        if ans**2 > x and ans**2 < 1:
            high = ans
        else:
            low = ans
        ans = (high+low)/2.0
# For positive numbers greater than or equal to 1.
elif x >= 1:
    low = 1.0
    high = x
    ans = (high+low)/2.0
    while abs(ans**2 - x) >= epsilon:
        print('low = '+str(low)+' high = '+str(high)+' ans = '+str(ans))
        num_guesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
print('num_guesses = '+str(num_guesses))
print(str(ans)+' is close to the square root of '+str(x))
