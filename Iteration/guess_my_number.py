# Interactive guessing game for guessing integer between 0 (inclusive) and 100 (non-inclusive)

low = 0
high = 100
guess = 0
print('Please think of a number between 0 and 100!')
while True:
    guess = (high+low)//2
    print('Is your secret number '+str(guess)+' ?')
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate\
 the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_input == 'l':
        low = guess
    elif user_input == 'h':
        high = guess
    elif user_input == 'c':
        print('Game over. Your secret number was: '+str(guess))
        break
    else:
        print('Sorry, I did not understand your input.')
