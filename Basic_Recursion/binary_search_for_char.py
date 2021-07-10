# Implement a binary search based function to check if a character
# is in a given string, using recursion.


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Check for zero length
    if len(aStr) == 0:
        return False
    # Check for length of 1.
    elif len(aStr) <= 1:
        return char == aStr
    # Char is middle character.
    elif char == aStr[len(aStr)//2]:
        return True
    # Char located in first half of string.
    elif char < aStr[len(aStr)//2]:
        return isIn(char, aStr[0:len(aStr)//2])
    # Char located in second half of string.
    elif char > aStr[len(aStr)//2]:
        return isIn(char, aStr[len(aStr)//2 + 1:len(aStr)])

def main():
    str = input("Enter a string: ")
    char = input("Enter a character you want to verify being in the string: ")
    sorted_chars = sorted(str)
    sorted_str = "".join(sorted_chars)
    if isIn(char, sorted_str) == True:
        print(char+" is in "+str)
    else:
        print(char+" is not in "+str)

if __name__ == "__main__":
    # execute only if run as a script
    main()
