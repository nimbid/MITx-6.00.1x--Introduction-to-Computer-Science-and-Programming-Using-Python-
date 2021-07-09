def isPalindrome(str):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = c + ans
        return ans
    def checkPalindrome(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPalindrome(s[1:-1])
    return checkPalindrome(toChars(str))

str = input("Enter string to check for palindrome: ")
if isPalindrome(str) == True:
    print("String "+str+" is a palindrome.")
else:
    print("String "+str+" is not a palindrome.")
