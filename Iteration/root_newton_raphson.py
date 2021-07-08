epsilon = 0.01
y = 24.0
guess = y/2.0
num_guesses = 0
while abs(guess**2-y) >= epsilon:
    num_guesses += 1
    guess = guess - (guess**2 - y)/(2*guess)
print('No. of guess: '+str(num_guesses))
print('Square root of '+str(y)+' is about '+str(guess))
